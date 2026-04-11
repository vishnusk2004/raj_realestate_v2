(function () {
    "use strict";

    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) {
            return parts.pop().split(";").shift();
        }
        return "";
    }

    async function getPresignedUpload(file, kind) {
        const response = await fetch("/api/uploads/presign/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken"),
            },
            body: JSON.stringify({
                filename: file.name,
                content_type: file.type,
                size: file.size,
                kind: kind,
                folder: "property-listings",
            }),
        });

        const data = await response.json();
        if (!response.ok || !data.success) {
            throw new Error(data.error || "Unable to initialize upload");
        }

        return data;
    }

    async function uploadToS3(uploadData, file) {
        const formData = new FormData();
        Object.keys(uploadData.upload.fields).forEach(function (key) {
            formData.append(key, uploadData.upload.fields[key]);
        });
        formData.append("file", file);

        const response = await fetch(uploadData.upload.url, {
            method: "POST",
            body: formData,
        });

        if (!response.ok) {
            throw new Error("Direct upload to S3 failed");
        }
    }

    function setStatus(message, isError) {
        let el = document.getElementById("direct-upload-status");
        if (!el) {
            el = document.createElement("div");
            el.id = "direct-upload-status";
            el.style.margin = "10px 0";
            el.style.padding = "8px 10px";
            el.style.borderRadius = "4px";
            const submitRow = document.querySelector(".submit-row");
            if (submitRow && submitRow.parentNode) {
                submitRow.parentNode.insertBefore(el, submitRow);
            }
        }

        el.textContent = message;
        el.style.background = isError ? "#fdecea" : "#eaf7ee";
        el.style.color = isError ? "#b42318" : "#067647";
        el.style.border = isError ? "1px solid #f5c2c7" : "1px solid #abefc6";
    }

    document.addEventListener("DOMContentLoaded", function () {
        // Only run on object edit pages; changelist has no media fields.
        const isChangePage = window.location.pathname.includes("/change/");
        if (!isChangePage) {
            return;
        }
        
        // Main change form in Django admin.
        let form = document.querySelector("form#propertylisting_form");
        
        // Fallback: find the form that contains the expected media fields.
        if (!form) {
            const allForms = document.querySelectorAll("form");
            
            for (let i = 0; i < allForms.length; i++) {
                const f = allForms[i];
                const imageFileInput =
                    f.querySelector("#id_image_file") || f.querySelector("input[name='image_file']");
                const videoFileInput =
                    f.querySelector("#id_video_file") || f.querySelector("input[name='video_file']");
                
                if (imageFileInput && videoFileInput) {
                    form = f;
                    break;
                }
            }
        }
        
        if (!form) {
            return;
        }

        const imageInput = form.querySelector("#id_image_file") || form.querySelector("input[name='image_file']");
        const videoInput = form.querySelector("#id_video_file") || form.querySelector("input[name='video_file']");
        const imageUrlInput = form.querySelector("#id_image_url") || form.querySelector("input[name='image_url']");
        const videoUrlInput = form.querySelector("#id_video_url") || form.querySelector("input[name='video_url']");

        if (!imageInput || !videoInput || !imageUrlInput || !videoUrlInput) {
            return;
        }

        form.addEventListener("submit", async function (event) {
            const imageFile = imageInput.files && imageInput.files[0] ? imageInput.files[0] : null;
            const videoFile = videoInput.files && videoInput.files[0] ? videoInput.files[0] : null;

            if (!imageFile && !videoFile) {
                return;
            }
            event.preventDefault();

            const submitButtons = form.querySelectorAll("input[type='submit'], button[type='submit']");
            submitButtons.forEach(function (btn) {
                btn.disabled = true;
            });

            try {
                setStatus("Uploading media directly to S3...", false);

                if (imageFile) {
                    const imageUpload = await getPresignedUpload(imageFile, "image");
                    await uploadToS3(imageUpload, imageFile);
                    imageUrlInput.value = imageUpload.file_url;
                    imageInput.value = "";
                }

                if (videoFile) {
                    const videoUpload = await getPresignedUpload(videoFile, "video");
                    await uploadToS3(videoUpload, videoFile);
                    videoUrlInput.value = videoUpload.file_url;
                    videoInput.value = "";
                }

                setStatus("Upload complete. Saving listing...", false);
                form.submit();
            } catch (error) {
                setStatus(error.message || "Upload failed. Please try again.", true);
                submitButtons.forEach(function (btn) {
                    btn.disabled = false;
                });
            }
        });
    });
})();
