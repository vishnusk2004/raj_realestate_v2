var sm = e => {
    throw TypeError(e)
}
;
var Zl = (e, t, n) => t.has(e) || sm("Cannot " + n);
var P = (e, t, n) => (Zl(e, t, "read from private field"),
n ? n.call(e) : t.get(e))
  , ue = (e, t, n) => t.has(e) ? sm("Cannot add the same private member more than once") : t instanceof WeakSet ? t.add(e) : t.set(e, n)
  , X = (e, t, n, r) => (Zl(e, t, "write to private field"),
r ? r.call(e, n) : t.set(e, n),
n)
  , Ke = (e, t, n) => (Zl(e, t, "access private method"),
n);
var $a = (e, t, n, r) => ({
    set _(o) {
        X(e, t, o, n)
    },
    get _() {
        return P(e, t, r)
    }
});
function Hw(e, t) {
    for (var n = 0; n < t.length; n++) {
        const r = t[n];
        if (typeof r != "string" && !Array.isArray(r)) {
            for (const o in r)
                if (o !== "default" && !(o in e)) {
                    const s = Object.getOwnPropertyDescriptor(r, o);
                    s && Object.defineProperty(e, o, s.get ? s : {
                        enumerable: !0,
                        get: () => r[o]
                    })
                }
        }
    }
    return Object.freeze(Object.defineProperty(e, Symbol.toStringTag, {
        value: "Module"
    }))
}
(function() {
    const t = document.createElement("link").relList;
    if (t && t.supports && t.supports("modulepreload"))
        return;
    for (const o of document.querySelectorAll('link[rel="modulepreload"]'))
        r(o);
    new MutationObserver(o => {
        for (const s of o)
            if (s.type === "childList")
                for (const i of s.addedNodes)
                    i.tagName === "LINK" && i.rel === "modulepreload" && r(i)
    }
    ).observe(document, {
        childList: !0,
        subtree: !0
    });
    function n(o) {
        const s = {};
        return o.integrity && (s.integrity = o.integrity),
        o.referrerPolicy && (s.referrerPolicy = o.referrerPolicy),
        o.crossOrigin === "use-credentials" ? s.credentials = "include" : o.crossOrigin === "anonymous" ? s.credentials = "omit" : s.credentials = "same-origin",
        s
    }
    function r(o) {
        if (o.ep)
            return;
        o.ep = !0;
        const s = n(o);
        fetch(o.href, s)
    }
}
)();
function Ep(e) {
    return e && e.__esModule && Object.prototype.hasOwnProperty.call(e, "default") ? e.default : e
}
var Pp = {
    exports: {}
}
  , pl = {}
  , Tp = {
    exports: {}
}
  , ne = {};
/**
 * @license React
 * react.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var ja = Symbol.for("react.element")
  , Vw = Symbol.for("react.portal")
  , Uw = Symbol.for("react.fragment")
  , Yw = Symbol.for("react.strict_mode")
  , Kw = Symbol.for("react.profiler")
  , Qw = Symbol.for("react.provider")
  , Gw = Symbol.for("react.context")
  , qw = Symbol.for("react.forward_ref")
  , Xw = Symbol.for("react.suspense")
  , Jw = Symbol.for("react.memo")
  , Zw = Symbol.for("react.lazy")
  , am = Symbol.iterator;
function e1(e) {
    return e === null || typeof e != "object" ? null : (e = am && e[am] || e["@@iterator"],
    typeof e == "function" ? e : null)
}
var Mp = {
    isMounted: function() {
        return !1
    },
    enqueueForceUpdate: function() {},
    enqueueReplaceState: function() {},
    enqueueSetState: function() {}
}
  , Rp = Object.assign
  , _p = {};
function us(e, t, n) {
    this.props = e,
    this.context = t,
    this.refs = _p,
    this.updater = n || Mp
}
us.prototype.isReactComponent = {};
us.prototype.setState = function(e, t) {
    if (typeof e != "object" && typeof e != "function" && e != null)
        throw Error("setState(...): takes an object of state variables to update or a function which returns an object of state variables.");
    this.updater.enqueueSetState(this, e, t, "setState")
}
;
us.prototype.forceUpdate = function(e) {
    this.updater.enqueueForceUpdate(this, e, "forceUpdate")
}
;
function Dp() {}
Dp.prototype = us.prototype;
function gd(e, t, n) {
    this.props = e,
    this.context = t,
    this.refs = _p,
    this.updater = n || Mp
}
var yd = gd.prototype = new Dp;
yd.constructor = gd;
Rp(yd, us.prototype);
yd.isPureReactComponent = !0;
var im = Array.isArray
  , Op = Object.prototype.hasOwnProperty
  , xd = {
    current: null
}
  , Ap = {
    key: !0,
    ref: !0,
    __self: !0,
    __source: !0
};
function Ip(e, t, n) {
    var r, o = {}, s = null, i = null;
    if (t != null)
        for (r in t.ref !== void 0 && (i = t.ref),
        t.key !== void 0 && (s = "" + t.key),
        t)
            Op.call(t, r) && !Ap.hasOwnProperty(r) && (o[r] = t[r]);
    var l = arguments.length - 2;
    if (l === 1)
        o.children = n;
    else if (1 < l) {
        for (var c = Array(l), u = 0; u < l; u++)
            c[u] = arguments[u + 2];
        o.children = c
    }
    if (e && e.defaultProps)
        for (r in l = e.defaultProps,
        l)
            o[r] === void 0 && (o[r] = l[r]);
    return {
        $$typeof: ja,
        type: e,
        key: s,
        ref: i,
        props: o,
        _owner: xd.current
    }
}
function t1(e, t) {
    return {
        $$typeof: ja,
        type: e.type,
        key: t,
        ref: e.ref,
        props: e.props,
        _owner: e._owner
    }
}
function wd(e) {
    return typeof e == "object" && e !== null && e.$$typeof === ja
}
function n1(e) {
    var t = {
        "=": "=0",
        ":": "=2"
    };
    return "$" + e.replace(/[=:]/g, function(n) {
        return t[n]
    })
}
var lm = /\/+/g;
function ec(e, t) {
    return typeof e == "object" && e !== null && e.key != null ? n1("" + e.key) : t.toString(36)
}
function mi(e, t, n, r, o) {
    var s = typeof e;
    (s === "undefined" || s === "boolean") && (e = null);
    var i = !1;
    if (e === null)
        i = !0;
    else
        switch (s) {
        case "string":
        case "number":
            i = !0;
            break;
        case "object":
            switch (e.$$typeof) {
            case ja:
            case Vw:
                i = !0
            }
        }
    if (i)
        return i = e,
        o = o(i),
        e = r === "" ? "." + ec(i, 0) : r,
        im(o) ? (n = "",
        e != null && (n = e.replace(lm, "$&/") + "/"),
        mi(o, t, n, "", function(u) {
            return u
        })) : o != null && (wd(o) && (o = t1(o, n + (!o.key || i && i.key === o.key ? "" : ("" + o.key).replace(lm, "$&/") + "/") + e)),
        t.push(o)),
        1;
    if (i = 0,
    r = r === "" ? "." : r + ":",
    im(e))
        for (var l = 0; l < e.length; l++) {
            s = e[l];
            var c = r + ec(s, l);
            i += mi(s, t, n, c, o)
        }
    else if (c = e1(e),
    typeof c == "function")
        for (e = c.call(e),
        l = 0; !(s = e.next()).done; )
            s = s.value,
            c = r + ec(s, l++),
            i += mi(s, t, n, c, o);
    else if (s === "object")
        throw t = String(e),
        Error("Objects are not valid as a React child (found: " + (t === "[object Object]" ? "object with keys {" + Object.keys(e).join(", ") + "}" : t) + "). If you meant to render a collection of children, use an array instead.");
    return i
}
function Ba(e, t, n) {
    if (e == null)
        return e;
    var r = []
      , o = 0;
    return mi(e, r, "", "", function(s) {
        return t.call(n, s, o++)
    }),
    r
}
function r1(e) {
    if (e._status === -1) {
        var t = e._result;
        t = t(),
        t.then(function(n) {
            (e._status === 0 || e._status === -1) && (e._status = 1,
            e._result = n)
        }, function(n) {
            (e._status === 0 || e._status === -1) && (e._status = 2,
            e._result = n)
        }),
        e._status === -1 && (e._status = 0,
        e._result = t)
    }
    if (e._status === 1)
        return e._result.default;
    throw e._result
}
var st = {
    current: null
}
  , hi = {
    transition: null
}
  , o1 = {
    ReactCurrentDispatcher: st,
    ReactCurrentBatchConfig: hi,
    ReactCurrentOwner: xd
};
function Lp() {
    throw Error("act(...) is not supported in production builds of React.")
}
ne.Children = {
    map: Ba,
    forEach: function(e, t, n) {
        Ba(e, function() {
            t.apply(this, arguments)
        }, n)
    },
    count: function(e) {
        var t = 0;
        return Ba(e, function() {
            t++
        }),
        t
    },
    toArray: function(e) {
        return Ba(e, function(t) {
            return t
        }) || []
    },
    only: function(e) {
        if (!wd(e))
            throw Error("React.Children.only expected to receive a single React element child.");
        return e
    }
};
ne.Component = us;
ne.Fragment = Uw;
ne.Profiler = Kw;
ne.PureComponent = gd;
ne.StrictMode = Yw;
ne.Suspense = Xw;
ne.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED = o1;
ne.act = Lp;
ne.cloneElement = function(e, t, n) {
    if (e == null)
        throw Error("React.cloneElement(...): The argument must be a React element, but you passed " + e + ".");
    var r = Rp({}, e.props)
      , o = e.key
      , s = e.ref
      , i = e._owner;
    if (t != null) {
        if (t.ref !== void 0 && (s = t.ref,
        i = xd.current),
        t.key !== void 0 && (o = "" + t.key),
        e.type && e.type.defaultProps)
            var l = e.type.defaultProps;
        for (c in t)
            Op.call(t, c) && !Ap.hasOwnProperty(c) && (r[c] = t[c] === void 0 && l !== void 0 ? l[c] : t[c])
    }
    var c = arguments.length - 2;
    if (c === 1)
        r.children = n;
    else if (1 < c) {
        l = Array(c);
        for (var u = 0; u < c; u++)
            l[u] = arguments[u + 2];
        r.children = l
    }
    return {
        $$typeof: ja,
        type: e.type,
        key: o,
        ref: s,
        props: r,
        _owner: i
    }
}
;
ne.createContext = function(e) {
    return e = {
        $$typeof: Gw,
        _currentValue: e,
        _currentValue2: e,
        _threadCount: 0,
        Provider: null,
        Consumer: null,
        _defaultValue: null,
        _globalName: null
    },
    e.Provider = {
        $$typeof: Qw,
        _context: e
    },
    e.Consumer = e
}
;
ne.createElement = Ip;
ne.createFactory = function(e) {
    var t = Ip.bind(null, e);
    return t.type = e,
    t
}
;
ne.createRef = function() {
    return {
        current: null
    }
}
;
ne.forwardRef = function(e) {
    return {
        $$typeof: qw,
        render: e
    }
}
;
ne.isValidElement = wd;
ne.lazy = function(e) {
    return {
        $$typeof: Zw,
        _payload: {
            _status: -1,
            _result: e
        },
        _init: r1
    }
}
;
ne.memo = function(e, t) {
    return {
        $$typeof: Jw,
        type: e,
        compare: t === void 0 ? null : t
    }
}
;
ne.startTransition = function(e) {
    var t = hi.transition;
    hi.transition = {};
    try {
        e()
    } finally {
        hi.transition = t
    }
}
;
ne.unstable_act = Lp;
ne.useCallback = function(e, t) {
    return st.current.useCallback(e, t)
}
;
ne.useContext = function(e) {
    return st.current.useContext(e)
}
;
ne.useDebugValue = function() {}
;
ne.useDeferredValue = function(e) {
    return st.current.useDeferredValue(e)
}
;
ne.useEffect = function(e, t) {
    return st.current.useEffect(e, t)
}
;
ne.useId = function() {
    return st.current.useId()
}
;
ne.useImperativeHandle = function(e, t, n) {
    return st.current.useImperativeHandle(e, t, n)
}
;
ne.useInsertionEffect = function(e, t) {
    return st.current.useInsertionEffect(e, t)
}
;
ne.useLayoutEffect = function(e, t) {
    return st.current.useLayoutEffect(e, t)
}
;
ne.useMemo = function(e, t) {
    return st.current.useMemo(e, t)
}
;
ne.useReducer = function(e, t, n) {
    return st.current.useReducer(e, t, n)
}
;
ne.useRef = function(e) {
    return st.current.useRef(e)
}
;
ne.useState = function(e) {
    return st.current.useState(e)
}
;
ne.useSyncExternalStore = function(e, t, n) {
    return st.current.useSyncExternalStore(e, t, n)
}
;
ne.useTransition = function() {
    return st.current.useTransition()
}
;
ne.version = "18.3.1";
Tp.exports = ne;
var m = Tp.exports;
const I = Ep(m)
  , bd = Hw({
    __proto__: null,
    default: I
}, [m]);
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var s1 = m
  , a1 = Symbol.for("react.element")
  , i1 = Symbol.for("react.fragment")
  , l1 = Object.prototype.hasOwnProperty
  , c1 = s1.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner
  , u1 = {
    key: !0,
    ref: !0,
    __self: !0,
    __source: !0
};
function Fp(e, t, n) {
    var r, o = {}, s = null, i = null;
    n !== void 0 && (s = "" + n),
    t.key !== void 0 && (s = "" + t.key),
    t.ref !== void 0 && (i = t.ref);
    for (r in t)
        l1.call(t, r) && !u1.hasOwnProperty(r) && (o[r] = t[r]);
    if (e && e.defaultProps)
        for (r in t = e.defaultProps,
        t)
            o[r] === void 0 && (o[r] = t[r]);
    return {
        $$typeof: a1,
        type: e,
        key: s,
        ref: i,
        props: o,
        _owner: c1.current
    }
}
pl.Fragment = i1;
pl.jsx = Fp;
pl.jsxs = Fp;
Pp.exports = pl;
var a = Pp.exports
  , zp = {
    exports: {}
}
  , Nt = {}
  , $p = {
    exports: {}
}
  , Bp = {};
/**
 * @license React
 * scheduler.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
(function(e) {
    function t(j, E) {
        var L = j.length;
        j.push(E);
        e: for (; 0 < L; ) {
            var U = L - 1 >>> 1
              , H = j[U];
            if (0 < o(H, E))
                j[U] = E,
                j[L] = H,
                L = U;
            else
                break e
        }
    }
    function n(j) {
        return j.length === 0 ? null : j[0]
    }
    function r(j) {
        if (j.length === 0)
            return null;
        var E = j[0]
          , L = j.pop();
        if (L !== E) {
            j[0] = L;
            e: for (var U = 0, H = j.length, J = H >>> 1; U < J; ) {
                var G = 2 * (U + 1) - 1
                  , xe = j[G]
                  , Me = G + 1
                  , z = j[Me];
                if (0 > o(xe, L))
                    Me < H && 0 > o(z, xe) ? (j[U] = z,
                    j[Me] = L,
                    U = Me) : (j[U] = xe,
                    j[G] = L,
                    U = G);
                else if (Me < H && 0 > o(z, L))
                    j[U] = z,
                    j[Me] = L,
                    U = Me;
                else
                    break e
            }
        }
        return E
    }
    function o(j, E) {
        var L = j.sortIndex - E.sortIndex;
        return L !== 0 ? L : j.id - E.id
    }
    if (typeof performance == "object" && typeof performance.now == "function") {
        var s = performance;
        e.unstable_now = function() {
            return s.now()
        }
    } else {
        var i = Date
          , l = i.now();
        e.unstable_now = function() {
            return i.now() - l
        }
    }
    var c = []
      , u = []
      , d = 1
      , f = null
      , g = 3
      , h = !1
      , b = !1
      , v = !1
      , w = typeof setTimeout == "function" ? setTimeout : null
      , y = typeof clearTimeout == "function" ? clearTimeout : null
      , p = typeof setImmediate < "u" ? setImmediate : null;
    typeof navigator < "u" && navigator.scheduling !== void 0 && navigator.scheduling.isInputPending !== void 0 && navigator.scheduling.isInputPending.bind(navigator.scheduling);
    function x(j) {
        for (var E = n(u); E !== null; ) {
            if (E.callback === null)
                r(u);
            else if (E.startTime <= j)
                r(u),
                E.sortIndex = E.expirationTime,
                t(c, E);
            else
                break;
            E = n(u)
        }
    }
    function N(j) {
        if (v = !1,
        x(j),
        !b)
            if (n(c) !== null)
                b = !0,
                $(S);
            else {
                var E = n(u);
                E !== null && M(N, E.startTime - j)
            }
    }
    function S(j, E) {
        b = !1,
        v && (v = !1,
        y(T),
        T = -1),
        h = !0;
        var L = g;
        try {
            for (x(E),
            f = n(c); f !== null && (!(f.expirationTime > E) || j && !F()); ) {
                var U = f.callback;
                if (typeof U == "function") {
                    f.callback = null,
                    g = f.priorityLevel;
                    var H = U(f.expirationTime <= E);
                    E = e.unstable_now(),
                    typeof H == "function" ? f.callback = H : f === n(c) && r(c),
                    x(E)
                } else
                    r(c);
                f = n(c)
            }
            if (f !== null)
                var J = !0;
            else {
                var G = n(u);
                G !== null && M(N, G.startTime - E),
                J = !1
            }
            return J
        } finally {
            f = null,
            g = L,
            h = !1
        }
    }
    var k = !1
      , C = null
      , T = -1
      , D = 5
      , R = -1;
    function F() {
        return !(e.unstable_now() - R < D)
    }
    function A() {
        if (C !== null) {
            var j = e.unstable_now();
            R = j;
            var E = !0;
            try {
                E = C(!0, j)
            } finally {
                E ? W() : (k = !1,
                C = null)
            }
        } else
            k = !1
    }
    var W;
    if (typeof p == "function")
        W = function() {
            p(A)
        }
        ;
    else if (typeof MessageChannel < "u") {
        var O = new MessageChannel
          , V = O.port2;
        O.port1.onmessage = A,
        W = function() {
            V.postMessage(null)
        }
    } else
        W = function() {
            w(A, 0)
        }
        ;
    function $(j) {
        C = j,
        k || (k = !0,
        W())
    }
    function M(j, E) {
        T = w(function() {
            j(e.unstable_now())
        }, E)
    }
    e.unstable_IdlePriority = 5,
    e.unstable_ImmediatePriority = 1,
    e.unstable_LowPriority = 4,
    e.unstable_NormalPriority = 3,
    e.unstable_Profiling = null,
    e.unstable_UserBlockingPriority = 2,
    e.unstable_cancelCallback = function(j) {
        j.callback = null
    }
    ,
    e.unstable_continueExecution = function() {
        b || h || (b = !0,
        $(S))
    }
    ,
    e.unstable_forceFrameRate = function(j) {
        0 > j || 125 < j ? console.error("forceFrameRate takes a positive int between 0 and 125, forcing frame rates higher than 125 fps is not supported") : D = 0 < j ? Math.floor(1e3 / j) : 5
    }
    ,
    e.unstable_getCurrentPriorityLevel = function() {
        return g
    }
    ,
    e.unstable_getFirstCallbackNode = function() {
        return n(c)
    }
    ,
    e.unstable_next = function(j) {
        switch (g) {
        case 1:
        case 2:
        case 3:
            var E = 3;
            break;
        default:
            E = g
        }
        var L = g;
        g = E;
        try {
            return j()
        } finally {
            g = L
        }
    }
    ,
    e.unstable_pauseExecution = function() {}
    ,
    e.unstable_requestPaint = function() {}
    ,
    e.unstable_runWithPriority = function(j, E) {
        switch (j) {
        case 1:
        case 2:
        case 3:
        case 4:
        case 5:
            break;
        default:
            j = 3
        }
        var L = g;
        g = j;
        try {
            return E()
        } finally {
            g = L
        }
    }
    ,
    e.unstable_scheduleCallback = function(j, E, L) {
        var U = e.unstable_now();
        switch (typeof L == "object" && L !== null ? (L = L.delay,
        L = typeof L == "number" && 0 < L ? U + L : U) : L = U,
        j) {
        case 1:
            var H = -1;
            break;
        case 2:
            H = 250;
            break;
        case 5:
            H = 1073741823;
            break;
        case 4:
            H = 1e4;
            break;
        default:
            H = 5e3
        }
        return H = L + H,
        j = {
            id: d++,
            callback: E,
            priorityLevel: j,
            startTime: L,
            expirationTime: H,
            sortIndex: -1
        },
        L > U ? (j.sortIndex = L,
        t(u, j),
        n(c) === null && j === n(u) && (v ? (y(T),
        T = -1) : v = !0,
        M(N, L - U))) : (j.sortIndex = H,
        t(c, j),
        b || h || (b = !0,
        $(S))),
        j
    }
    ,
    e.unstable_shouldYield = F,
    e.unstable_wrapCallback = function(j) {
        var E = g;
        return function() {
            var L = g;
            g = E;
            try {
                return j.apply(this, arguments)
            } finally {
                g = L
            }
        }
    }
}
)(Bp);
$p.exports = Bp;
var d1 = $p.exports;
/**
 * @license React
 * react-dom.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var f1 = m
  , wt = d1;
function _(e) {
    for (var t = "https://reactjs.org/docs/error-decoder.html?invariant=" + e, n = 1; n < arguments.length; n++)
        t += "&args[]=" + encodeURIComponent(arguments[n]);
    return "Minified React error #" + e + "; visit " + t + " for the full message or use the non-minified dev environment for full errors and additional helpful warnings."
}
var Wp = new Set
  , qs = {};
function oo(e, t) {
    qo(e, t),
    qo(e + "Capture", t)
}
function qo(e, t) {
    for (qs[e] = t,
    e = 0; e < t.length; e++)
        Wp.add(t[e])
}
var Dn = !(typeof window > "u" || typeof window.document > "u" || typeof window.document.createElement > "u")
  , Qc = Object.prototype.hasOwnProperty
  , m1 = /^[:A-Z_a-z\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u02FF\u0370-\u037D\u037F-\u1FFF\u200C-\u200D\u2070-\u218F\u2C00-\u2FEF\u3001-\uD7FF\uF900-\uFDCF\uFDF0-\uFFFD][:A-Z_a-z\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u02FF\u0370-\u037D\u037F-\u1FFF\u200C-\u200D\u2070-\u218F\u2C00-\u2FEF\u3001-\uD7FF\uF900-\uFDCF\uFDF0-\uFFFD\-.0-9\u00B7\u0300-\u036F\u203F-\u2040]*$/
  , cm = {}
  , um = {};
function h1(e) {
    return Qc.call(um, e) ? !0 : Qc.call(cm, e) ? !1 : m1.test(e) ? um[e] = !0 : (cm[e] = !0,
    !1)
}
function p1(e, t, n, r) {
    if (n !== null && n.type === 0)
        return !1;
    switch (typeof t) {
    case "function":
    case "symbol":
        return !0;
    case "boolean":
        return r ? !1 : n !== null ? !n.acceptsBooleans : (e = e.toLowerCase().slice(0, 5),
        e !== "data-" && e !== "aria-");
    default:
        return !1
    }
}
function v1(e, t, n, r) {
    if (t === null || typeof t > "u" || p1(e, t, n, r))
        return !0;
    if (r)
        return !1;
    if (n !== null)
        switch (n.type) {
        case 3:
            return !t;
        case 4:
            return t === !1;
        case 5:
            return isNaN(t);
        case 6:
            return isNaN(t) || 1 > t
        }
    return !1
}
function at(e, t, n, r, o, s, i) {
    this.acceptsBooleans = t === 2 || t === 3 || t === 4,
    this.attributeName = r,
    this.attributeNamespace = o,
    this.mustUseProperty = n,
    this.propertyName = e,
    this.type = t,
    this.sanitizeURL = s,
    this.removeEmptyString = i
}
var Ve = {};
"children dangerouslySetInnerHTML defaultValue defaultChecked innerHTML suppressContentEditableWarning suppressHydrationWarning style".split(" ").forEach(function(e) {
    Ve[e] = new at(e,0,!1,e,null,!1,!1)
});
[["acceptCharset", "accept-charset"], ["className", "class"], ["htmlFor", "for"], ["httpEquiv", "http-equiv"]].forEach(function(e) {
    var t = e[0];
    Ve[t] = new at(t,1,!1,e[1],null,!1,!1)
});
["contentEditable", "draggable", "spellCheck", "value"].forEach(function(e) {
    Ve[e] = new at(e,2,!1,e.toLowerCase(),null,!1,!1)
});
["autoReverse", "externalResourcesRequired", "focusable", "preserveAlpha"].forEach(function(e) {
    Ve[e] = new at(e,2,!1,e,null,!1,!1)
});
"allowFullScreen async autoFocus autoPlay controls default defer disabled disablePictureInPicture disableRemotePlayback formNoValidate hidden loop noModule noValidate open playsInline readOnly required reversed scoped seamless itemScope".split(" ").forEach(function(e) {
    Ve[e] = new at(e,3,!1,e.toLowerCase(),null,!1,!1)
});
["checked", "multiple", "muted", "selected"].forEach(function(e) {
    Ve[e] = new at(e,3,!0,e,null,!1,!1)
});
["capture", "download"].forEach(function(e) {
    Ve[e] = new at(e,4,!1,e,null,!1,!1)
});
["cols", "rows", "size", "span"].forEach(function(e) {
    Ve[e] = new at(e,6,!1,e,null,!1,!1)
});
["rowSpan", "start"].forEach(function(e) {
    Ve[e] = new at(e,5,!1,e.toLowerCase(),null,!1,!1)
});
var Nd = /[\-:]([a-z])/g;
function Sd(e) {
    return e[1].toUpperCase()
}
"accent-height alignment-baseline arabic-form baseline-shift cap-height clip-path clip-rule color-interpolation color-interpolation-filters color-profile color-rendering dominant-baseline enable-background fill-opacity fill-rule flood-color flood-opacity font-family font-size font-size-adjust font-stretch font-style font-variant font-weight glyph-name glyph-orientation-horizontal glyph-orientation-vertical horiz-adv-x horiz-origin-x image-rendering letter-spacing lighting-color marker-end marker-mid marker-start overline-position overline-thickness paint-order panose-1 pointer-events rendering-intent shape-rendering stop-color stop-opacity strikethrough-position strikethrough-thickness stroke-dasharray stroke-dashoffset stroke-linecap stroke-linejoin stroke-miterlimit stroke-opacity stroke-width text-anchor text-decoration text-rendering underline-position underline-thickness unicode-bidi unicode-range units-per-em v-alphabetic v-hanging v-ideographic v-mathematical vector-effect vert-adv-y vert-origin-x vert-origin-y word-spacing writing-mode xmlns:xlink x-height".split(" ").forEach(function(e) {
    var t = e.replace(Nd, Sd);
    Ve[t] = new at(t,1,!1,e,null,!1,!1)
});
"xlink:actuate xlink:arcrole xlink:role xlink:show xlink:title xlink:type".split(" ").forEach(function(e) {
    var t = e.replace(Nd, Sd);
    Ve[t] = new at(t,1,!1,e,"http://www.w3.org/1999/xlink",!1,!1)
});
["xml:base", "xml:lang", "xml:space"].forEach(function(e) {
    var t = e.replace(Nd, Sd);
    Ve[t] = new at(t,1,!1,e,"http://www.w3.org/XML/1998/namespace",!1,!1)
});
["tabIndex", "crossOrigin"].forEach(function(e) {
    Ve[e] = new at(e,1,!1,e.toLowerCase(),null,!1,!1)
});
Ve.xlinkHref = new at("xlinkHref",1,!1,"xlink:href","http://www.w3.org/1999/xlink",!0,!1);
["src", "href", "action", "formAction"].forEach(function(e) {
    Ve[e] = new at(e,1,!1,e.toLowerCase(),null,!0,!0)
});
function jd(e, t, n, r) {
    var o = Ve.hasOwnProperty(t) ? Ve[t] : null;
    (o !== null ? o.type !== 0 : r || !(2 < t.length) || t[0] !== "o" && t[0] !== "O" || t[1] !== "n" && t[1] !== "N") && (v1(t, n, o, r) && (n = null),
    r || o === null ? h1(t) && (n === null ? e.removeAttribute(t) : e.setAttribute(t, "" + n)) : o.mustUseProperty ? e[o.propertyName] = n === null ? o.type === 3 ? !1 : "" : n : (t = o.attributeName,
    r = o.attributeNamespace,
    n === null ? e.removeAttribute(t) : (o = o.type,
    n = o === 3 || o === 4 && n === !0 ? "" : "" + n,
    r ? e.setAttributeNS(r, t, n) : e.setAttribute(t, n))))
}
var zn = f1.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED
  , Wa = Symbol.for("react.element")
  , wo = Symbol.for("react.portal")
  , bo = Symbol.for("react.fragment")
  , Cd = Symbol.for("react.strict_mode")
  , Gc = Symbol.for("react.profiler")
  , Hp = Symbol.for("react.provider")
  , Vp = Symbol.for("react.context")
  , kd = Symbol.for("react.forward_ref")
  , qc = Symbol.for("react.suspense")
  , Xc = Symbol.for("react.suspense_list")
  , Ed = Symbol.for("react.memo")
  , qn = Symbol.for("react.lazy")
  , Up = Symbol.for("react.offscreen")
  , dm = Symbol.iterator;
function Ss(e) {
    return e === null || typeof e != "object" ? null : (e = dm && e[dm] || e["@@iterator"],
    typeof e == "function" ? e : null)
}
var Te = Object.assign, tc;
function As(e) {
    if (tc === void 0)
        try {
            throw Error()
        } catch (n) {
            var t = n.stack.trim().match(/\n( *(at )?)/);
            tc = t && t[1] || ""
        }
    return `
` + tc + e
}
var nc = !1;
function rc(e, t) {
    if (!e || nc)
        return "";
    nc = !0;
    var n = Error.prepareStackTrace;
    Error.prepareStackTrace = void 0;
    try {
        if (t)
            if (t = function() {
                throw Error()
            }
            ,
            Object.defineProperty(t.prototype, "props", {
                set: function() {
                    throw Error()
                }
            }),
            typeof Reflect == "object" && Reflect.construct) {
                try {
                    Reflect.construct(t, [])
                } catch (u) {
                    var r = u
                }
                Reflect.construct(e, [], t)
            } else {
                try {
                    t.call()
                } catch (u) {
                    r = u
                }
                e.call(t.prototype)
            }
        else {
            try {
                throw Error()
            } catch (u) {
                r = u
            }
            e()
        }
    } catch (u) {
        if (u && r && typeof u.stack == "string") {
            for (var o = u.stack.split(`
`), s = r.stack.split(`
`), i = o.length - 1, l = s.length - 1; 1 <= i && 0 <= l && o[i] !== s[l]; )
                l--;
            for (; 1 <= i && 0 <= l; i--,
            l--)
                if (o[i] !== s[l]) {
                    if (i !== 1 || l !== 1)
                        do
                            if (i--,
                            l--,
                            0 > l || o[i] !== s[l]) {
                                var c = `
` + o[i].replace(" at new ", " at ");
                                return e.displayName && c.includes("<anonymous>") && (c = c.replace("<anonymous>", e.displayName)),
                                c
                            }
                        while (1 <= i && 0 <= l);
                    break
                }
        }
    } finally {
        nc = !1,
        Error.prepareStackTrace = n
    }
    return (e = e ? e.displayName || e.name : "") ? As(e) : ""
}
function g1(e) {
    switch (e.tag) {
    case 5:
        return As(e.type);
    case 16:
        return As("Lazy");
    case 13:
        return As("Suspense");
    case 19:
        return As("SuspenseList");
    case 0:
    case 2:
    case 15:
        return e = rc(e.type, !1),
        e;
    case 11:
        return e = rc(e.type.render, !1),
        e;
    case 1:
        return e = rc(e.type, !0),
        e;
    default:
        return ""
    }
}
function Jc(e) {
    if (e == null)
        return null;
    if (typeof e == "function")
        return e.displayName || e.name || null;
    if (typeof e == "string")
        return e;
    switch (e) {
    case bo:
        return "Fragment";
    case wo:
        return "Portal";
    case Gc:
        return "Profiler";
    case Cd:
        return "StrictMode";
    case qc:
        return "Suspense";
    case Xc:
        return "SuspenseList"
    }
    if (typeof e == "object")
        switch (e.$$typeof) {
        case Vp:
            return (e.displayName || "Context") + ".Consumer";
        case Hp:
            return (e._context.displayName || "Context") + ".Provider";
        case kd:
            var t = e.render;
            return e = e.displayName,
            e || (e = t.displayName || t.name || "",
            e = e !== "" ? "ForwardRef(" + e + ")" : "ForwardRef"),
            e;
        case Ed:
            return t = e.displayName || null,
            t !== null ? t : Jc(e.type) || "Memo";
        case qn:
            t = e._payload,
            e = e._init;
            try {
                return Jc(e(t))
            } catch {}
        }
    return null
}
function y1(e) {
    var t = e.type;
    switch (e.tag) {
    case 24:
        return "Cache";
    case 9:
        return (t.displayName || "Context") + ".Consumer";
    case 10:
        return (t._context.displayName || "Context") + ".Provider";
    case 18:
        return "DehydratedFragment";
    case 11:
        return e = t.render,
        e = e.displayName || e.name || "",
        t.displayName || (e !== "" ? "ForwardRef(" + e + ")" : "ForwardRef");
    case 7:
        return "Fragment";
    case 5:
        return t;
    case 4:
        return "Portal";
    case 3:
        return "Root";
    case 6:
        return "Text";
    case 16:
        return Jc(t);
    case 8:
        return t === Cd ? "StrictMode" : "Mode";
    case 22:
        return "Offscreen";
    case 12:
        return "Profiler";
    case 21:
        return "Scope";
    case 13:
        return "Suspense";
    case 19:
        return "SuspenseList";
    case 25:
        return "TracingMarker";
    case 1:
    case 0:
    case 17:
    case 2:
    case 14:
    case 15:
        if (typeof t == "function")
            return t.displayName || t.name || null;
        if (typeof t == "string")
            return t
    }
    return null
}
function yr(e) {
    switch (typeof e) {
    case "boolean":
    case "number":
    case "string":
    case "undefined":
        return e;
    case "object":
        return e;
    default:
        return ""
    }
}
function Yp(e) {
    var t = e.type;
    return (e = e.nodeName) && e.toLowerCase() === "input" && (t === "checkbox" || t === "radio")
}
function x1(e) {
    var t = Yp(e) ? "checked" : "value"
      , n = Object.getOwnPropertyDescriptor(e.constructor.prototype, t)
      , r = "" + e[t];
    if (!e.hasOwnProperty(t) && typeof n < "u" && typeof n.get == "function" && typeof n.set == "function") {
        var o = n.get
          , s = n.set;
        return Object.defineProperty(e, t, {
            configurable: !0,
            get: function() {
                return o.call(this)
            },
            set: function(i) {
                r = "" + i,
                s.call(this, i)
            }
        }),
        Object.defineProperty(e, t, {
            enumerable: n.enumerable
        }),
        {
            getValue: function() {
                return r
            },
            setValue: function(i) {
                r = "" + i
            },
            stopTracking: function() {
                e._valueTracker = null,
                delete e[t]
            }
        }
    }
}
function Ha(e) {
    e._valueTracker || (e._valueTracker = x1(e))
}
function Kp(e) {
    if (!e)
        return !1;
    var t = e._valueTracker;
    if (!t)
        return !0;
    var n = t.getValue()
      , r = "";
    return e && (r = Yp(e) ? e.checked ? "true" : "false" : e.value),
    e = r,
    e !== n ? (t.setValue(e),
    !0) : !1
}
function _i(e) {
    if (e = e || (typeof document < "u" ? document : void 0),
    typeof e > "u")
        return null;
    try {
        return e.activeElement || e.body
    } catch {
        return e.body
    }
}
function Zc(e, t) {
    var n = t.checked;
    return Te({}, t, {
        defaultChecked: void 0,
        defaultValue: void 0,
        value: void 0,
        checked: n ?? e._wrapperState.initialChecked
    })
}
function fm(e, t) {
    var n = t.defaultValue == null ? "" : t.defaultValue
      , r = t.checked != null ? t.checked : t.defaultChecked;
    n = yr(t.value != null ? t.value : n),
    e._wrapperState = {
        initialChecked: r,
        initialValue: n,
        controlled: t.type === "checkbox" || t.type === "radio" ? t.checked != null : t.value != null
    }
}
function Qp(e, t) {
    t = t.checked,
    t != null && jd(e, "checked", t, !1)
}
function eu(e, t) {
    Qp(e, t);
    var n = yr(t.value)
      , r = t.type;
    if (n != null)
        r === "number" ? (n === 0 && e.value === "" || e.value != n) && (e.value = "" + n) : e.value !== "" + n && (e.value = "" + n);
    else if (r === "submit" || r === "reset") {
        e.removeAttribute("value");
        return
    }
    t.hasOwnProperty("value") ? tu(e, t.type, n) : t.hasOwnProperty("defaultValue") && tu(e, t.type, yr(t.defaultValue)),
    t.checked == null && t.defaultChecked != null && (e.defaultChecked = !!t.defaultChecked)
}
function mm(e, t, n) {
    if (t.hasOwnProperty("value") || t.hasOwnProperty("defaultValue")) {
        var r = t.type;
        if (!(r !== "submit" && r !== "reset" || t.value !== void 0 && t.value !== null))
            return;
        t = "" + e._wrapperState.initialValue,
        n || t === e.value || (e.value = t),
        e.defaultValue = t
    }
    n = e.name,
    n !== "" && (e.name = ""),
    e.defaultChecked = !!e._wrapperState.initialChecked,
    n !== "" && (e.name = n)
}
function tu(e, t, n) {
    (t !== "number" || _i(e.ownerDocument) !== e) && (n == null ? e.defaultValue = "" + e._wrapperState.initialValue : e.defaultValue !== "" + n && (e.defaultValue = "" + n))
}
var Is = Array.isArray;
function _o(e, t, n, r) {
    if (e = e.options,
    t) {
        t = {};
        for (var o = 0; o < n.length; o++)
            t["$" + n[o]] = !0;
        for (n = 0; n < e.length; n++)
            o = t.hasOwnProperty("$" + e[n].value),
            e[n].selected !== o && (e[n].selected = o),
            o && r && (e[n].defaultSelected = !0)
    } else {
        for (n = "" + yr(n),
        t = null,
        o = 0; o < e.length; o++) {
            if (e[o].value === n) {
                e[o].selected = !0,
                r && (e[o].defaultSelected = !0);
                return
            }
            t !== null || e[o].disabled || (t = e[o])
        }
        t !== null && (t.selected = !0)
    }
}
function nu(e, t) {
    if (t.dangerouslySetInnerHTML != null)
        throw Error(_(91));
    return Te({}, t, {
        value: void 0,
        defaultValue: void 0,
        children: "" + e._wrapperState.initialValue
    })
}
function hm(e, t) {
    var n = t.value;
    if (n == null) {
        if (n = t.children,
        t = t.defaultValue,
        n != null) {
            if (t != null)
                throw Error(_(92));
            if (Is(n)) {
                if (1 < n.length)
                    throw Error(_(93));
                n = n[0]
            }
            t = n
        }
        t == null && (t = ""),
        n = t
    }
    e._wrapperState = {
        initialValue: yr(n)
    }
}
function Gp(e, t) {
    var n = yr(t.value)
      , r = yr(t.defaultValue);
    n != null && (n = "" + n,
    n !== e.value && (e.value = n),
    t.defaultValue == null && e.defaultValue !== n && (e.defaultValue = n)),
    r != null && (e.defaultValue = "" + r)
}
function pm(e) {
    var t = e.textContent;
    t === e._wrapperState.initialValue && t !== "" && t !== null && (e.value = t)
}
function qp(e) {
    switch (e) {
    case "svg":
        return "http://www.w3.org/2000/svg";
    case "math":
        return "http://www.w3.org/1998/Math/MathML";
    default:
        return "http://www.w3.org/1999/xhtml"
    }
}
function ru(e, t) {
    return e == null || e === "http://www.w3.org/1999/xhtml" ? qp(t) : e === "http://www.w3.org/2000/svg" && t === "foreignObject" ? "http://www.w3.org/1999/xhtml" : e
}
var Va, Xp = function(e) {
    return typeof MSApp < "u" && MSApp.execUnsafeLocalFunction ? function(t, n, r, o) {
        MSApp.execUnsafeLocalFunction(function() {
            return e(t, n, r, o)
        })
    }
    : e
}(function(e, t) {
    if (e.namespaceURI !== "http://www.w3.org/2000/svg" || "innerHTML"in e)
        e.innerHTML = t;
    else {
        for (Va = Va || document.createElement("div"),
        Va.innerHTML = "<svg>" + t.valueOf().toString() + "</svg>",
        t = Va.firstChild; e.firstChild; )
            e.removeChild(e.firstChild);
        for (; t.firstChild; )
            e.appendChild(t.firstChild)
    }
});
function Xs(e, t) {
    if (t) {
        var n = e.firstChild;
        if (n && n === e.lastChild && n.nodeType === 3) {
            n.nodeValue = t;
            return
        }
    }
    e.textContent = t
}
var $s = {
    animationIterationCount: !0,
    aspectRatio: !0,
    borderImageOutset: !0,
    borderImageSlice: !0,
    borderImageWidth: !0,
    boxFlex: !0,
    boxFlexGroup: !0,
    boxOrdinalGroup: !0,
    columnCount: !0,
    columns: !0,
    flex: !0,
    flexGrow: !0,
    flexPositive: !0,
    flexShrink: !0,
    flexNegative: !0,
    flexOrder: !0,
    gridArea: !0,
    gridRow: !0,
    gridRowEnd: !0,
    gridRowSpan: !0,
    gridRowStart: !0,
    gridColumn: !0,
    gridColumnEnd: !0,
    gridColumnSpan: !0,
    gridColumnStart: !0,
    fontWeight: !0,
    lineClamp: !0,
    lineHeight: !0,
    opacity: !0,
    order: !0,
    orphans: !0,
    tabSize: !0,
    widows: !0,
    zIndex: !0,
    zoom: !0,
    fillOpacity: !0,
    floodOpacity: !0,
    stopOpacity: !0,
    strokeDasharray: !0,
    strokeDashoffset: !0,
    strokeMiterlimit: !0,
    strokeOpacity: !0,
    strokeWidth: !0
}
  , w1 = ["Webkit", "ms", "Moz", "O"];
Object.keys($s).forEach(function(e) {
    w1.forEach(function(t) {
        t = t + e.charAt(0).toUpperCase() + e.substring(1),
        $s[t] = $s[e]
    })
});
function Jp(e, t, n) {
    return t == null || typeof t == "boolean" || t === "" ? "" : n || typeof t != "number" || t === 0 || $s.hasOwnProperty(e) && $s[e] ? ("" + t).trim() : t + "px"
}
function Zp(e, t) {
    e = e.style;
    for (var n in t)
        if (t.hasOwnProperty(n)) {
            var r = n.indexOf("--") === 0
              , o = Jp(n, t[n], r);
            n === "float" && (n = "cssFloat"),
            r ? e.setProperty(n, o) : e[n] = o
        }
}
var b1 = Te({
    menuitem: !0
}, {
    area: !0,
    base: !0,
    br: !0,
    col: !0,
    embed: !0,
    hr: !0,
    img: !0,
    input: !0,
    keygen: !0,
    link: !0,
    meta: !0,
    param: !0,
    source: !0,
    track: !0,
    wbr: !0
});
function ou(e, t) {
    if (t) {
        if (b1[e] && (t.children != null || t.dangerouslySetInnerHTML != null))
            throw Error(_(137, e));
        if (t.dangerouslySetInnerHTML != null) {
            if (t.children != null)
                throw Error(_(60));
            if (typeof t.dangerouslySetInnerHTML != "object" || !("__html"in t.dangerouslySetInnerHTML))
                throw Error(_(61))
        }
        if (t.style != null && typeof t.style != "object")
            throw Error(_(62))
    }
}
function su(e, t) {
    if (e.indexOf("-") === -1)
        return typeof t.is == "string";
    switch (e) {
    case "annotation-xml":
    case "color-profile":
    case "font-face":
    case "font-face-src":
    case "font-face-uri":
    case "font-face-format":
    case "font-face-name":
    case "missing-glyph":
        return !1;
    default:
        return !0
    }
}
var au = null;
function Pd(e) {
    return e = e.target || e.srcElement || window,
    e.correspondingUseElement && (e = e.correspondingUseElement),
    e.nodeType === 3 ? e.parentNode : e
}
var iu = null
  , Do = null
  , Oo = null;
function vm(e) {
    if (e = Ea(e)) {
        if (typeof iu != "function")
            throw Error(_(280));
        var t = e.stateNode;
        t && (t = wl(t),
        iu(e.stateNode, e.type, t))
    }
}
function ev(e) {
    Do ? Oo ? Oo.push(e) : Oo = [e] : Do = e
}
function tv() {
    if (Do) {
        var e = Do
          , t = Oo;
        if (Oo = Do = null,
        vm(e),
        t)
            for (e = 0; e < t.length; e++)
                vm(t[e])
    }
}
function nv(e, t) {
    return e(t)
}
function rv() {}
var oc = !1;
function ov(e, t, n) {
    if (oc)
        return e(t, n);
    oc = !0;
    try {
        return nv(e, t, n)
    } finally {
        oc = !1,
        (Do !== null || Oo !== null) && (rv(),
        tv())
    }
}
function Js(e, t) {
    var n = e.stateNode;
    if (n === null)
        return null;
    var r = wl(n);
    if (r === null)
        return null;
    n = r[t];
    e: switch (t) {
    case "onClick":
    case "onClickCapture":
    case "onDoubleClick":
    case "onDoubleClickCapture":
    case "onMouseDown":
    case "onMouseDownCapture":
    case "onMouseMove":
    case "onMouseMoveCapture":
    case "onMouseUp":
    case "onMouseUpCapture":
    case "onMouseEnter":
        (r = !r.disabled) || (e = e.type,
        r = !(e === "button" || e === "input" || e === "select" || e === "textarea")),
        e = !r;
        break e;
    default:
        e = !1
    }
    if (e)
        return null;
    if (n && typeof n != "function")
        throw Error(_(231, t, typeof n));
    return n
}
var lu = !1;
if (Dn)
    try {
        var js = {};
        Object.defineProperty(js, "passive", {
            get: function() {
                lu = !0
            }
        }),
        window.addEventListener("test", js, js),
        window.removeEventListener("test", js, js)
    } catch {
        lu = !1
    }
function N1(e, t, n, r, o, s, i, l, c) {
    var u = Array.prototype.slice.call(arguments, 3);
    try {
        t.apply(n, u)
    } catch (d) {
        this.onError(d)
    }
}
var Bs = !1
  , Di = null
  , Oi = !1
  , cu = null
  , S1 = {
    onError: function(e) {
        Bs = !0,
        Di = e
    }
};
function j1(e, t, n, r, o, s, i, l, c) {
    Bs = !1,
    Di = null,
    N1.apply(S1, arguments)
}
function C1(e, t, n, r, o, s, i, l, c) {
    if (j1.apply(this, arguments),
    Bs) {
        if (Bs) {
            var u = Di;
            Bs = !1,
            Di = null
        } else
            throw Error(_(198));
        Oi || (Oi = !0,
        cu = u)
    }
}
function so(e) {
    var t = e
      , n = e;
    if (e.alternate)
        for (; t.return; )
            t = t.return;
    else {
        e = t;
        do
            t = e,
            t.flags & 4098 && (n = t.return),
            e = t.return;
        while (e)
    }
    return t.tag === 3 ? n : null
}
function sv(e) {
    if (e.tag === 13) {
        var t = e.memoizedState;
        if (t === null && (e = e.alternate,
        e !== null && (t = e.memoizedState)),
        t !== null)
            return t.dehydrated
    }
    return null
}
function gm(e) {
    if (so(e) !== e)
        throw Error(_(188))
}
function k1(e) {
    var t = e.alternate;
    if (!t) {
        if (t = so(e),
        t === null)
            throw Error(_(188));
        return t !== e ? null : e
    }
    for (var n = e, r = t; ; ) {
        var o = n.return;
        if (o === null)
            break;
        var s = o.alternate;
        if (s === null) {
            if (r = o.return,
            r !== null) {
                n = r;
                continue
            }
            break
        }
        if (o.child === s.child) {
            for (s = o.child; s; ) {
                if (s === n)
                    return gm(o),
                    e;
                if (s === r)
                    return gm(o),
                    t;
                s = s.sibling
            }
            throw Error(_(188))
        }
        if (n.return !== r.return)
            n = o,
            r = s;
        else {
            for (var i = !1, l = o.child; l; ) {
                if (l === n) {
                    i = !0,
                    n = o,
                    r = s;
                    break
                }
                if (l === r) {
                    i = !0,
                    r = o,
                    n = s;
                    break
                }
                l = l.sibling
            }
            if (!i) {
                for (l = s.child; l; ) {
                    if (l === n) {
                        i = !0,
                        n = s,
                        r = o;
                        break
                    }
                    if (l === r) {
                        i = !0,
                        r = s,
                        n = o;
                        break
                    }
                    l = l.sibling
                }
                if (!i)
                    throw Error(_(189))
            }
        }
        if (n.alternate !== r)
            throw Error(_(190))
    }
    if (n.tag !== 3)
        throw Error(_(188));
    return n.stateNode.current === n ? e : t
}
function av(e) {
    return e = k1(e),
    e !== null ? iv(e) : null
}
function iv(e) {
    if (e.tag === 5 || e.tag === 6)
        return e;
    for (e = e.child; e !== null; ) {
        var t = iv(e);
        if (t !== null)
            return t;
        e = e.sibling
    }
    return null
}
var lv = wt.unstable_scheduleCallback
  , ym = wt.unstable_cancelCallback
  , E1 = wt.unstable_shouldYield
  , P1 = wt.unstable_requestPaint
  , Oe = wt.unstable_now
  , T1 = wt.unstable_getCurrentPriorityLevel
  , Td = wt.unstable_ImmediatePriority
  , cv = wt.unstable_UserBlockingPriority
  , Ai = wt.unstable_NormalPriority
  , M1 = wt.unstable_LowPriority
  , uv = wt.unstable_IdlePriority
  , vl = null
  , pn = null;
function R1(e) {
    if (pn && typeof pn.onCommitFiberRoot == "function")
        try {
            pn.onCommitFiberRoot(vl, e, void 0, (e.current.flags & 128) === 128)
        } catch {}
}
var Gt = Math.clz32 ? Math.clz32 : O1
  , _1 = Math.log
  , D1 = Math.LN2;
function O1(e) {
    return e >>>= 0,
    e === 0 ? 32 : 31 - (_1(e) / D1 | 0) | 0
}
var Ua = 64
  , Ya = 4194304;
function Ls(e) {
    switch (e & -e) {
    case 1:
        return 1;
    case 2:
        return 2;
    case 4:
        return 4;
    case 8:
        return 8;
    case 16:
        return 16;
    case 32:
        return 32;
    case 64:
    case 128:
    case 256:
    case 512:
    case 1024:
    case 2048:
    case 4096:
    case 8192:
    case 16384:
    case 32768:
    case 65536:
    case 131072:
    case 262144:
    case 524288:
    case 1048576:
    case 2097152:
        return e & 4194240;
    case 4194304:
    case 8388608:
    case 16777216:
    case 33554432:
    case 67108864:
        return e & 130023424;
    case 134217728:
        return 134217728;
    case 268435456:
        return 268435456;
    case 536870912:
        return 536870912;
    case 1073741824:
        return 1073741824;
    default:
        return e
    }
}
function Ii(e, t) {
    var n = e.pendingLanes;
    if (n === 0)
        return 0;
    var r = 0
      , o = e.suspendedLanes
      , s = e.pingedLanes
      , i = n & 268435455;
    if (i !== 0) {
        var l = i & ~o;
        l !== 0 ? r = Ls(l) : (s &= i,
        s !== 0 && (r = Ls(s)))
    } else
        i = n & ~o,
        i !== 0 ? r = Ls(i) : s !== 0 && (r = Ls(s));
    if (r === 0)
        return 0;
    if (t !== 0 && t !== r && !(t & o) && (o = r & -r,
    s = t & -t,
    o >= s || o === 16 && (s & 4194240) !== 0))
        return t;
    if (r & 4 && (r |= n & 16),
    t = e.entangledLanes,
    t !== 0)
        for (e = e.entanglements,
        t &= r; 0 < t; )
            n = 31 - Gt(t),
            o = 1 << n,
            r |= e[n],
            t &= ~o;
    return r
}
function A1(e, t) {
    switch (e) {
    case 1:
    case 2:
    case 4:
        return t + 250;
    case 8:
    case 16:
    case 32:
    case 64:
    case 128:
    case 256:
    case 512:
    case 1024:
    case 2048:
    case 4096:
    case 8192:
    case 16384:
    case 32768:
    case 65536:
    case 131072:
    case 262144:
    case 524288:
    case 1048576:
    case 2097152:
        return t + 5e3;
    case 4194304:
    case 8388608:
    case 16777216:
    case 33554432:
    case 67108864:
        return -1;
    case 134217728:
    case 268435456:
    case 536870912:
    case 1073741824:
        return -1;
    default:
        return -1
    }
}
function I1(e, t) {
    for (var n = e.suspendedLanes, r = e.pingedLanes, o = e.expirationTimes, s = e.pendingLanes; 0 < s; ) {
        var i = 31 - Gt(s)
          , l = 1 << i
          , c = o[i];
        c === -1 ? (!(l & n) || l & r) && (o[i] = A1(l, t)) : c <= t && (e.expiredLanes |= l),
        s &= ~l
    }
}
function uu(e) {
    return e = e.pendingLanes & -1073741825,
    e !== 0 ? e : e & 1073741824 ? 1073741824 : 0
}
function dv() {
    var e = Ua;
    return Ua <<= 1,
    !(Ua & 4194240) && (Ua = 64),
    e
}
function sc(e) {
    for (var t = [], n = 0; 31 > n; n++)
        t.push(e);
    return t
}
function Ca(e, t, n) {
    e.pendingLanes |= t,
    t !== 536870912 && (e.suspendedLanes = 0,
    e.pingedLanes = 0),
    e = e.eventTimes,
    t = 31 - Gt(t),
    e[t] = n
}
function L1(e, t) {
    var n = e.pendingLanes & ~t;
    e.pendingLanes = t,
    e.suspendedLanes = 0,
    e.pingedLanes = 0,
    e.expiredLanes &= t,
    e.mutableReadLanes &= t,
    e.entangledLanes &= t,
    t = e.entanglements;
    var r = e.eventTimes;
    for (e = e.expirationTimes; 0 < n; ) {
        var o = 31 - Gt(n)
          , s = 1 << o;
        t[o] = 0,
        r[o] = -1,
        e[o] = -1,
        n &= ~s
    }
}
function Md(e, t) {
    var n = e.entangledLanes |= t;
    for (e = e.entanglements; n; ) {
        var r = 31 - Gt(n)
          , o = 1 << r;
        o & t | e[r] & t && (e[r] |= t),
        n &= ~o
    }
}
var pe = 0;
function fv(e) {
    return e &= -e,
    1 < e ? 4 < e ? e & 268435455 ? 16 : 536870912 : 4 : 1
}
var mv, Rd, hv, pv, vv, du = !1, Ka = [], cr = null, ur = null, dr = null, Zs = new Map, ea = new Map, Jn = [], F1 = "mousedown mouseup touchcancel touchend touchstart auxclick dblclick pointercancel pointerdown pointerup dragend dragstart drop compositionend compositionstart keydown keypress keyup input textInput copy cut paste click change contextmenu reset submit".split(" ");
function xm(e, t) {
    switch (e) {
    case "focusin":
    case "focusout":
        cr = null;
        break;
    case "dragenter":
    case "dragleave":
        ur = null;
        break;
    case "mouseover":
    case "mouseout":
        dr = null;
        break;
    case "pointerover":
    case "pointerout":
        Zs.delete(t.pointerId);
        break;
    case "gotpointercapture":
    case "lostpointercapture":
        ea.delete(t.pointerId)
    }
}
function Cs(e, t, n, r, o, s) {
    return e === null || e.nativeEvent !== s ? (e = {
        blockedOn: t,
        domEventName: n,
        eventSystemFlags: r,
        nativeEvent: s,
        targetContainers: [o]
    },
    t !== null && (t = Ea(t),
    t !== null && Rd(t)),
    e) : (e.eventSystemFlags |= r,
    t = e.targetContainers,
    o !== null && t.indexOf(o) === -1 && t.push(o),
    e)
}
function z1(e, t, n, r, o) {
    switch (t) {
    case "focusin":
        return cr = Cs(cr, e, t, n, r, o),
        !0;
    case "dragenter":
        return ur = Cs(ur, e, t, n, r, o),
        !0;
    case "mouseover":
        return dr = Cs(dr, e, t, n, r, o),
        !0;
    case "pointerover":
        var s = o.pointerId;
        return Zs.set(s, Cs(Zs.get(s) || null, e, t, n, r, o)),
        !0;
    case "gotpointercapture":
        return s = o.pointerId,
        ea.set(s, Cs(ea.get(s) || null, e, t, n, r, o)),
        !0
    }
    return !1
}
function gv(e) {
    var t = Ir(e.target);
    if (t !== null) {
        var n = so(t);
        if (n !== null) {
            if (t = n.tag,
            t === 13) {
                if (t = sv(n),
                t !== null) {
                    e.blockedOn = t,
                    vv(e.priority, function() {
                        hv(n)
                    });
                    return
                }
            } else if (t === 3 && n.stateNode.current.memoizedState.isDehydrated) {
                e.blockedOn = n.tag === 3 ? n.stateNode.containerInfo : null;
                return
            }
        }
    }
    e.blockedOn = null
}
function pi(e) {
    if (e.blockedOn !== null)
        return !1;
    for (var t = e.targetContainers; 0 < t.length; ) {
        var n = fu(e.domEventName, e.eventSystemFlags, t[0], e.nativeEvent);
        if (n === null) {
            n = e.nativeEvent;
            var r = new n.constructor(n.type,n);
            au = r,
            n.target.dispatchEvent(r),
            au = null
        } else
            return t = Ea(n),
            t !== null && Rd(t),
            e.blockedOn = n,
            !1;
        t.shift()
    }
    return !0
}
function wm(e, t, n) {
    pi(e) && n.delete(t)
}
function $1() {
    du = !1,
    cr !== null && pi(cr) && (cr = null),
    ur !== null && pi(ur) && (ur = null),
    dr !== null && pi(dr) && (dr = null),
    Zs.forEach(wm),
    ea.forEach(wm)
}
function ks(e, t) {
    e.blockedOn === t && (e.blockedOn = null,
    du || (du = !0,
    wt.unstable_scheduleCallback(wt.unstable_NormalPriority, $1)))
}
function ta(e) {
    function t(o) {
        return ks(o, e)
    }
    if (0 < Ka.length) {
        ks(Ka[0], e);
        for (var n = 1; n < Ka.length; n++) {
            var r = Ka[n];
            r.blockedOn === e && (r.blockedOn = null)
        }
    }
    for (cr !== null && ks(cr, e),
    ur !== null && ks(ur, e),
    dr !== null && ks(dr, e),
    Zs.forEach(t),
    ea.forEach(t),
    n = 0; n < Jn.length; n++)
        r = Jn[n],
        r.blockedOn === e && (r.blockedOn = null);
    for (; 0 < Jn.length && (n = Jn[0],
    n.blockedOn === null); )
        gv(n),
        n.blockedOn === null && Jn.shift()
}
var Ao = zn.ReactCurrentBatchConfig
  , Li = !0;
function B1(e, t, n, r) {
    var o = pe
      , s = Ao.transition;
    Ao.transition = null;
    try {
        pe = 1,
        _d(e, t, n, r)
    } finally {
        pe = o,
        Ao.transition = s
    }
}
function W1(e, t, n, r) {
    var o = pe
      , s = Ao.transition;
    Ao.transition = null;
    try {
        pe = 4,
        _d(e, t, n, r)
    } finally {
        pe = o,
        Ao.transition = s
    }
}
function _d(e, t, n, r) {
    if (Li) {
        var o = fu(e, t, n, r);
        if (o === null)
            pc(e, t, r, Fi, n),
            xm(e, r);
        else if (z1(o, e, t, n, r))
            r.stopPropagation();
        else if (xm(e, r),
        t & 4 && -1 < F1.indexOf(e)) {
            for (; o !== null; ) {
                var s = Ea(o);
                if (s !== null && mv(s),
                s = fu(e, t, n, r),
                s === null && pc(e, t, r, Fi, n),
                s === o)
                    break;
                o = s
            }
            o !== null && r.stopPropagation()
        } else
            pc(e, t, r, null, n)
    }
}
var Fi = null;
function fu(e, t, n, r) {
    if (Fi = null,
    e = Pd(r),
    e = Ir(e),
    e !== null)
        if (t = so(e),
        t === null)
            e = null;
        else if (n = t.tag,
        n === 13) {
            if (e = sv(t),
            e !== null)
                return e;
            e = null
        } else if (n === 3) {
            if (t.stateNode.current.memoizedState.isDehydrated)
                return t.tag === 3 ? t.stateNode.containerInfo : null;
            e = null
        } else
            t !== e && (e = null);
    return Fi = e,
    null
}
function yv(e) {
    switch (e) {
    case "cancel":
    case "click":
    case "close":
    case "contextmenu":
    case "copy":
    case "cut":
    case "auxclick":
    case "dblclick":
    case "dragend":
    case "dragstart":
    case "drop":
    case "focusin":
    case "focusout":
    case "input":
    case "invalid":
    case "keydown":
    case "keypress":
    case "keyup":
    case "mousedown":
    case "mouseup":
    case "paste":
    case "pause":
    case "play":
    case "pointercancel":
    case "pointerdown":
    case "pointerup":
    case "ratechange":
    case "reset":
    case "resize":
    case "seeked":
    case "submit":
    case "touchcancel":
    case "touchend":
    case "touchstart":
    case "volumechange":
    case "change":
    case "selectionchange":
    case "textInput":
    case "compositionstart":
    case "compositionend":
    case "compositionupdate":
    case "beforeblur":
    case "afterblur":
    case "beforeinput":
    case "blur":
    case "fullscreenchange":
    case "focus":
    case "hashchange":
    case "popstate":
    case "select":
    case "selectstart":
        return 1;
    case "drag":
    case "dragenter":
    case "dragexit":
    case "dragleave":
    case "dragover":
    case "mousemove":
    case "mouseout":
    case "mouseover":
    case "pointermove":
    case "pointerout":
    case "pointerover":
    case "scroll":
    case "toggle":
    case "touchmove":
    case "wheel":
    case "mouseenter":
    case "mouseleave":
    case "pointerenter":
    case "pointerleave":
        return 4;
    case "message":
        switch (T1()) {
        case Td:
            return 1;
        case cv:
            return 4;
        case Ai:
        case M1:
            return 16;
        case uv:
            return 536870912;
        default:
            return 16
        }
    default:
        return 16
    }
}
var sr = null
  , Dd = null
  , vi = null;
function xv() {
    if (vi)
        return vi;
    var e, t = Dd, n = t.length, r, o = "value"in sr ? sr.value : sr.textContent, s = o.length;
    for (e = 0; e < n && t[e] === o[e]; e++)
        ;
    var i = n - e;
    for (r = 1; r <= i && t[n - r] === o[s - r]; r++)
        ;
    return vi = o.slice(e, 1 < r ? 1 - r : void 0)
}
function gi(e) {
    var t = e.keyCode;
    return "charCode"in e ? (e = e.charCode,
    e === 0 && t === 13 && (e = 13)) : e = t,
    e === 10 && (e = 13),
    32 <= e || e === 13 ? e : 0
}
function Qa() {
    return !0
}
function bm() {
    return !1
}
function St(e) {
    function t(n, r, o, s, i) {
        this._reactName = n,
        this._targetInst = o,
        this.type = r,
        this.nativeEvent = s,
        this.target = i,
        this.currentTarget = null;
        for (var l in e)
            e.hasOwnProperty(l) && (n = e[l],
            this[l] = n ? n(s) : s[l]);
        return this.isDefaultPrevented = (s.defaultPrevented != null ? s.defaultPrevented : s.returnValue === !1) ? Qa : bm,
        this.isPropagationStopped = bm,
        this
    }
    return Te(t.prototype, {
        preventDefault: function() {
            this.defaultPrevented = !0;
            var n = this.nativeEvent;
            n && (n.preventDefault ? n.preventDefault() : typeof n.returnValue != "unknown" && (n.returnValue = !1),
            this.isDefaultPrevented = Qa)
        },
        stopPropagation: function() {
            var n = this.nativeEvent;
            n && (n.stopPropagation ? n.stopPropagation() : typeof n.cancelBubble != "unknown" && (n.cancelBubble = !0),
            this.isPropagationStopped = Qa)
        },
        persist: function() {},
        isPersistent: Qa
    }),
    t
}
var ds = {
    eventPhase: 0,
    bubbles: 0,
    cancelable: 0,
    timeStamp: function(e) {
        return e.timeStamp || Date.now()
    },
    defaultPrevented: 0,
    isTrusted: 0
}, Od = St(ds), ka = Te({}, ds, {
    view: 0,
    detail: 0
}), H1 = St(ka), ac, ic, Es, gl = Te({}, ka, {
    screenX: 0,
    screenY: 0,
    clientX: 0,
    clientY: 0,
    pageX: 0,
    pageY: 0,
    ctrlKey: 0,
    shiftKey: 0,
    altKey: 0,
    metaKey: 0,
    getModifierState: Ad,
    button: 0,
    buttons: 0,
    relatedTarget: function(e) {
        return e.relatedTarget === void 0 ? e.fromElement === e.srcElement ? e.toElement : e.fromElement : e.relatedTarget
    },
    movementX: function(e) {
        return "movementX"in e ? e.movementX : (e !== Es && (Es && e.type === "mousemove" ? (ac = e.screenX - Es.screenX,
        ic = e.screenY - Es.screenY) : ic = ac = 0,
        Es = e),
        ac)
    },
    movementY: function(e) {
        return "movementY"in e ? e.movementY : ic
    }
}), Nm = St(gl), V1 = Te({}, gl, {
    dataTransfer: 0
}), U1 = St(V1), Y1 = Te({}, ka, {
    relatedTarget: 0
}), lc = St(Y1), K1 = Te({}, ds, {
    animationName: 0,
    elapsedTime: 0,
    pseudoElement: 0
}), Q1 = St(K1), G1 = Te({}, ds, {
    clipboardData: function(e) {
        return "clipboardData"in e ? e.clipboardData : window.clipboardData
    }
}), q1 = St(G1), X1 = Te({}, ds, {
    data: 0
}), Sm = St(X1), J1 = {
    Esc: "Escape",
    Spacebar: " ",
    Left: "ArrowLeft",
    Up: "ArrowUp",
    Right: "ArrowRight",
    Down: "ArrowDown",
    Del: "Delete",
    Win: "OS",
    Menu: "ContextMenu",
    Apps: "ContextMenu",
    Scroll: "ScrollLock",
    MozPrintableKey: "Unidentified"
}, Z1 = {
    8: "Backspace",
    9: "Tab",
    12: "Clear",
    13: "Enter",
    16: "Shift",
    17: "Control",
    18: "Alt",
    19: "Pause",
    20: "CapsLock",
    27: "Escape",
    32: " ",
    33: "PageUp",
    34: "PageDown",
    35: "End",
    36: "Home",
    37: "ArrowLeft",
    38: "ArrowUp",
    39: "ArrowRight",
    40: "ArrowDown",
    45: "Insert",
    46: "Delete",
    112: "F1",
    113: "F2",
    114: "F3",
    115: "F4",
    116: "F5",
    117: "F6",
    118: "F7",
    119: "F8",
    120: "F9",
    121: "F10",
    122: "F11",
    123: "F12",
    144: "NumLock",
    145: "ScrollLock",
    224: "Meta"
}, eb = {
    Alt: "altKey",
    Control: "ctrlKey",
    Meta: "metaKey",
    Shift: "shiftKey"
};
function tb(e) {
    var t = this.nativeEvent;
    return t.getModifierState ? t.getModifierState(e) : (e = eb[e]) ? !!t[e] : !1
}
function Ad() {
    return tb
}
var nb = Te({}, ka, {
    key: function(e) {
        if (e.key) {
            var t = J1[e.key] || e.key;
            if (t !== "Unidentified")
                return t
        }
        return e.type === "keypress" ? (e = gi(e),
        e === 13 ? "Enter" : String.fromCharCode(e)) : e.type === "keydown" || e.type === "keyup" ? Z1[e.keyCode] || "Unidentified" : ""
    },
    code: 0,
    location: 0,
    ctrlKey: 0,
    shiftKey: 0,
    altKey: 0,
    metaKey: 0,
    repeat: 0,
    locale: 0,
    getModifierState: Ad,
    charCode: function(e) {
        return e.type === "keypress" ? gi(e) : 0
    },
    keyCode: function(e) {
        return e.type === "keydown" || e.type === "keyup" ? e.keyCode : 0
    },
    which: function(e) {
        return e.type === "keypress" ? gi(e) : e.type === "keydown" || e.type === "keyup" ? e.keyCode : 0
    }
})
  , rb = St(nb)
  , ob = Te({}, gl, {
    pointerId: 0,
    width: 0,
    height: 0,
    pressure: 0,
    tangentialPressure: 0,
    tiltX: 0,
    tiltY: 0,
    twist: 0,
    pointerType: 0,
    isPrimary: 0
})
  , jm = St(ob)
  , sb = Te({}, ka, {
    touches: 0,
    targetTouches: 0,
    changedTouches: 0,
    altKey: 0,
    metaKey: 0,
    ctrlKey: 0,
    shiftKey: 0,
    getModifierState: Ad
})
  , ab = St(sb)
  , ib = Te({}, ds, {
    propertyName: 0,
    elapsedTime: 0,
    pseudoElement: 0
})
  , lb = St(ib)
  , cb = Te({}, gl, {
    deltaX: function(e) {
        return "deltaX"in e ? e.deltaX : "wheelDeltaX"in e ? -e.wheelDeltaX : 0
    },
    deltaY: function(e) {
        return "deltaY"in e ? e.deltaY : "wheelDeltaY"in e ? -e.wheelDeltaY : "wheelDelta"in e ? -e.wheelDelta : 0
    },
    deltaZ: 0,
    deltaMode: 0
})
  , ub = St(cb)
  , db = [9, 13, 27, 32]
  , Id = Dn && "CompositionEvent"in window
  , Ws = null;
Dn && "documentMode"in document && (Ws = document.documentMode);
var fb = Dn && "TextEvent"in window && !Ws
  , wv = Dn && (!Id || Ws && 8 < Ws && 11 >= Ws)
  , Cm = " "
  , km = !1;
function bv(e, t) {
    switch (e) {
    case "keyup":
        return db.indexOf(t.keyCode) !== -1;
    case "keydown":
        return t.keyCode !== 229;
    case "keypress":
    case "mousedown":
    case "focusout":
        return !0;
    default:
        return !1
    }
}
function Nv(e) {
    return e = e.detail,
    typeof e == "object" && "data"in e ? e.data : null
}
var No = !1;
function mb(e, t) {
    switch (e) {
    case "compositionend":
        return Nv(t);
    case "keypress":
        return t.which !== 32 ? null : (km = !0,
        Cm);
    case "textInput":
        return e = t.data,
        e === Cm && km ? null : e;
    default:
        return null
    }
}
function hb(e, t) {
    if (No)
        return e === "compositionend" || !Id && bv(e, t) ? (e = xv(),
        vi = Dd = sr = null,
        No = !1,
        e) : null;
    switch (e) {
    case "paste":
        return null;
    case "keypress":
        if (!(t.ctrlKey || t.altKey || t.metaKey) || t.ctrlKey && t.altKey) {
            if (t.char && 1 < t.char.length)
                return t.char;
            if (t.which)
                return String.fromCharCode(t.which)
        }
        return null;
    case "compositionend":
        return wv && t.locale !== "ko" ? null : t.data;
    default:
        return null
    }
}
var pb = {
    color: !0,
    date: !0,
    datetime: !0,
    "datetime-local": !0,
    email: !0,
    month: !0,
    number: !0,
    password: !0,
    range: !0,
    search: !0,
    tel: !0,
    text: !0,
    time: !0,
    url: !0,
    week: !0
};
function Em(e) {
    var t = e && e.nodeName && e.nodeName.toLowerCase();
    return t === "input" ? !!pb[e.type] : t === "textarea"
}
function Sv(e, t, n, r) {
    ev(r),
    t = zi(t, "onChange"),
    0 < t.length && (n = new Od("onChange","change",null,n,r),
    e.push({
        event: n,
        listeners: t
    }))
}
var Hs = null
  , na = null;
function vb(e) {
    Ov(e, 0)
}
function yl(e) {
    var t = Co(e);
    if (Kp(t))
        return e
}
function gb(e, t) {
    if (e === "change")
        return t
}
var jv = !1;
if (Dn) {
    var cc;
    if (Dn) {
        var uc = "oninput"in document;
        if (!uc) {
            var Pm = document.createElement("div");
            Pm.setAttribute("oninput", "return;"),
            uc = typeof Pm.oninput == "function"
        }
        cc = uc
    } else
        cc = !1;
    jv = cc && (!document.documentMode || 9 < document.documentMode)
}
function Tm() {
    Hs && (Hs.detachEvent("onpropertychange", Cv),
    na = Hs = null)
}
function Cv(e) {
    if (e.propertyName === "value" && yl(na)) {
        var t = [];
        Sv(t, na, e, Pd(e)),
        ov(vb, t)
    }
}
function yb(e, t, n) {
    e === "focusin" ? (Tm(),
    Hs = t,
    na = n,
    Hs.attachEvent("onpropertychange", Cv)) : e === "focusout" && Tm()
}
function xb(e) {
    if (e === "selectionchange" || e === "keyup" || e === "keydown")
        return yl(na)
}
function wb(e, t) {
    if (e === "click")
        return yl(t)
}
function bb(e, t) {
    if (e === "input" || e === "change")
        return yl(t)
}
function Nb(e, t) {
    return e === t && (e !== 0 || 1 / e === 1 / t) || e !== e && t !== t
}
var Jt = typeof Object.is == "function" ? Object.is : Nb;
function ra(e, t) {
    if (Jt(e, t))
        return !0;
    if (typeof e != "object" || e === null || typeof t != "object" || t === null)
        return !1;
    var n = Object.keys(e)
      , r = Object.keys(t);
    if (n.length !== r.length)
        return !1;
    for (r = 0; r < n.length; r++) {
        var o = n[r];
        if (!Qc.call(t, o) || !Jt(e[o], t[o]))
            return !1
    }
    return !0
}
function Mm(e) {
    for (; e && e.firstChild; )
        e = e.firstChild;
    return e
}
function Rm(e, t) {
    var n = Mm(e);
    e = 0;
    for (var r; n; ) {
        if (n.nodeType === 3) {
            if (r = e + n.textContent.length,
            e <= t && r >= t)
                return {
                    node: n,
                    offset: t - e
                };
            e = r
        }
        e: {
            for (; n; ) {
                if (n.nextSibling) {
                    n = n.nextSibling;
                    break e
                }
                n = n.parentNode
            }
            n = void 0
        }
        n = Mm(n)
    }
}
function kv(e, t) {
    return e && t ? e === t ? !0 : e && e.nodeType === 3 ? !1 : t && t.nodeType === 3 ? kv(e, t.parentNode) : "contains"in e ? e.contains(t) : e.compareDocumentPosition ? !!(e.compareDocumentPosition(t) & 16) : !1 : !1
}
function Ev() {
    for (var e = window, t = _i(); t instanceof e.HTMLIFrameElement; ) {
        try {
            var n = typeof t.contentWindow.location.href == "string"
        } catch {
            n = !1
        }
        if (n)
            e = t.contentWindow;
        else
            break;
        t = _i(e.document)
    }
    return t
}
function Ld(e) {
    var t = e && e.nodeName && e.nodeName.toLowerCase();
    return t && (t === "input" && (e.type === "text" || e.type === "search" || e.type === "tel" || e.type === "url" || e.type === "password") || t === "textarea" || e.contentEditable === "true")
}
function Sb(e) {
    var t = Ev()
      , n = e.focusedElem
      , r = e.selectionRange;
    if (t !== n && n && n.ownerDocument && kv(n.ownerDocument.documentElement, n)) {
        if (r !== null && Ld(n)) {
            if (t = r.start,
            e = r.end,
            e === void 0 && (e = t),
            "selectionStart"in n)
                n.selectionStart = t,
                n.selectionEnd = Math.min(e, n.value.length);
            else if (e = (t = n.ownerDocument || document) && t.defaultView || window,
            e.getSelection) {
                e = e.getSelection();
                var o = n.textContent.length
                  , s = Math.min(r.start, o);
                r = r.end === void 0 ? s : Math.min(r.end, o),
                !e.extend && s > r && (o = r,
                r = s,
                s = o),
                o = Rm(n, s);
                var i = Rm(n, r);
                o && i && (e.rangeCount !== 1 || e.anchorNode !== o.node || e.anchorOffset !== o.offset || e.focusNode !== i.node || e.focusOffset !== i.offset) && (t = t.createRange(),
                t.setStart(o.node, o.offset),
                e.removeAllRanges(),
                s > r ? (e.addRange(t),
                e.extend(i.node, i.offset)) : (t.setEnd(i.node, i.offset),
                e.addRange(t)))
            }
        }
        for (t = [],
        e = n; e = e.parentNode; )
            e.nodeType === 1 && t.push({
                element: e,
                left: e.scrollLeft,
                top: e.scrollTop
            });
        for (typeof n.focus == "function" && n.focus(),
        n = 0; n < t.length; n++)
            e = t[n],
            e.element.scrollLeft = e.left,
            e.element.scrollTop = e.top
    }
}
var jb = Dn && "documentMode"in document && 11 >= document.documentMode
  , So = null
  , mu = null
  , Vs = null
  , hu = !1;
function _m(e, t, n) {
    var r = n.window === n ? n.document : n.nodeType === 9 ? n : n.ownerDocument;
    hu || So == null || So !== _i(r) || (r = So,
    "selectionStart"in r && Ld(r) ? r = {
        start: r.selectionStart,
        end: r.selectionEnd
    } : (r = (r.ownerDocument && r.ownerDocument.defaultView || window).getSelection(),
    r = {
        anchorNode: r.anchorNode,
        anchorOffset: r.anchorOffset,
        focusNode: r.focusNode,
        focusOffset: r.focusOffset
    }),
    Vs && ra(Vs, r) || (Vs = r,
    r = zi(mu, "onSelect"),
    0 < r.length && (t = new Od("onSelect","select",null,t,n),
    e.push({
        event: t,
        listeners: r
    }),
    t.target = So)))
}
function Ga(e, t) {
    var n = {};
    return n[e.toLowerCase()] = t.toLowerCase(),
    n["Webkit" + e] = "webkit" + t,
    n["Moz" + e] = "moz" + t,
    n
}
var jo = {
    animationend: Ga("Animation", "AnimationEnd"),
    animationiteration: Ga("Animation", "AnimationIteration"),
    animationstart: Ga("Animation", "AnimationStart"),
    transitionend: Ga("Transition", "TransitionEnd")
}
  , dc = {}
  , Pv = {};
Dn && (Pv = document.createElement("div").style,
"AnimationEvent"in window || (delete jo.animationend.animation,
delete jo.animationiteration.animation,
delete jo.animationstart.animation),
"TransitionEvent"in window || delete jo.transitionend.transition);
function xl(e) {
    if (dc[e])
        return dc[e];
    if (!jo[e])
        return e;
    var t = jo[e], n;
    for (n in t)
        if (t.hasOwnProperty(n) && n in Pv)
            return dc[e] = t[n];
    return e
}
var Tv = xl("animationend")
  , Mv = xl("animationiteration")
  , Rv = xl("animationstart")
  , _v = xl("transitionend")
  , Dv = new Map
  , Dm = "abort auxClick cancel canPlay canPlayThrough click close contextMenu copy cut drag dragEnd dragEnter dragExit dragLeave dragOver dragStart drop durationChange emptied encrypted ended error gotPointerCapture input invalid keyDown keyPress keyUp load loadedData loadedMetadata loadStart lostPointerCapture mouseDown mouseMove mouseOut mouseOver mouseUp paste pause play playing pointerCancel pointerDown pointerMove pointerOut pointerOver pointerUp progress rateChange reset resize seeked seeking stalled submit suspend timeUpdate touchCancel touchEnd touchStart volumeChange scroll toggle touchMove waiting wheel".split(" ");
function Sr(e, t) {
    Dv.set(e, t),
    oo(t, [e])
}
for (var fc = 0; fc < Dm.length; fc++) {
    var mc = Dm[fc]
      , Cb = mc.toLowerCase()
      , kb = mc[0].toUpperCase() + mc.slice(1);
    Sr(Cb, "on" + kb)
}
Sr(Tv, "onAnimationEnd");
Sr(Mv, "onAnimationIteration");
Sr(Rv, "onAnimationStart");
Sr("dblclick", "onDoubleClick");
Sr("focusin", "onFocus");
Sr("focusout", "onBlur");
Sr(_v, "onTransitionEnd");
qo("onMouseEnter", ["mouseout", "mouseover"]);
qo("onMouseLeave", ["mouseout", "mouseover"]);
qo("onPointerEnter", ["pointerout", "pointerover"]);
qo("onPointerLeave", ["pointerout", "pointerover"]);
oo("onChange", "change click focusin focusout input keydown keyup selectionchange".split(" "));
oo("onSelect", "focusout contextmenu dragend focusin keydown keyup mousedown mouseup selectionchange".split(" "));
oo("onBeforeInput", ["compositionend", "keypress", "textInput", "paste"]);
oo("onCompositionEnd", "compositionend focusout keydown keypress keyup mousedown".split(" "));
oo("onCompositionStart", "compositionstart focusout keydown keypress keyup mousedown".split(" "));
oo("onCompositionUpdate", "compositionupdate focusout keydown keypress keyup mousedown".split(" "));
var Fs = "abort canplay canplaythrough durationchange emptied encrypted ended error loadeddata loadedmetadata loadstart pause play playing progress ratechange resize seeked seeking stalled suspend timeupdate volumechange waiting".split(" ")
  , Eb = new Set("cancel close invalid load scroll toggle".split(" ").concat(Fs));
function Om(e, t, n) {
    var r = e.type || "unknown-event";
    e.currentTarget = n,
    C1(r, t, void 0, e),
    e.currentTarget = null
}
function Ov(e, t) {
    t = (t & 4) !== 0;
    for (var n = 0; n < e.length; n++) {
        var r = e[n]
          , o = r.event;
        r = r.listeners;
        e: {
            var s = void 0;
            if (t)
                for (var i = r.length - 1; 0 <= i; i--) {
                    var l = r[i]
                      , c = l.instance
                      , u = l.currentTarget;
                    if (l = l.listener,
                    c !== s && o.isPropagationStopped())
                        break e;
                    Om(o, l, u),
                    s = c
                }
            else
                for (i = 0; i < r.length; i++) {
                    if (l = r[i],
                    c = l.instance,
                    u = l.currentTarget,
                    l = l.listener,
                    c !== s && o.isPropagationStopped())
                        break e;
                    Om(o, l, u),
                    s = c
                }
        }
    }
    if (Oi)
        throw e = cu,
        Oi = !1,
        cu = null,
        e
}
function be(e, t) {
    var n = t[xu];
    n === void 0 && (n = t[xu] = new Set);
    var r = e + "__bubble";
    n.has(r) || (Av(t, e, 2, !1),
    n.add(r))
}
function hc(e, t, n) {
    var r = 0;
    t && (r |= 4),
    Av(n, e, r, t)
}
var qa = "_reactListening" + Math.random().toString(36).slice(2);
function oa(e) {
    if (!e[qa]) {
        e[qa] = !0,
        Wp.forEach(function(n) {
            n !== "selectionchange" && (Eb.has(n) || hc(n, !1, e),
            hc(n, !0, e))
        });
        var t = e.nodeType === 9 ? e : e.ownerDocument;
        t === null || t[qa] || (t[qa] = !0,
        hc("selectionchange", !1, t))
    }
}
function Av(e, t, n, r) {
    switch (yv(t)) {
    case 1:
        var o = B1;
        break;
    case 4:
        o = W1;
        break;
    default:
        o = _d
    }
    n = o.bind(null, t, n, e),
    o = void 0,
    !lu || t !== "touchstart" && t !== "touchmove" && t !== "wheel" || (o = !0),
    r ? o !== void 0 ? e.addEventListener(t, n, {
        capture: !0,
        passive: o
    }) : e.addEventListener(t, n, !0) : o !== void 0 ? e.addEventListener(t, n, {
        passive: o
    }) : e.addEventListener(t, n, !1)
}
function pc(e, t, n, r, o) {
    var s = r;
    if (!(t & 1) && !(t & 2) && r !== null)
        e: for (; ; ) {
            if (r === null)
                return;
            var i = r.tag;
            if (i === 3 || i === 4) {
                var l = r.stateNode.containerInfo;
                if (l === o || l.nodeType === 8 && l.parentNode === o)
                    break;
                if (i === 4)
                    for (i = r.return; i !== null; ) {
                        var c = i.tag;
                        if ((c === 3 || c === 4) && (c = i.stateNode.containerInfo,
                        c === o || c.nodeType === 8 && c.parentNode === o))
                            return;
                        i = i.return
                    }
                for (; l !== null; ) {
                    if (i = Ir(l),
                    i === null)
                        return;
                    if (c = i.tag,
                    c === 5 || c === 6) {
                        r = s = i;
                        continue e
                    }
                    l = l.parentNode
                }
            }
            r = r.return
        }
    ov(function() {
        var u = s
          , d = Pd(n)
          , f = [];
        e: {
            var g = Dv.get(e);
            if (g !== void 0) {
                var h = Od
                  , b = e;
                switch (e) {
                case "keypress":
                    if (gi(n) === 0)
                        break e;
                case "keydown":
                case "keyup":
                    h = rb;
                    break;
                case "focusin":
                    b = "focus",
                    h = lc;
                    break;
                case "focusout":
                    b = "blur",
                    h = lc;
                    break;
                case "beforeblur":
                case "afterblur":
                    h = lc;
                    break;
                case "click":
                    if (n.button === 2)
                        break e;
                case "auxclick":
                case "dblclick":
                case "mousedown":
                case "mousemove":
                case "mouseup":
                case "mouseout":
                case "mouseover":
                case "contextmenu":
                    h = Nm;
                    break;
                case "drag":
                case "dragend":
                case "dragenter":
                case "dragexit":
                case "dragleave":
                case "dragover":
                case "dragstart":
                case "drop":
                    h = U1;
                    break;
                case "touchcancel":
                case "touchend":
                case "touchmove":
                case "touchstart":
                    h = ab;
                    break;
                case Tv:
                case Mv:
                case Rv:
                    h = Q1;
                    break;
                case _v:
                    h = lb;
                    break;
                case "scroll":
                    h = H1;
                    break;
                case "wheel":
                    h = ub;
                    break;
                case "copy":
                case "cut":
                case "paste":
                    h = q1;
                    break;
                case "gotpointercapture":
                case "lostpointercapture":
                case "pointercancel":
                case "pointerdown":
                case "pointermove":
                case "pointerout":
                case "pointerover":
                case "pointerup":
                    h = jm
                }
                var v = (t & 4) !== 0
                  , w = !v && e === "scroll"
                  , y = v ? g !== null ? g + "Capture" : null : g;
                v = [];
                for (var p = u, x; p !== null; ) {
                    x = p;
                    var N = x.stateNode;
                    if (x.tag === 5 && N !== null && (x = N,
                    y !== null && (N = Js(p, y),
                    N != null && v.push(sa(p, N, x)))),
                    w)
                        break;
                    p = p.return
                }
                0 < v.length && (g = new h(g,b,null,n,d),
                f.push({
                    event: g,
                    listeners: v
                }))
            }
        }
        if (!(t & 7)) {
            e: {
                if (g = e === "mouseover" || e === "pointerover",
                h = e === "mouseout" || e === "pointerout",
                g && n !== au && (b = n.relatedTarget || n.fromElement) && (Ir(b) || b[On]))
                    break e;
                if ((h || g) && (g = d.window === d ? d : (g = d.ownerDocument) ? g.defaultView || g.parentWindow : window,
                h ? (b = n.relatedTarget || n.toElement,
                h = u,
                b = b ? Ir(b) : null,
                b !== null && (w = so(b),
                b !== w || b.tag !== 5 && b.tag !== 6) && (b = null)) : (h = null,
                b = u),
                h !== b)) {
                    if (v = Nm,
                    N = "onMouseLeave",
                    y = "onMouseEnter",
                    p = "mouse",
                    (e === "pointerout" || e === "pointerover") && (v = jm,
                    N = "onPointerLeave",
                    y = "onPointerEnter",
                    p = "pointer"),
                    w = h == null ? g : Co(h),
                    x = b == null ? g : Co(b),
                    g = new v(N,p + "leave",h,n,d),
                    g.target = w,
                    g.relatedTarget = x,
                    N = null,
                    Ir(d) === u && (v = new v(y,p + "enter",b,n,d),
                    v.target = x,
                    v.relatedTarget = w,
                    N = v),
                    w = N,
                    h && b)
                        t: {
                            for (v = h,
                            y = b,
                            p = 0,
                            x = v; x; x = po(x))
                                p++;
                            for (x = 0,
                            N = y; N; N = po(N))
                                x++;
                            for (; 0 < p - x; )
                                v = po(v),
                                p--;
                            for (; 0 < x - p; )
                                y = po(y),
                                x--;
                            for (; p--; ) {
                                if (v === y || y !== null && v === y.alternate)
                                    break t;
                                v = po(v),
                                y = po(y)
                            }
                            v = null
                        }
                    else
                        v = null;
                    h !== null && Am(f, g, h, v, !1),
                    b !== null && w !== null && Am(f, w, b, v, !0)
                }
            }
            e: {
                if (g = u ? Co(u) : window,
                h = g.nodeName && g.nodeName.toLowerCase(),
                h === "select" || h === "input" && g.type === "file")
                    var S = gb;
                else if (Em(g))
                    if (jv)
                        S = bb;
                    else {
                        S = xb;
                        var k = yb
                    }
                else
                    (h = g.nodeName) && h.toLowerCase() === "input" && (g.type === "checkbox" || g.type === "radio") && (S = wb);
                if (S && (S = S(e, u))) {
                    Sv(f, S, n, d);
                    break e
                }
                k && k(e, g, u),
                e === "focusout" && (k = g._wrapperState) && k.controlled && g.type === "number" && tu(g, "number", g.value)
            }
            switch (k = u ? Co(u) : window,
            e) {
            case "focusin":
                (Em(k) || k.contentEditable === "true") && (So = k,
                mu = u,
                Vs = null);
                break;
            case "focusout":
                Vs = mu = So = null;
                break;
            case "mousedown":
                hu = !0;
                break;
            case "contextmenu":
            case "mouseup":
            case "dragend":
                hu = !1,
                _m(f, n, d);
                break;
            case "selectionchange":
                if (jb)
                    break;
            case "keydown":
            case "keyup":
                _m(f, n, d)
            }
            var C;
            if (Id)
                e: {
                    switch (e) {
                    case "compositionstart":
                        var T = "onCompositionStart";
                        break e;
                    case "compositionend":
                        T = "onCompositionEnd";
                        break e;
                    case "compositionupdate":
                        T = "onCompositionUpdate";
                        break e
                    }
                    T = void 0
                }
            else
                No ? bv(e, n) && (T = "onCompositionEnd") : e === "keydown" && n.keyCode === 229 && (T = "onCompositionStart");
            T && (wv && n.locale !== "ko" && (No || T !== "onCompositionStart" ? T === "onCompositionEnd" && No && (C = xv()) : (sr = d,
            Dd = "value"in sr ? sr.value : sr.textContent,
            No = !0)),
            k = zi(u, T),
            0 < k.length && (T = new Sm(T,e,null,n,d),
            f.push({
                event: T,
                listeners: k
            }),
            C ? T.data = C : (C = Nv(n),
            C !== null && (T.data = C)))),
            (C = fb ? mb(e, n) : hb(e, n)) && (u = zi(u, "onBeforeInput"),
            0 < u.length && (d = new Sm("onBeforeInput","beforeinput",null,n,d),
            f.push({
                event: d,
                listeners: u
            }),
            d.data = C))
        }
        Ov(f, t)
    })
}
function sa(e, t, n) {
    return {
        instance: e,
        listener: t,
        currentTarget: n
    }
}
function zi(e, t) {
    for (var n = t + "Capture", r = []; e !== null; ) {
        var o = e
          , s = o.stateNode;
        o.tag === 5 && s !== null && (o = s,
        s = Js(e, n),
        s != null && r.unshift(sa(e, s, o)),
        s = Js(e, t),
        s != null && r.push(sa(e, s, o))),
        e = e.return
    }
    return r
}
function po(e) {
    if (e === null)
        return null;
    do
        e = e.return;
    while (e && e.tag !== 5);
    return e || null
}
function Am(e, t, n, r, o) {
    for (var s = t._reactName, i = []; n !== null && n !== r; ) {
        var l = n
          , c = l.alternate
          , u = l.stateNode;
        if (c !== null && c === r)
            break;
        l.tag === 5 && u !== null && (l = u,
        o ? (c = Js(n, s),
        c != null && i.unshift(sa(n, c, l))) : o || (c = Js(n, s),
        c != null && i.push(sa(n, c, l)))),
        n = n.return
    }
    i.length !== 0 && e.push({
        event: t,
        listeners: i
    })
}
var Pb = /\r\n?/g
  , Tb = /\u0000|\uFFFD/g;
function Im(e) {
    return (typeof e == "string" ? e : "" + e).replace(Pb, `
`).replace(Tb, "")
}
function Xa(e, t, n) {
    if (t = Im(t),
    Im(e) !== t && n)
        throw Error(_(425))
}
function $i() {}
var pu = null
  , vu = null;
function gu(e, t) {
    return e === "textarea" || e === "noscript" || typeof t.children == "string" || typeof t.children == "number" || typeof t.dangerouslySetInnerHTML == "object" && t.dangerouslySetInnerHTML !== null && t.dangerouslySetInnerHTML.__html != null
}
var yu = typeof setTimeout == "function" ? setTimeout : void 0
  , Mb = typeof clearTimeout == "function" ? clearTimeout : void 0
  , Lm = typeof Promise == "function" ? Promise : void 0
  , Rb = typeof queueMicrotask == "function" ? queueMicrotask : typeof Lm < "u" ? function(e) {
    return Lm.resolve(null).then(e).catch(_b)
}
: yu;
function _b(e) {
    setTimeout(function() {
        throw e
    })
}
function vc(e, t) {
    var n = t
      , r = 0;
    do {
        var o = n.nextSibling;
        if (e.removeChild(n),
        o && o.nodeType === 8)
            if (n = o.data,
            n === "/$") {
                if (r === 0) {
                    e.removeChild(o),
                    ta(t);
                    return
                }
                r--
            } else
                n !== "$" && n !== "$?" && n !== "$!" || r++;
        n = o
    } while (n);
    ta(t)
}
function fr(e) {
    for (; e != null; e = e.nextSibling) {
        var t = e.nodeType;
        if (t === 1 || t === 3)
            break;
        if (t === 8) {
            if (t = e.data,
            t === "$" || t === "$!" || t === "$?")
                break;
            if (t === "/$")
                return null
        }
    }
    return e
}
function Fm(e) {
    e = e.previousSibling;
    for (var t = 0; e; ) {
        if (e.nodeType === 8) {
            var n = e.data;
            if (n === "$" || n === "$!" || n === "$?") {
                if (t === 0)
                    return e;
                t--
            } else
                n === "/$" && t++
        }
        e = e.previousSibling
    }
    return null
}
var fs = Math.random().toString(36).slice(2)
  , dn = "__reactFiber$" + fs
  , aa = "__reactProps$" + fs
  , On = "__reactContainer$" + fs
  , xu = "__reactEvents$" + fs
  , Db = "__reactListeners$" + fs
  , Ob = "__reactHandles$" + fs;
function Ir(e) {
    var t = e[dn];
    if (t)
        return t;
    for (var n = e.parentNode; n; ) {
        if (t = n[On] || n[dn]) {
            if (n = t.alternate,
            t.child !== null || n !== null && n.child !== null)
                for (e = Fm(e); e !== null; ) {
                    if (n = e[dn])
                        return n;
                    e = Fm(e)
                }
            return t
        }
        e = n,
        n = e.parentNode
    }
    return null
}
function Ea(e) {
    return e = e[dn] || e[On],
    !e || e.tag !== 5 && e.tag !== 6 && e.tag !== 13 && e.tag !== 3 ? null : e
}
function Co(e) {
    if (e.tag === 5 || e.tag === 6)
        return e.stateNode;
    throw Error(_(33))
}
function wl(e) {
    return e[aa] || null
}
var wu = []
  , ko = -1;
function jr(e) {
    return {
        current: e
    }
}
function Ne(e) {
    0 > ko || (e.current = wu[ko],
    wu[ko] = null,
    ko--)
}
function ge(e, t) {
    ko++,
    wu[ko] = e.current,
    e.current = t
}
var xr = {}
  , Je = jr(xr)
  , dt = jr(!1)
  , Kr = xr;
function Xo(e, t) {
    var n = e.type.contextTypes;
    if (!n)
        return xr;
    var r = e.stateNode;
    if (r && r.__reactInternalMemoizedUnmaskedChildContext === t)
        return r.__reactInternalMemoizedMaskedChildContext;
    var o = {}, s;
    for (s in n)
        o[s] = t[s];
    return r && (e = e.stateNode,
    e.__reactInternalMemoizedUnmaskedChildContext = t,
    e.__reactInternalMemoizedMaskedChildContext = o),
    o
}
function ft(e) {
    return e = e.childContextTypes,
    e != null
}
function Bi() {
    Ne(dt),
    Ne(Je)
}
function zm(e, t, n) {
    if (Je.current !== xr)
        throw Error(_(168));
    ge(Je, t),
    ge(dt, n)
}
function Iv(e, t, n) {
    var r = e.stateNode;
    if (t = t.childContextTypes,
    typeof r.getChildContext != "function")
        return n;
    r = r.getChildContext();
    for (var o in r)
        if (!(o in t))
            throw Error(_(108, y1(e) || "Unknown", o));
    return Te({}, n, r)
}
function Wi(e) {
    return e = (e = e.stateNode) && e.__reactInternalMemoizedMergedChildContext || xr,
    Kr = Je.current,
    ge(Je, e),
    ge(dt, dt.current),
    !0
}
function $m(e, t, n) {
    var r = e.stateNode;
    if (!r)
        throw Error(_(169));
    n ? (e = Iv(e, t, Kr),
    r.__reactInternalMemoizedMergedChildContext = e,
    Ne(dt),
    Ne(Je),
    ge(Je, e)) : Ne(dt),
    ge(dt, n)
}
var En = null
  , bl = !1
  , gc = !1;
function Lv(e) {
    En === null ? En = [e] : En.push(e)
}
function Ab(e) {
    bl = !0,
    Lv(e)
}
function Cr() {
    if (!gc && En !== null) {
        gc = !0;
        var e = 0
          , t = pe;
        try {
            var n = En;
            for (pe = 1; e < n.length; e++) {
                var r = n[e];
                do
                    r = r(!0);
                while (r !== null)
            }
            En = null,
            bl = !1
        } catch (o) {
            throw En !== null && (En = En.slice(e + 1)),
            lv(Td, Cr),
            o
        } finally {
            pe = t,
            gc = !1
        }
    }
    return null
}
var Eo = []
  , Po = 0
  , Hi = null
  , Vi = 0
  , Et = []
  , Pt = 0
  , Qr = null
  , Tn = 1
  , Mn = "";
function Dr(e, t) {
    Eo[Po++] = Vi,
    Eo[Po++] = Hi,
    Hi = e,
    Vi = t
}
function Fv(e, t, n) {
    Et[Pt++] = Tn,
    Et[Pt++] = Mn,
    Et[Pt++] = Qr,
    Qr = e;
    var r = Tn;
    e = Mn;
    var o = 32 - Gt(r) - 1;
    r &= ~(1 << o),
    n += 1;
    var s = 32 - Gt(t) + o;
    if (30 < s) {
        var i = o - o % 5;
        s = (r & (1 << i) - 1).toString(32),
        r >>= i,
        o -= i,
        Tn = 1 << 32 - Gt(t) + o | n << o | r,
        Mn = s + e
    } else
        Tn = 1 << s | n << o | r,
        Mn = e
}
function Fd(e) {
    e.return !== null && (Dr(e, 1),
    Fv(e, 1, 0))
}
function zd(e) {
    for (; e === Hi; )
        Hi = Eo[--Po],
        Eo[Po] = null,
        Vi = Eo[--Po],
        Eo[Po] = null;
    for (; e === Qr; )
        Qr = Et[--Pt],
        Et[Pt] = null,
        Mn = Et[--Pt],
        Et[Pt] = null,
        Tn = Et[--Pt],
        Et[Pt] = null
}
var yt = null
  , gt = null
  , je = !1
  , Yt = null;
function zv(e, t) {
    var n = Tt(5, null, null, 0);
    n.elementType = "DELETED",
    n.stateNode = t,
    n.return = e,
    t = e.deletions,
    t === null ? (e.deletions = [n],
    e.flags |= 16) : t.push(n)
}
function Bm(e, t) {
    switch (e.tag) {
    case 5:
        var n = e.type;
        return t = t.nodeType !== 1 || n.toLowerCase() !== t.nodeName.toLowerCase() ? null : t,
        t !== null ? (e.stateNode = t,
        yt = e,
        gt = fr(t.firstChild),
        !0) : !1;
    case 6:
        return t = e.pendingProps === "" || t.nodeType !== 3 ? null : t,
        t !== null ? (e.stateNode = t,
        yt = e,
        gt = null,
        !0) : !1;
    case 13:
        return t = t.nodeType !== 8 ? null : t,
        t !== null ? (n = Qr !== null ? {
            id: Tn,
            overflow: Mn
        } : null,
        e.memoizedState = {
            dehydrated: t,
            treeContext: n,
            retryLane: 1073741824
        },
        n = Tt(18, null, null, 0),
        n.stateNode = t,
        n.return = e,
        e.child = n,
        yt = e,
        gt = null,
        !0) : !1;
    default:
        return !1
    }
}
function bu(e) {
    return (e.mode & 1) !== 0 && (e.flags & 128) === 0
}
function Nu(e) {
    if (je) {
        var t = gt;
        if (t) {
            var n = t;
            if (!Bm(e, t)) {
                if (bu(e))
                    throw Error(_(418));
                t = fr(n.nextSibling);
                var r = yt;
                t && Bm(e, t) ? zv(r, n) : (e.flags = e.flags & -4097 | 2,
                je = !1,
                yt = e)
            }
        } else {
            if (bu(e))
                throw Error(_(418));
            e.flags = e.flags & -4097 | 2,
            je = !1,
            yt = e
        }
    }
}
function Wm(e) {
    for (e = e.return; e !== null && e.tag !== 5 && e.tag !== 3 && e.tag !== 13; )
        e = e.return;
    yt = e
}
function Ja(e) {
    if (e !== yt)
        return !1;
    if (!je)
        return Wm(e),
        je = !0,
        !1;
    var t;
    if ((t = e.tag !== 3) && !(t = e.tag !== 5) && (t = e.type,
    t = t !== "head" && t !== "body" && !gu(e.type, e.memoizedProps)),
    t && (t = gt)) {
        if (bu(e))
            throw $v(),
            Error(_(418));
        for (; t; )
            zv(e, t),
            t = fr(t.nextSibling)
    }
    if (Wm(e),
    e.tag === 13) {
        if (e = e.memoizedState,
        e = e !== null ? e.dehydrated : null,
        !e)
            throw Error(_(317));
        e: {
            for (e = e.nextSibling,
            t = 0; e; ) {
                if (e.nodeType === 8) {
                    var n = e.data;
                    if (n === "/$") {
                        if (t === 0) {
                            gt = fr(e.nextSibling);
                            break e
                        }
                        t--
                    } else
                        n !== "$" && n !== "$!" && n !== "$?" || t++
                }
                e = e.nextSibling
            }
            gt = null
        }
    } else
        gt = yt ? fr(e.stateNode.nextSibling) : null;
    return !0
}
function $v() {
    for (var e = gt; e; )
        e = fr(e.nextSibling)
}
function Jo() {
    gt = yt = null,
    je = !1
}
function $d(e) {
    Yt === null ? Yt = [e] : Yt.push(e)
}
var Ib = zn.ReactCurrentBatchConfig;
function Ps(e, t, n) {
    if (e = n.ref,
    e !== null && typeof e != "function" && typeof e != "object") {
        if (n._owner) {
            if (n = n._owner,
            n) {
                if (n.tag !== 1)
                    throw Error(_(309));
                var r = n.stateNode
            }
            if (!r)
                throw Error(_(147, e));
            var o = r
              , s = "" + e;
            return t !== null && t.ref !== null && typeof t.ref == "function" && t.ref._stringRef === s ? t.ref : (t = function(i) {
                var l = o.refs;
                i === null ? delete l[s] : l[s] = i
            }
            ,
            t._stringRef = s,
            t)
        }
        if (typeof e != "string")
            throw Error(_(284));
        if (!n._owner)
            throw Error(_(290, e))
    }
    return e
}
function Za(e, t) {
    throw e = Object.prototype.toString.call(t),
    Error(_(31, e === "[object Object]" ? "object with keys {" + Object.keys(t).join(", ") + "}" : e))
}
function Hm(e) {
    var t = e._init;
    return t(e._payload)
}
function Bv(e) {
    function t(y, p) {
        if (e) {
            var x = y.deletions;
            x === null ? (y.deletions = [p],
            y.flags |= 16) : x.push(p)
        }
    }
    function n(y, p) {
        if (!e)
            return null;
        for (; p !== null; )
            t(y, p),
            p = p.sibling;
        return null
    }
    function r(y, p) {
        for (y = new Map; p !== null; )
            p.key !== null ? y.set(p.key, p) : y.set(p.index, p),
            p = p.sibling;
        return y
    }
    function o(y, p) {
        return y = vr(y, p),
        y.index = 0,
        y.sibling = null,
        y
    }
    function s(y, p, x) {
        return y.index = x,
        e ? (x = y.alternate,
        x !== null ? (x = x.index,
        x < p ? (y.flags |= 2,
        p) : x) : (y.flags |= 2,
        p)) : (y.flags |= 1048576,
        p)
    }
    function i(y) {
        return e && y.alternate === null && (y.flags |= 2),
        y
    }
    function l(y, p, x, N) {
        return p === null || p.tag !== 6 ? (p = jc(x, y.mode, N),
        p.return = y,
        p) : (p = o(p, x),
        p.return = y,
        p)
    }
    function c(y, p, x, N) {
        var S = x.type;
        return S === bo ? d(y, p, x.props.children, N, x.key) : p !== null && (p.elementType === S || typeof S == "object" && S !== null && S.$$typeof === qn && Hm(S) === p.type) ? (N = o(p, x.props),
        N.ref = Ps(y, p, x),
        N.return = y,
        N) : (N = ji(x.type, x.key, x.props, null, y.mode, N),
        N.ref = Ps(y, p, x),
        N.return = y,
        N)
    }
    function u(y, p, x, N) {
        return p === null || p.tag !== 4 || p.stateNode.containerInfo !== x.containerInfo || p.stateNode.implementation !== x.implementation ? (p = Cc(x, y.mode, N),
        p.return = y,
        p) : (p = o(p, x.children || []),
        p.return = y,
        p)
    }
    function d(y, p, x, N, S) {
        return p === null || p.tag !== 7 ? (p = Yr(x, y.mode, N, S),
        p.return = y,
        p) : (p = o(p, x),
        p.return = y,
        p)
    }
    function f(y, p, x) {
        if (typeof p == "string" && p !== "" || typeof p == "number")
            return p = jc("" + p, y.mode, x),
            p.return = y,
            p;
        if (typeof p == "object" && p !== null) {
            switch (p.$$typeof) {
            case Wa:
                return x = ji(p.type, p.key, p.props, null, y.mode, x),
                x.ref = Ps(y, null, p),
                x.return = y,
                x;
            case wo:
                return p = Cc(p, y.mode, x),
                p.return = y,
                p;
            case qn:
                var N = p._init;
                return f(y, N(p._payload), x)
            }
            if (Is(p) || Ss(p))
                return p = Yr(p, y.mode, x, null),
                p.return = y,
                p;
            Za(y, p)
        }
        return null
    }
    function g(y, p, x, N) {
        var S = p !== null ? p.key : null;
        if (typeof x == "string" && x !== "" || typeof x == "number")
            return S !== null ? null : l(y, p, "" + x, N);
        if (typeof x == "object" && x !== null) {
            switch (x.$$typeof) {
            case Wa:
                return x.key === S ? c(y, p, x, N) : null;
            case wo:
                return x.key === S ? u(y, p, x, N) : null;
            case qn:
                return S = x._init,
                g(y, p, S(x._payload), N)
            }
            if (Is(x) || Ss(x))
                return S !== null ? null : d(y, p, x, N, null);
            Za(y, x)
        }
        return null
    }
    function h(y, p, x, N, S) {
        if (typeof N == "string" && N !== "" || typeof N == "number")
            return y = y.get(x) || null,
            l(p, y, "" + N, S);
        if (typeof N == "object" && N !== null) {
            switch (N.$$typeof) {
            case Wa:
                return y = y.get(N.key === null ? x : N.key) || null,
                c(p, y, N, S);
            case wo:
                return y = y.get(N.key === null ? x : N.key) || null,
                u(p, y, N, S);
            case qn:
                var k = N._init;
                return h(y, p, x, k(N._payload), S)
            }
            if (Is(N) || Ss(N))
                return y = y.get(x) || null,
                d(p, y, N, S, null);
            Za(p, N)
        }
        return null
    }
    function b(y, p, x, N) {
        for (var S = null, k = null, C = p, T = p = 0, D = null; C !== null && T < x.length; T++) {
            C.index > T ? (D = C,
            C = null) : D = C.sibling;
            var R = g(y, C, x[T], N);
            if (R === null) {
                C === null && (C = D);
                break
            }
            e && C && R.alternate === null && t(y, C),
            p = s(R, p, T),
            k === null ? S = R : k.sibling = R,
            k = R,
            C = D
        }
        if (T === x.length)
            return n(y, C),
            je && Dr(y, T),
            S;
        if (C === null) {
            for (; T < x.length; T++)
                C = f(y, x[T], N),
                C !== null && (p = s(C, p, T),
                k === null ? S = C : k.sibling = C,
                k = C);
            return je && Dr(y, T),
            S
        }
        for (C = r(y, C); T < x.length; T++)
            D = h(C, y, T, x[T], N),
            D !== null && (e && D.alternate !== null && C.delete(D.key === null ? T : D.key),
            p = s(D, p, T),
            k === null ? S = D : k.sibling = D,
            k = D);
        return e && C.forEach(function(F) {
            return t(y, F)
        }),
        je && Dr(y, T),
        S
    }
    function v(y, p, x, N) {
        var S = Ss(x);
        if (typeof S != "function")
            throw Error(_(150));
        if (x = S.call(x),
        x == null)
            throw Error(_(151));
        for (var k = S = null, C = p, T = p = 0, D = null, R = x.next(); C !== null && !R.done; T++,
        R = x.next()) {
            C.index > T ? (D = C,
            C = null) : D = C.sibling;
            var F = g(y, C, R.value, N);
            if (F === null) {
                C === null && (C = D);
                break
            }
            e && C && F.alternate === null && t(y, C),
            p = s(F, p, T),
            k === null ? S = F : k.sibling = F,
            k = F,
            C = D
        }
        if (R.done)
            return n(y, C),
            je && Dr(y, T),
            S;
        if (C === null) {
            for (; !R.done; T++,
            R = x.next())
                R = f(y, R.value, N),
                R !== null && (p = s(R, p, T),
                k === null ? S = R : k.sibling = R,
                k = R);
            return je && Dr(y, T),
            S
        }
        for (C = r(y, C); !R.done; T++,
        R = x.next())
            R = h(C, y, T, R.value, N),
            R !== null && (e && R.alternate !== null && C.delete(R.key === null ? T : R.key),
            p = s(R, p, T),
            k === null ? S = R : k.sibling = R,
            k = R);
        return e && C.forEach(function(A) {
            return t(y, A)
        }),
        je && Dr(y, T),
        S
    }
    function w(y, p, x, N) {
        if (typeof x == "object" && x !== null && x.type === bo && x.key === null && (x = x.props.children),
        typeof x == "object" && x !== null) {
            switch (x.$$typeof) {
            case Wa:
                e: {
                    for (var S = x.key, k = p; k !== null; ) {
                        if (k.key === S) {
                            if (S = x.type,
                            S === bo) {
                                if (k.tag === 7) {
                                    n(y, k.sibling),
                                    p = o(k, x.props.children),
                                    p.return = y,
                                    y = p;
                                    break e
                                }
                            } else if (k.elementType === S || typeof S == "object" && S !== null && S.$$typeof === qn && Hm(S) === k.type) {
                                n(y, k.sibling),
                                p = o(k, x.props),
                                p.ref = Ps(y, k, x),
                                p.return = y,
                                y = p;
                                break e
                            }
                            n(y, k);
                            break
                        } else
                            t(y, k);
                        k = k.sibling
                    }
                    x.type === bo ? (p = Yr(x.props.children, y.mode, N, x.key),
                    p.return = y,
                    y = p) : (N = ji(x.type, x.key, x.props, null, y.mode, N),
                    N.ref = Ps(y, p, x),
                    N.return = y,
                    y = N)
                }
                return i(y);
            case wo:
                e: {
                    for (k = x.key; p !== null; ) {
                        if (p.key === k)
                            if (p.tag === 4 && p.stateNode.containerInfo === x.containerInfo && p.stateNode.implementation === x.implementation) {
                                n(y, p.sibling),
                                p = o(p, x.children || []),
                                p.return = y,
                                y = p;
                                break e
                            } else {
                                n(y, p);
                                break
                            }
                        else
                            t(y, p);
                        p = p.sibling
                    }
                    p = Cc(x, y.mode, N),
                    p.return = y,
                    y = p
                }
                return i(y);
            case qn:
                return k = x._init,
                w(y, p, k(x._payload), N)
            }
            if (Is(x))
                return b(y, p, x, N);
            if (Ss(x))
                return v(y, p, x, N);
            Za(y, x)
        }
        return typeof x == "string" && x !== "" || typeof x == "number" ? (x = "" + x,
        p !== null && p.tag === 6 ? (n(y, p.sibling),
        p = o(p, x),
        p.return = y,
        y = p) : (n(y, p),
        p = jc(x, y.mode, N),
        p.return = y,
        y = p),
        i(y)) : n(y, p)
    }
    return w
}
var Zo = Bv(!0)
  , Wv = Bv(!1)
  , Ui = jr(null)
  , Yi = null
  , To = null
  , Bd = null;
function Wd() {
    Bd = To = Yi = null
}
function Hd(e) {
    var t = Ui.current;
    Ne(Ui),
    e._currentValue = t
}
function Su(e, t, n) {
    for (; e !== null; ) {
        var r = e.alternate;
        if ((e.childLanes & t) !== t ? (e.childLanes |= t,
        r !== null && (r.childLanes |= t)) : r !== null && (r.childLanes & t) !== t && (r.childLanes |= t),
        e === n)
            break;
        e = e.return
    }
}
function Io(e, t) {
    Yi = e,
    Bd = To = null,
    e = e.dependencies,
    e !== null && e.firstContext !== null && (e.lanes & t && (ct = !0),
    e.firstContext = null)
}
function Dt(e) {
    var t = e._currentValue;
    if (Bd !== e)
        if (e = {
            context: e,
            memoizedValue: t,
            next: null
        },
        To === null) {
            if (Yi === null)
                throw Error(_(308));
            To = e,
            Yi.dependencies = {
                lanes: 0,
                firstContext: e
            }
        } else
            To = To.next = e;
    return t
}
var Lr = null;
function Vd(e) {
    Lr === null ? Lr = [e] : Lr.push(e)
}
function Hv(e, t, n, r) {
    var o = t.interleaved;
    return o === null ? (n.next = n,
    Vd(t)) : (n.next = o.next,
    o.next = n),
    t.interleaved = n,
    An(e, r)
}
function An(e, t) {
    e.lanes |= t;
    var n = e.alternate;
    for (n !== null && (n.lanes |= t),
    n = e,
    e = e.return; e !== null; )
        e.childLanes |= t,
        n = e.alternate,
        n !== null && (n.childLanes |= t),
        n = e,
        e = e.return;
    return n.tag === 3 ? n.stateNode : null
}
var Xn = !1;
function Ud(e) {
    e.updateQueue = {
        baseState: e.memoizedState,
        firstBaseUpdate: null,
        lastBaseUpdate: null,
        shared: {
            pending: null,
            interleaved: null,
            lanes: 0
        },
        effects: null
    }
}
function Vv(e, t) {
    e = e.updateQueue,
    t.updateQueue === e && (t.updateQueue = {
        baseState: e.baseState,
        firstBaseUpdate: e.firstBaseUpdate,
        lastBaseUpdate: e.lastBaseUpdate,
        shared: e.shared,
        effects: e.effects
    })
}
function Rn(e, t) {
    return {
        eventTime: e,
        lane: t,
        tag: 0,
        payload: null,
        callback: null,
        next: null
    }
}
function mr(e, t, n) {
    var r = e.updateQueue;
    if (r === null)
        return null;
    if (r = r.shared,
    ie & 2) {
        var o = r.pending;
        return o === null ? t.next = t : (t.next = o.next,
        o.next = t),
        r.pending = t,
        An(e, n)
    }
    return o = r.interleaved,
    o === null ? (t.next = t,
    Vd(r)) : (t.next = o.next,
    o.next = t),
    r.interleaved = t,
    An(e, n)
}
function yi(e, t, n) {
    if (t = t.updateQueue,
    t !== null && (t = t.shared,
    (n & 4194240) !== 0)) {
        var r = t.lanes;
        r &= e.pendingLanes,
        n |= r,
        t.lanes = n,
        Md(e, n)
    }
}
function Vm(e, t) {
    var n = e.updateQueue
      , r = e.alternate;
    if (r !== null && (r = r.updateQueue,
    n === r)) {
        var o = null
          , s = null;
        if (n = n.firstBaseUpdate,
        n !== null) {
            do {
                var i = {
                    eventTime: n.eventTime,
                    lane: n.lane,
                    tag: n.tag,
                    payload: n.payload,
                    callback: n.callback,
                    next: null
                };
                s === null ? o = s = i : s = s.next = i,
                n = n.next
            } while (n !== null);
            s === null ? o = s = t : s = s.next = t
        } else
            o = s = t;
        n = {
            baseState: r.baseState,
            firstBaseUpdate: o,
            lastBaseUpdate: s,
            shared: r.shared,
            effects: r.effects
        },
        e.updateQueue = n;
        return
    }
    e = n.lastBaseUpdate,
    e === null ? n.firstBaseUpdate = t : e.next = t,
    n.lastBaseUpdate = t
}
function Ki(e, t, n, r) {
    var o = e.updateQueue;
    Xn = !1;
    var s = o.firstBaseUpdate
      , i = o.lastBaseUpdate
      , l = o.shared.pending;
    if (l !== null) {
        o.shared.pending = null;
        var c = l
          , u = c.next;
        c.next = null,
        i === null ? s = u : i.next = u,
        i = c;
        var d = e.alternate;
        d !== null && (d = d.updateQueue,
        l = d.lastBaseUpdate,
        l !== i && (l === null ? d.firstBaseUpdate = u : l.next = u,
        d.lastBaseUpdate = c))
    }
    if (s !== null) {
        var f = o.baseState;
        i = 0,
        d = u = c = null,
        l = s;
        do {
            var g = l.lane
              , h = l.eventTime;
            if ((r & g) === g) {
                d !== null && (d = d.next = {
                    eventTime: h,
                    lane: 0,
                    tag: l.tag,
                    payload: l.payload,
                    callback: l.callback,
                    next: null
                });
                e: {
                    var b = e
                      , v = l;
                    switch (g = t,
                    h = n,
                    v.tag) {
                    case 1:
                        if (b = v.payload,
                        typeof b == "function") {
                            f = b.call(h, f, g);
                            break e
                        }
                        f = b;
                        break e;
                    case 3:
                        b.flags = b.flags & -65537 | 128;
                    case 0:
                        if (b = v.payload,
                        g = typeof b == "function" ? b.call(h, f, g) : b,
                        g == null)
                            break e;
                        f = Te({}, f, g);
                        break e;
                    case 2:
                        Xn = !0
                    }
                }
                l.callback !== null && l.lane !== 0 && (e.flags |= 64,
                g = o.effects,
                g === null ? o.effects = [l] : g.push(l))
            } else
                h = {
                    eventTime: h,
                    lane: g,
                    tag: l.tag,
                    payload: l.payload,
                    callback: l.callback,
                    next: null
                },
                d === null ? (u = d = h,
                c = f) : d = d.next = h,
                i |= g;
            if (l = l.next,
            l === null) {
                if (l = o.shared.pending,
                l === null)
                    break;
                g = l,
                l = g.next,
                g.next = null,
                o.lastBaseUpdate = g,
                o.shared.pending = null
            }
        } while (!0);
        if (d === null && (c = f),
        o.baseState = c,
        o.firstBaseUpdate = u,
        o.lastBaseUpdate = d,
        t = o.shared.interleaved,
        t !== null) {
            o = t;
            do
                i |= o.lane,
                o = o.next;
            while (o !== t)
        } else
            s === null && (o.shared.lanes = 0);
        qr |= i,
        e.lanes = i,
        e.memoizedState = f
    }
}
function Um(e, t, n) {
    if (e = t.effects,
    t.effects = null,
    e !== null)
        for (t = 0; t < e.length; t++) {
            var r = e[t]
              , o = r.callback;
            if (o !== null) {
                if (r.callback = null,
                r = n,
                typeof o != "function")
                    throw Error(_(191, o));
                o.call(r)
            }
        }
}
var Pa = {}
  , vn = jr(Pa)
  , ia = jr(Pa)
  , la = jr(Pa);
function Fr(e) {
    if (e === Pa)
        throw Error(_(174));
    return e
}
function Yd(e, t) {
    switch (ge(la, t),
    ge(ia, e),
    ge(vn, Pa),
    e = t.nodeType,
    e) {
    case 9:
    case 11:
        t = (t = t.documentElement) ? t.namespaceURI : ru(null, "");
        break;
    default:
        e = e === 8 ? t.parentNode : t,
        t = e.namespaceURI || null,
        e = e.tagName,
        t = ru(t, e)
    }
    Ne(vn),
    ge(vn, t)
}
function es() {
    Ne(vn),
    Ne(ia),
    Ne(la)
}
function Uv(e) {
    Fr(la.current);
    var t = Fr(vn.current)
      , n = ru(t, e.type);
    t !== n && (ge(ia, e),
    ge(vn, n))
}
function Kd(e) {
    ia.current === e && (Ne(vn),
    Ne(ia))
}
var ke = jr(0);
function Qi(e) {
    for (var t = e; t !== null; ) {
        if (t.tag === 13) {
            var n = t.memoizedState;
            if (n !== null && (n = n.dehydrated,
            n === null || n.data === "$?" || n.data === "$!"))
                return t
        } else if (t.tag === 19 && t.memoizedProps.revealOrder !== void 0) {
            if (t.flags & 128)
                return t
        } else if (t.child !== null) {
            t.child.return = t,
            t = t.child;
            continue
        }
        if (t === e)
            break;
        for (; t.sibling === null; ) {
            if (t.return === null || t.return === e)
                return null;
            t = t.return
        }
        t.sibling.return = t.return,
        t = t.sibling
    }
    return null
}
var yc = [];
function Qd() {
    for (var e = 0; e < yc.length; e++)
        yc[e]._workInProgressVersionPrimary = null;
    yc.length = 0
}
var xi = zn.ReactCurrentDispatcher
  , xc = zn.ReactCurrentBatchConfig
  , Gr = 0
  , Pe = null
  , Le = null
  , $e = null
  , Gi = !1
  , Us = !1
  , ca = 0
  , Lb = 0;
function Qe() {
    throw Error(_(321))
}
function Gd(e, t) {
    if (t === null)
        return !1;
    for (var n = 0; n < t.length && n < e.length; n++)
        if (!Jt(e[n], t[n]))
            return !1;
    return !0
}
function qd(e, t, n, r, o, s) {
    if (Gr = s,
    Pe = t,
    t.memoizedState = null,
    t.updateQueue = null,
    t.lanes = 0,
    xi.current = e === null || e.memoizedState === null ? Bb : Wb,
    e = n(r, o),
    Us) {
        s = 0;
        do {
            if (Us = !1,
            ca = 0,
            25 <= s)
                throw Error(_(301));
            s += 1,
            $e = Le = null,
            t.updateQueue = null,
            xi.current = Hb,
            e = n(r, o)
        } while (Us)
    }
    if (xi.current = qi,
    t = Le !== null && Le.next !== null,
    Gr = 0,
    $e = Le = Pe = null,
    Gi = !1,
    t)
        throw Error(_(300));
    return e
}
function Xd() {
    var e = ca !== 0;
    return ca = 0,
    e
}
function an() {
    var e = {
        memoizedState: null,
        baseState: null,
        baseQueue: null,
        queue: null,
        next: null
    };
    return $e === null ? Pe.memoizedState = $e = e : $e = $e.next = e,
    $e
}
function Ot() {
    if (Le === null) {
        var e = Pe.alternate;
        e = e !== null ? e.memoizedState : null
    } else
        e = Le.next;
    var t = $e === null ? Pe.memoizedState : $e.next;
    if (t !== null)
        $e = t,
        Le = e;
    else {
        if (e === null)
            throw Error(_(310));
        Le = e,
        e = {
            memoizedState: Le.memoizedState,
            baseState: Le.baseState,
            baseQueue: Le.baseQueue,
            queue: Le.queue,
            next: null
        },
        $e === null ? Pe.memoizedState = $e = e : $e = $e.next = e
    }
    return $e
}
function ua(e, t) {
    return typeof t == "function" ? t(e) : t
}
function wc(e) {
    var t = Ot()
      , n = t.queue;
    if (n === null)
        throw Error(_(311));
    n.lastRenderedReducer = e;
    var r = Le
      , o = r.baseQueue
      , s = n.pending;
    if (s !== null) {
        if (o !== null) {
            var i = o.next;
            o.next = s.next,
            s.next = i
        }
        r.baseQueue = o = s,
        n.pending = null
    }
    if (o !== null) {
        s = o.next,
        r = r.baseState;
        var l = i = null
          , c = null
          , u = s;
        do {
            var d = u.lane;
            if ((Gr & d) === d)
                c !== null && (c = c.next = {
                    lane: 0,
                    action: u.action,
                    hasEagerState: u.hasEagerState,
                    eagerState: u.eagerState,
                    next: null
                }),
                r = u.hasEagerState ? u.eagerState : e(r, u.action);
            else {
                var f = {
                    lane: d,
                    action: u.action,
                    hasEagerState: u.hasEagerState,
                    eagerState: u.eagerState,
                    next: null
                };
                c === null ? (l = c = f,
                i = r) : c = c.next = f,
                Pe.lanes |= d,
                qr |= d
            }
            u = u.next
        } while (u !== null && u !== s);
        c === null ? i = r : c.next = l,
        Jt(r, t.memoizedState) || (ct = !0),
        t.memoizedState = r,
        t.baseState = i,
        t.baseQueue = c,
        n.lastRenderedState = r
    }
    if (e = n.interleaved,
    e !== null) {
        o = e;
        do
            s = o.lane,
            Pe.lanes |= s,
            qr |= s,
            o = o.next;
        while (o !== e)
    } else
        o === null && (n.lanes = 0);
    return [t.memoizedState, n.dispatch]
}
function bc(e) {
    var t = Ot()
      , n = t.queue;
    if (n === null)
        throw Error(_(311));
    n.lastRenderedReducer = e;
    var r = n.dispatch
      , o = n.pending
      , s = t.memoizedState;
    if (o !== null) {
        n.pending = null;
        var i = o = o.next;
        do
            s = e(s, i.action),
            i = i.next;
        while (i !== o);
        Jt(s, t.memoizedState) || (ct = !0),
        t.memoizedState = s,
        t.baseQueue === null && (t.baseState = s),
        n.lastRenderedState = s
    }
    return [s, r]
}
function Yv() {}
function Kv(e, t) {
    var n = Pe
      , r = Ot()
      , o = t()
      , s = !Jt(r.memoizedState, o);
    if (s && (r.memoizedState = o,
    ct = !0),
    r = r.queue,
    Jd(qv.bind(null, n, r, e), [e]),
    r.getSnapshot !== t || s || $e !== null && $e.memoizedState.tag & 1) {
        if (n.flags |= 2048,
        da(9, Gv.bind(null, n, r, o, t), void 0, null),
        Be === null)
            throw Error(_(349));
        Gr & 30 || Qv(n, t, o)
    }
    return o
}
function Qv(e, t, n) {
    e.flags |= 16384,
    e = {
        getSnapshot: t,
        value: n
    },
    t = Pe.updateQueue,
    t === null ? (t = {
        lastEffect: null,
        stores: null
    },
    Pe.updateQueue = t,
    t.stores = [e]) : (n = t.stores,
    n === null ? t.stores = [e] : n.push(e))
}
function Gv(e, t, n, r) {
    t.value = n,
    t.getSnapshot = r,
    Xv(t) && Jv(e)
}
function qv(e, t, n) {
    return n(function() {
        Xv(t) && Jv(e)
    })
}
function Xv(e) {
    var t = e.getSnapshot;
    e = e.value;
    try {
        var n = t();
        return !Jt(e, n)
    } catch {
        return !0
    }
}
function Jv(e) {
    var t = An(e, 1);
    t !== null && qt(t, e, 1, -1)
}
function Ym(e) {
    var t = an();
    return typeof e == "function" && (e = e()),
    t.memoizedState = t.baseState = e,
    e = {
        pending: null,
        interleaved: null,
        lanes: 0,
        dispatch: null,
        lastRenderedReducer: ua,
        lastRenderedState: e
    },
    t.queue = e,
    e = e.dispatch = $b.bind(null, Pe, e),
    [t.memoizedState, e]
}
function da(e, t, n, r) {
    return e = {
        tag: e,
        create: t,
        destroy: n,
        deps: r,
        next: null
    },
    t = Pe.updateQueue,
    t === null ? (t = {
        lastEffect: null,
        stores: null
    },
    Pe.updateQueue = t,
    t.lastEffect = e.next = e) : (n = t.lastEffect,
    n === null ? t.lastEffect = e.next = e : (r = n.next,
    n.next = e,
    e.next = r,
    t.lastEffect = e)),
    e
}
function Zv() {
    return Ot().memoizedState
}
function wi(e, t, n, r) {
    var o = an();
    Pe.flags |= e,
    o.memoizedState = da(1 | t, n, void 0, r === void 0 ? null : r)
}
function Nl(e, t, n, r) {
    var o = Ot();
    r = r === void 0 ? null : r;
    var s = void 0;
    if (Le !== null) {
        var i = Le.memoizedState;
        if (s = i.destroy,
        r !== null && Gd(r, i.deps)) {
            o.memoizedState = da(t, n, s, r);
            return
        }
    }
    Pe.flags |= e,
    o.memoizedState = da(1 | t, n, s, r)
}
function Km(e, t) {
    return wi(8390656, 8, e, t)
}
function Jd(e, t) {
    return Nl(2048, 8, e, t)
}
function eg(e, t) {
    return Nl(4, 2, e, t)
}
function tg(e, t) {
    return Nl(4, 4, e, t)
}
function ng(e, t) {
    if (typeof t == "function")
        return e = e(),
        t(e),
        function() {
            t(null)
        }
        ;
    if (t != null)
        return e = e(),
        t.current = e,
        function() {
            t.current = null
        }
}
function rg(e, t, n) {
    return n = n != null ? n.concat([e]) : null,
    Nl(4, 4, ng.bind(null, t, e), n)
}
function Zd() {}
function og(e, t) {
    var n = Ot();
    t = t === void 0 ? null : t;
    var r = n.memoizedState;
    return r !== null && t !== null && Gd(t, r[1]) ? r[0] : (n.memoizedState = [e, t],
    e)
}
function sg(e, t) {
    var n = Ot();
    t = t === void 0 ? null : t;
    var r = n.memoizedState;
    return r !== null && t !== null && Gd(t, r[1]) ? r[0] : (e = e(),
    n.memoizedState = [e, t],
    e)
}
function ag(e, t, n) {
    return Gr & 21 ? (Jt(n, t) || (n = dv(),
    Pe.lanes |= n,
    qr |= n,
    e.baseState = !0),
    t) : (e.baseState && (e.baseState = !1,
    ct = !0),
    e.memoizedState = n)
}
function Fb(e, t) {
    var n = pe;
    pe = n !== 0 && 4 > n ? n : 4,
    e(!0);
    var r = xc.transition;
    xc.transition = {};
    try {
        e(!1),
        t()
    } finally {
        pe = n,
        xc.transition = r
    }
}
function ig() {
    return Ot().memoizedState
}
function zb(e, t, n) {
    var r = pr(e);
    if (n = {
        lane: r,
        action: n,
        hasEagerState: !1,
        eagerState: null,
        next: null
    },
    lg(e))
        cg(t, n);
    else if (n = Hv(e, t, n, r),
    n !== null) {
        var o = ot();
        qt(n, e, r, o),
        ug(n, t, r)
    }
}
function $b(e, t, n) {
    var r = pr(e)
      , o = {
        lane: r,
        action: n,
        hasEagerState: !1,
        eagerState: null,
        next: null
    };
    if (lg(e))
        cg(t, o);
    else {
        var s = e.alternate;
        if (e.lanes === 0 && (s === null || s.lanes === 0) && (s = t.lastRenderedReducer,
        s !== null))
            try {
                var i = t.lastRenderedState
                  , l = s(i, n);
                if (o.hasEagerState = !0,
                o.eagerState = l,
                Jt(l, i)) {
                    var c = t.interleaved;
                    c === null ? (o.next = o,
                    Vd(t)) : (o.next = c.next,
                    c.next = o),
                    t.interleaved = o;
                    return
                }
            } catch {} finally {}
        n = Hv(e, t, o, r),
        n !== null && (o = ot(),
        qt(n, e, r, o),
        ug(n, t, r))
    }
}
function lg(e) {
    var t = e.alternate;
    return e === Pe || t !== null && t === Pe
}
function cg(e, t) {
    Us = Gi = !0;
    var n = e.pending;
    n === null ? t.next = t : (t.next = n.next,
    n.next = t),
    e.pending = t
}
function ug(e, t, n) {
    if (n & 4194240) {
        var r = t.lanes;
        r &= e.pendingLanes,
        n |= r,
        t.lanes = n,
        Md(e, n)
    }
}
var qi = {
    readContext: Dt,
    useCallback: Qe,
    useContext: Qe,
    useEffect: Qe,
    useImperativeHandle: Qe,
    useInsertionEffect: Qe,
    useLayoutEffect: Qe,
    useMemo: Qe,
    useReducer: Qe,
    useRef: Qe,
    useState: Qe,
    useDebugValue: Qe,
    useDeferredValue: Qe,
    useTransition: Qe,
    useMutableSource: Qe,
    useSyncExternalStore: Qe,
    useId: Qe,
    unstable_isNewReconciler: !1
}
  , Bb = {
    readContext: Dt,
    useCallback: function(e, t) {
        return an().memoizedState = [e, t === void 0 ? null : t],
        e
    },
    useContext: Dt,
    useEffect: Km,
    useImperativeHandle: function(e, t, n) {
        return n = n != null ? n.concat([e]) : null,
        wi(4194308, 4, ng.bind(null, t, e), n)
    },
    useLayoutEffect: function(e, t) {
        return wi(4194308, 4, e, t)
    },
    useInsertionEffect: function(e, t) {
        return wi(4, 2, e, t)
    },
    useMemo: function(e, t) {
        var n = an();
        return t = t === void 0 ? null : t,
        e = e(),
        n.memoizedState = [e, t],
        e
    },
    useReducer: function(e, t, n) {
        var r = an();
        return t = n !== void 0 ? n(t) : t,
        r.memoizedState = r.baseState = t,
        e = {
            pending: null,
            interleaved: null,
            lanes: 0,
            dispatch: null,
            lastRenderedReducer: e,
            lastRenderedState: t
        },
        r.queue = e,
        e = e.dispatch = zb.bind(null, Pe, e),
        [r.memoizedState, e]
    },
    useRef: function(e) {
        var t = an();
        return e = {
            current: e
        },
        t.memoizedState = e
    },
    useState: Ym,
    useDebugValue: Zd,
    useDeferredValue: function(e) {
        return an().memoizedState = e
    },
    useTransition: function() {
        var e = Ym(!1)
          , t = e[0];
        return e = Fb.bind(null, e[1]),
        an().memoizedState = e,
        [t, e]
    },
    useMutableSource: function() {},
    useSyncExternalStore: function(e, t, n) {
        var r = Pe
          , o = an();
        if (je) {
            if (n === void 0)
                throw Error(_(407));
            n = n()
        } else {
            if (n = t(),
            Be === null)
                throw Error(_(349));
            Gr & 30 || Qv(r, t, n)
        }
        o.memoizedState = n;
        var s = {
            value: n,
            getSnapshot: t
        };
        return o.queue = s,
        Km(qv.bind(null, r, s, e), [e]),
        r.flags |= 2048,
        da(9, Gv.bind(null, r, s, n, t), void 0, null),
        n
    },
    useId: function() {
        var e = an()
          , t = Be.identifierPrefix;
        if (je) {
            var n = Mn
              , r = Tn;
            n = (r & ~(1 << 32 - Gt(r) - 1)).toString(32) + n,
            t = ":" + t + "R" + n,
            n = ca++,
            0 < n && (t += "H" + n.toString(32)),
            t += ":"
        } else
            n = Lb++,
            t = ":" + t + "r" + n.toString(32) + ":";
        return e.memoizedState = t
    },
    unstable_isNewReconciler: !1
}
  , Wb = {
    readContext: Dt,
    useCallback: og,
    useContext: Dt,
    useEffect: Jd,
    useImperativeHandle: rg,
    useInsertionEffect: eg,
    useLayoutEffect: tg,
    useMemo: sg,
    useReducer: wc,
    useRef: Zv,
    useState: function() {
        return wc(ua)
    },
    useDebugValue: Zd,
    useDeferredValue: function(e) {
        var t = Ot();
        return ag(t, Le.memoizedState, e)
    },
    useTransition: function() {
        var e = wc(ua)[0]
          , t = Ot().memoizedState;
        return [e, t]
    },
    useMutableSource: Yv,
    useSyncExternalStore: Kv,
    useId: ig,
    unstable_isNewReconciler: !1
}
  , Hb = {
    readContext: Dt,
    useCallback: og,
    useContext: Dt,
    useEffect: Jd,
    useImperativeHandle: rg,
    useInsertionEffect: eg,
    useLayoutEffect: tg,
    useMemo: sg,
    useReducer: bc,
    useRef: Zv,
    useState: function() {
        return bc(ua)
    },
    useDebugValue: Zd,
    useDeferredValue: function(e) {
        var t = Ot();
        return Le === null ? t.memoizedState = e : ag(t, Le.memoizedState, e)
    },
    useTransition: function() {
        var e = bc(ua)[0]
          , t = Ot().memoizedState;
        return [e, t]
    },
    useMutableSource: Yv,
    useSyncExternalStore: Kv,
    useId: ig,
    unstable_isNewReconciler: !1
};
function Bt(e, t) {
    if (e && e.defaultProps) {
        t = Te({}, t),
        e = e.defaultProps;
        for (var n in e)
            t[n] === void 0 && (t[n] = e[n]);
        return t
    }
    return t
}
function ju(e, t, n, r) {
    t = e.memoizedState,
    n = n(r, t),
    n = n == null ? t : Te({}, t, n),
    e.memoizedState = n,
    e.lanes === 0 && (e.updateQueue.baseState = n)
}
var Sl = {
    isMounted: function(e) {
        return (e = e._reactInternals) ? so(e) === e : !1
    },
    enqueueSetState: function(e, t, n) {
        e = e._reactInternals;
        var r = ot()
          , o = pr(e)
          , s = Rn(r, o);
        s.payload = t,
        n != null && (s.callback = n),
        t = mr(e, s, o),
        t !== null && (qt(t, e, o, r),
        yi(t, e, o))
    },
    enqueueReplaceState: function(e, t, n) {
        e = e._reactInternals;
        var r = ot()
          , o = pr(e)
          , s = Rn(r, o);
        s.tag = 1,
        s.payload = t,
        n != null && (s.callback = n),
        t = mr(e, s, o),
        t !== null && (qt(t, e, o, r),
        yi(t, e, o))
    },
    enqueueForceUpdate: function(e, t) {
        e = e._reactInternals;
        var n = ot()
          , r = pr(e)
          , o = Rn(n, r);
        o.tag = 2,
        t != null && (o.callback = t),
        t = mr(e, o, r),
        t !== null && (qt(t, e, r, n),
        yi(t, e, r))
    }
};
function Qm(e, t, n, r, o, s, i) {
    return e = e.stateNode,
    typeof e.shouldComponentUpdate == "function" ? e.shouldComponentUpdate(r, s, i) : t.prototype && t.prototype.isPureReactComponent ? !ra(n, r) || !ra(o, s) : !0
}
function dg(e, t, n) {
    var r = !1
      , o = xr
      , s = t.contextType;
    return typeof s == "object" && s !== null ? s = Dt(s) : (o = ft(t) ? Kr : Je.current,
    r = t.contextTypes,
    s = (r = r != null) ? Xo(e, o) : xr),
    t = new t(n,s),
    e.memoizedState = t.state !== null && t.state !== void 0 ? t.state : null,
    t.updater = Sl,
    e.stateNode = t,
    t._reactInternals = e,
    r && (e = e.stateNode,
    e.__reactInternalMemoizedUnmaskedChildContext = o,
    e.__reactInternalMemoizedMaskedChildContext = s),
    t
}
function Gm(e, t, n, r) {
    e = t.state,
    typeof t.componentWillReceiveProps == "function" && t.componentWillReceiveProps(n, r),
    typeof t.UNSAFE_componentWillReceiveProps == "function" && t.UNSAFE_componentWillReceiveProps(n, r),
    t.state !== e && Sl.enqueueReplaceState(t, t.state, null)
}
function Cu(e, t, n, r) {
    var o = e.stateNode;
    o.props = n,
    o.state = e.memoizedState,
    o.refs = {},
    Ud(e);
    var s = t.contextType;
    typeof s == "object" && s !== null ? o.context = Dt(s) : (s = ft(t) ? Kr : Je.current,
    o.context = Xo(e, s)),
    o.state = e.memoizedState,
    s = t.getDerivedStateFromProps,
    typeof s == "function" && (ju(e, t, s, n),
    o.state = e.memoizedState),
    typeof t.getDerivedStateFromProps == "function" || typeof o.getSnapshotBeforeUpdate == "function" || typeof o.UNSAFE_componentWillMount != "function" && typeof o.componentWillMount != "function" || (t = o.state,
    typeof o.componentWillMount == "function" && o.componentWillMount(),
    typeof o.UNSAFE_componentWillMount == "function" && o.UNSAFE_componentWillMount(),
    t !== o.state && Sl.enqueueReplaceState(o, o.state, null),
    Ki(e, n, o, r),
    o.state = e.memoizedState),
    typeof o.componentDidMount == "function" && (e.flags |= 4194308)
}
function ts(e, t) {
    try {
        var n = ""
          , r = t;
        do
            n += g1(r),
            r = r.return;
        while (r);
        var o = n
    } catch (s) {
        o = `
Error generating stack: ` + s.message + `
` + s.stack
    }
    return {
        value: e,
        source: t,
        stack: o,
        digest: null
    }
}
function Nc(e, t, n) {
    return {
        value: e,
        source: null,
        stack: n ?? null,
        digest: t ?? null
    }
}
function ku(e, t) {
    try {
        console.error(t.value)
    } catch (n) {
        setTimeout(function() {
            throw n
        })
    }
}
var Vb = typeof WeakMap == "function" ? WeakMap : Map;
function fg(e, t, n) {
    n = Rn(-1, n),
    n.tag = 3,
    n.payload = {
        element: null
    };
    var r = t.value;
    return n.callback = function() {
        Ji || (Ji = !0,
        Iu = r),
        ku(e, t)
    }
    ,
    n
}
function mg(e, t, n) {
    n = Rn(-1, n),
    n.tag = 3;
    var r = e.type.getDerivedStateFromError;
    if (typeof r == "function") {
        var o = t.value;
        n.payload = function() {
            return r(o)
        }
        ,
        n.callback = function() {
            ku(e, t)
        }
    }
    var s = e.stateNode;
    return s !== null && typeof s.componentDidCatch == "function" && (n.callback = function() {
        ku(e, t),
        typeof r != "function" && (hr === null ? hr = new Set([this]) : hr.add(this));
        var i = t.stack;
        this.componentDidCatch(t.value, {
            componentStack: i !== null ? i : ""
        })
    }
    ),
    n
}
function qm(e, t, n) {
    var r = e.pingCache;
    if (r === null) {
        r = e.pingCache = new Vb;
        var o = new Set;
        r.set(t, o)
    } else
        o = r.get(t),
        o === void 0 && (o = new Set,
        r.set(t, o));
    o.has(n) || (o.add(n),
    e = oN.bind(null, e, t, n),
    t.then(e, e))
}
function Xm(e) {
    do {
        var t;
        if ((t = e.tag === 13) && (t = e.memoizedState,
        t = t !== null ? t.dehydrated !== null : !0),
        t)
            return e;
        e = e.return
    } while (e !== null);
    return null
}
function Jm(e, t, n, r, o) {
    return e.mode & 1 ? (e.flags |= 65536,
    e.lanes = o,
    e) : (e === t ? e.flags |= 65536 : (e.flags |= 128,
    n.flags |= 131072,
    n.flags &= -52805,
    n.tag === 1 && (n.alternate === null ? n.tag = 17 : (t = Rn(-1, 1),
    t.tag = 2,
    mr(n, t, 1))),
    n.lanes |= 1),
    e)
}
var Ub = zn.ReactCurrentOwner
  , ct = !1;
function et(e, t, n, r) {
    t.child = e === null ? Wv(t, null, n, r) : Zo(t, e.child, n, r)
}
function Zm(e, t, n, r, o) {
    n = n.render;
    var s = t.ref;
    return Io(t, o),
    r = qd(e, t, n, r, s, o),
    n = Xd(),
    e !== null && !ct ? (t.updateQueue = e.updateQueue,
    t.flags &= -2053,
    e.lanes &= ~o,
    In(e, t, o)) : (je && n && Fd(t),
    t.flags |= 1,
    et(e, t, r, o),
    t.child)
}
function eh(e, t, n, r, o) {
    if (e === null) {
        var s = n.type;
        return typeof s == "function" && !lf(s) && s.defaultProps === void 0 && n.compare === null && n.defaultProps === void 0 ? (t.tag = 15,
        t.type = s,
        hg(e, t, s, r, o)) : (e = ji(n.type, null, r, t, t.mode, o),
        e.ref = t.ref,
        e.return = t,
        t.child = e)
    }
    if (s = e.child,
    !(e.lanes & o)) {
        var i = s.memoizedProps;
        if (n = n.compare,
        n = n !== null ? n : ra,
        n(i, r) && e.ref === t.ref)
            return In(e, t, o)
    }
    return t.flags |= 1,
    e = vr(s, r),
    e.ref = t.ref,
    e.return = t,
    t.child = e
}
function hg(e, t, n, r, o) {
    if (e !== null) {
        var s = e.memoizedProps;
        if (ra(s, r) && e.ref === t.ref)
            if (ct = !1,
            t.pendingProps = r = s,
            (e.lanes & o) !== 0)
                e.flags & 131072 && (ct = !0);
            else
                return t.lanes = e.lanes,
                In(e, t, o)
    }
    return Eu(e, t, n, r, o)
}
function pg(e, t, n) {
    var r = t.pendingProps
      , o = r.children
      , s = e !== null ? e.memoizedState : null;
    if (r.mode === "hidden")
        if (!(t.mode & 1))
            t.memoizedState = {
                baseLanes: 0,
                cachePool: null,
                transitions: null
            },
            ge(Ro, pt),
            pt |= n;
        else {
            if (!(n & 1073741824))
                return e = s !== null ? s.baseLanes | n : n,
                t.lanes = t.childLanes = 1073741824,
                t.memoizedState = {
                    baseLanes: e,
                    cachePool: null,
                    transitions: null
                },
                t.updateQueue = null,
                ge(Ro, pt),
                pt |= e,
                null;
            t.memoizedState = {
                baseLanes: 0,
                cachePool: null,
                transitions: null
            },
            r = s !== null ? s.baseLanes : n,
            ge(Ro, pt),
            pt |= r
        }
    else
        s !== null ? (r = s.baseLanes | n,
        t.memoizedState = null) : r = n,
        ge(Ro, pt),
        pt |= r;
    return et(e, t, o, n),
    t.child
}
function vg(e, t) {
    var n = t.ref;
    (e === null && n !== null || e !== null && e.ref !== n) && (t.flags |= 512,
    t.flags |= 2097152)
}
function Eu(e, t, n, r, o) {
    var s = ft(n) ? Kr : Je.current;
    return s = Xo(t, s),
    Io(t, o),
    n = qd(e, t, n, r, s, o),
    r = Xd(),
    e !== null && !ct ? (t.updateQueue = e.updateQueue,
    t.flags &= -2053,
    e.lanes &= ~o,
    In(e, t, o)) : (je && r && Fd(t),
    t.flags |= 1,
    et(e, t, n, o),
    t.child)
}
function th(e, t, n, r, o) {
    if (ft(n)) {
        var s = !0;
        Wi(t)
    } else
        s = !1;
    if (Io(t, o),
    t.stateNode === null)
        bi(e, t),
        dg(t, n, r),
        Cu(t, n, r, o),
        r = !0;
    else if (e === null) {
        var i = t.stateNode
          , l = t.memoizedProps;
        i.props = l;
        var c = i.context
          , u = n.contextType;
        typeof u == "object" && u !== null ? u = Dt(u) : (u = ft(n) ? Kr : Je.current,
        u = Xo(t, u));
        var d = n.getDerivedStateFromProps
          , f = typeof d == "function" || typeof i.getSnapshotBeforeUpdate == "function";
        f || typeof i.UNSAFE_componentWillReceiveProps != "function" && typeof i.componentWillReceiveProps != "function" || (l !== r || c !== u) && Gm(t, i, r, u),
        Xn = !1;
        var g = t.memoizedState;
        i.state = g,
        Ki(t, r, i, o),
        c = t.memoizedState,
        l !== r || g !== c || dt.current || Xn ? (typeof d == "function" && (ju(t, n, d, r),
        c = t.memoizedState),
        (l = Xn || Qm(t, n, l, r, g, c, u)) ? (f || typeof i.UNSAFE_componentWillMount != "function" && typeof i.componentWillMount != "function" || (typeof i.componentWillMount == "function" && i.componentWillMount(),
        typeof i.UNSAFE_componentWillMount == "function" && i.UNSAFE_componentWillMount()),
        typeof i.componentDidMount == "function" && (t.flags |= 4194308)) : (typeof i.componentDidMount == "function" && (t.flags |= 4194308),
        t.memoizedProps = r,
        t.memoizedState = c),
        i.props = r,
        i.state = c,
        i.context = u,
        r = l) : (typeof i.componentDidMount == "function" && (t.flags |= 4194308),
        r = !1)
    } else {
        i = t.stateNode,
        Vv(e, t),
        l = t.memoizedProps,
        u = t.type === t.elementType ? l : Bt(t.type, l),
        i.props = u,
        f = t.pendingProps,
        g = i.context,
        c = n.contextType,
        typeof c == "object" && c !== null ? c = Dt(c) : (c = ft(n) ? Kr : Je.current,
        c = Xo(t, c));
        var h = n.getDerivedStateFromProps;
        (d = typeof h == "function" || typeof i.getSnapshotBeforeUpdate == "function") || typeof i.UNSAFE_componentWillReceiveProps != "function" && typeof i.componentWillReceiveProps != "function" || (l !== f || g !== c) && Gm(t, i, r, c),
        Xn = !1,
        g = t.memoizedState,
        i.state = g,
        Ki(t, r, i, o);
        var b = t.memoizedState;
        l !== f || g !== b || dt.current || Xn ? (typeof h == "function" && (ju(t, n, h, r),
        b = t.memoizedState),
        (u = Xn || Qm(t, n, u, r, g, b, c) || !1) ? (d || typeof i.UNSAFE_componentWillUpdate != "function" && typeof i.componentWillUpdate != "function" || (typeof i.componentWillUpdate == "function" && i.componentWillUpdate(r, b, c),
        typeof i.UNSAFE_componentWillUpdate == "function" && i.UNSAFE_componentWillUpdate(r, b, c)),
        typeof i.componentDidUpdate == "function" && (t.flags |= 4),
        typeof i.getSnapshotBeforeUpdate == "function" && (t.flags |= 1024)) : (typeof i.componentDidUpdate != "function" || l === e.memoizedProps && g === e.memoizedState || (t.flags |= 4),
        typeof i.getSnapshotBeforeUpdate != "function" || l === e.memoizedProps && g === e.memoizedState || (t.flags |= 1024),
        t.memoizedProps = r,
        t.memoizedState = b),
        i.props = r,
        i.state = b,
        i.context = c,
        r = u) : (typeof i.componentDidUpdate != "function" || l === e.memoizedProps && g === e.memoizedState || (t.flags |= 4),
        typeof i.getSnapshotBeforeUpdate != "function" || l === e.memoizedProps && g === e.memoizedState || (t.flags |= 1024),
        r = !1)
    }
    return Pu(e, t, n, r, s, o)
}
function Pu(e, t, n, r, o, s) {
    vg(e, t);
    var i = (t.flags & 128) !== 0;
    if (!r && !i)
        return o && $m(t, n, !1),
        In(e, t, s);
    r = t.stateNode,
    Ub.current = t;
    var l = i && typeof n.getDerivedStateFromError != "function" ? null : r.render();
    return t.flags |= 1,
    e !== null && i ? (t.child = Zo(t, e.child, null, s),
    t.child = Zo(t, null, l, s)) : et(e, t, l, s),
    t.memoizedState = r.state,
    o && $m(t, n, !0),
    t.child
}
function gg(e) {
    var t = e.stateNode;
    t.pendingContext ? zm(e, t.pendingContext, t.pendingContext !== t.context) : t.context && zm(e, t.context, !1),
    Yd(e, t.containerInfo)
}
function nh(e, t, n, r, o) {
    return Jo(),
    $d(o),
    t.flags |= 256,
    et(e, t, n, r),
    t.child
}
var Tu = {
    dehydrated: null,
    treeContext: null,
    retryLane: 0
};
function Mu(e) {
    return {
        baseLanes: e,
        cachePool: null,
        transitions: null
    }
}
function yg(e, t, n) {
    var r = t.pendingProps, o = ke.current, s = !1, i = (t.flags & 128) !== 0, l;
    if ((l = i) || (l = e !== null && e.memoizedState === null ? !1 : (o & 2) !== 0),
    l ? (s = !0,
    t.flags &= -129) : (e === null || e.memoizedState !== null) && (o |= 1),
    ge(ke, o & 1),
    e === null)
        return Nu(t),
        e = t.memoizedState,
        e !== null && (e = e.dehydrated,
        e !== null) ? (t.mode & 1 ? e.data === "$!" ? t.lanes = 8 : t.lanes = 1073741824 : t.lanes = 1,
        null) : (i = r.children,
        e = r.fallback,
        s ? (r = t.mode,
        s = t.child,
        i = {
            mode: "hidden",
            children: i
        },
        !(r & 1) && s !== null ? (s.childLanes = 0,
        s.pendingProps = i) : s = kl(i, r, 0, null),
        e = Yr(e, r, n, null),
        s.return = t,
        e.return = t,
        s.sibling = e,
        t.child = s,
        t.child.memoizedState = Mu(n),
        t.memoizedState = Tu,
        e) : ef(t, i));
    if (o = e.memoizedState,
    o !== null && (l = o.dehydrated,
    l !== null))
        return Yb(e, t, i, r, l, o, n);
    if (s) {
        s = r.fallback,
        i = t.mode,
        o = e.child,
        l = o.sibling;
        var c = {
            mode: "hidden",
            children: r.children
        };
        return !(i & 1) && t.child !== o ? (r = t.child,
        r.childLanes = 0,
        r.pendingProps = c,
        t.deletions = null) : (r = vr(o, c),
        r.subtreeFlags = o.subtreeFlags & 14680064),
        l !== null ? s = vr(l, s) : (s = Yr(s, i, n, null),
        s.flags |= 2),
        s.return = t,
        r.return = t,
        r.sibling = s,
        t.child = r,
        r = s,
        s = t.child,
        i = e.child.memoizedState,
        i = i === null ? Mu(n) : {
            baseLanes: i.baseLanes | n,
            cachePool: null,
            transitions: i.transitions
        },
        s.memoizedState = i,
        s.childLanes = e.childLanes & ~n,
        t.memoizedState = Tu,
        r
    }
    return s = e.child,
    e = s.sibling,
    r = vr(s, {
        mode: "visible",
        children: r.children
    }),
    !(t.mode & 1) && (r.lanes = n),
    r.return = t,
    r.sibling = null,
    e !== null && (n = t.deletions,
    n === null ? (t.deletions = [e],
    t.flags |= 16) : n.push(e)),
    t.child = r,
    t.memoizedState = null,
    r
}
function ef(e, t) {
    return t = kl({
        mode: "visible",
        children: t
    }, e.mode, 0, null),
    t.return = e,
    e.child = t
}
function ei(e, t, n, r) {
    return r !== null && $d(r),
    Zo(t, e.child, null, n),
    e = ef(t, t.pendingProps.children),
    e.flags |= 2,
    t.memoizedState = null,
    e
}
function Yb(e, t, n, r, o, s, i) {
    if (n)
        return t.flags & 256 ? (t.flags &= -257,
        r = Nc(Error(_(422))),
        ei(e, t, i, r)) : t.memoizedState !== null ? (t.child = e.child,
        t.flags |= 128,
        null) : (s = r.fallback,
        o = t.mode,
        r = kl({
            mode: "visible",
            children: r.children
        }, o, 0, null),
        s = Yr(s, o, i, null),
        s.flags |= 2,
        r.return = t,
        s.return = t,
        r.sibling = s,
        t.child = r,
        t.mode & 1 && Zo(t, e.child, null, i),
        t.child.memoizedState = Mu(i),
        t.memoizedState = Tu,
        s);
    if (!(t.mode & 1))
        return ei(e, t, i, null);
    if (o.data === "$!") {
        if (r = o.nextSibling && o.nextSibling.dataset,
        r)
            var l = r.dgst;
        return r = l,
        s = Error(_(419)),
        r = Nc(s, r, void 0),
        ei(e, t, i, r)
    }
    if (l = (i & e.childLanes) !== 0,
    ct || l) {
        if (r = Be,
        r !== null) {
            switch (i & -i) {
            case 4:
                o = 2;
                break;
            case 16:
                o = 8;
                break;
            case 64:
            case 128:
            case 256:
            case 512:
            case 1024:
            case 2048:
            case 4096:
            case 8192:
            case 16384:
            case 32768:
            case 65536:
            case 131072:
            case 262144:
            case 524288:
            case 1048576:
            case 2097152:
            case 4194304:
            case 8388608:
            case 16777216:
            case 33554432:
            case 67108864:
                o = 32;
                break;
            case 536870912:
                o = 268435456;
                break;
            default:
                o = 0
            }
            o = o & (r.suspendedLanes | i) ? 0 : o,
            o !== 0 && o !== s.retryLane && (s.retryLane = o,
            An(e, o),
            qt(r, e, o, -1))
        }
        return af(),
        r = Nc(Error(_(421))),
        ei(e, t, i, r)
    }
    return o.data === "$?" ? (t.flags |= 128,
    t.child = e.child,
    t = sN.bind(null, e),
    o._reactRetry = t,
    null) : (e = s.treeContext,
    gt = fr(o.nextSibling),
    yt = t,
    je = !0,
    Yt = null,
    e !== null && (Et[Pt++] = Tn,
    Et[Pt++] = Mn,
    Et[Pt++] = Qr,
    Tn = e.id,
    Mn = e.overflow,
    Qr = t),
    t = ef(t, r.children),
    t.flags |= 4096,
    t)
}
function rh(e, t, n) {
    e.lanes |= t;
    var r = e.alternate;
    r !== null && (r.lanes |= t),
    Su(e.return, t, n)
}
function Sc(e, t, n, r, o) {
    var s = e.memoizedState;
    s === null ? e.memoizedState = {
        isBackwards: t,
        rendering: null,
        renderingStartTime: 0,
        last: r,
        tail: n,
        tailMode: o
    } : (s.isBackwards = t,
    s.rendering = null,
    s.renderingStartTime = 0,
    s.last = r,
    s.tail = n,
    s.tailMode = o)
}
function xg(e, t, n) {
    var r = t.pendingProps
      , o = r.revealOrder
      , s = r.tail;
    if (et(e, t, r.children, n),
    r = ke.current,
    r & 2)
        r = r & 1 | 2,
        t.flags |= 128;
    else {
        if (e !== null && e.flags & 128)
            e: for (e = t.child; e !== null; ) {
                if (e.tag === 13)
                    e.memoizedState !== null && rh(e, n, t);
                else if (e.tag === 19)
                    rh(e, n, t);
                else if (e.child !== null) {
                    e.child.return = e,
                    e = e.child;
                    continue
                }
                if (e === t)
                    break e;
                for (; e.sibling === null; ) {
                    if (e.return === null || e.return === t)
                        break e;
                    e = e.return
                }
                e.sibling.return = e.return,
                e = e.sibling
            }
        r &= 1
    }
    if (ge(ke, r),
    !(t.mode & 1))
        t.memoizedState = null;
    else
        switch (o) {
        case "forwards":
            for (n = t.child,
            o = null; n !== null; )
                e = n.alternate,
                e !== null && Qi(e) === null && (o = n),
                n = n.sibling;
            n = o,
            n === null ? (o = t.child,
            t.child = null) : (o = n.sibling,
            n.sibling = null),
            Sc(t, !1, o, n, s);
            break;
        case "backwards":
            for (n = null,
            o = t.child,
            t.child = null; o !== null; ) {
                if (e = o.alternate,
                e !== null && Qi(e) === null) {
                    t.child = o;
                    break
                }
                e = o.sibling,
                o.sibling = n,
                n = o,
                o = e
            }
            Sc(t, !0, n, null, s);
            break;
        case "together":
            Sc(t, !1, null, null, void 0);
            break;
        default:
            t.memoizedState = null
        }
    return t.child
}
function bi(e, t) {
    !(t.mode & 1) && e !== null && (e.alternate = null,
    t.alternate = null,
    t.flags |= 2)
}
function In(e, t, n) {
    if (e !== null && (t.dependencies = e.dependencies),
    qr |= t.lanes,
    !(n & t.childLanes))
        return null;
    if (e !== null && t.child !== e.child)
        throw Error(_(153));
    if (t.child !== null) {
        for (e = t.child,
        n = vr(e, e.pendingProps),
        t.child = n,
        n.return = t; e.sibling !== null; )
            e = e.sibling,
            n = n.sibling = vr(e, e.pendingProps),
            n.return = t;
        n.sibling = null
    }
    return t.child
}
function Kb(e, t, n) {
    switch (t.tag) {
    case 3:
        gg(t),
        Jo();
        break;
    case 5:
        Uv(t);
        break;
    case 1:
        ft(t.type) && Wi(t);
        break;
    case 4:
        Yd(t, t.stateNode.containerInfo);
        break;
    case 10:
        var r = t.type._context
          , o = t.memoizedProps.value;
        ge(Ui, r._currentValue),
        r._currentValue = o;
        break;
    case 13:
        if (r = t.memoizedState,
        r !== null)
            return r.dehydrated !== null ? (ge(ke, ke.current & 1),
            t.flags |= 128,
            null) : n & t.child.childLanes ? yg(e, t, n) : (ge(ke, ke.current & 1),
            e = In(e, t, n),
            e !== null ? e.sibling : null);
        ge(ke, ke.current & 1);
        break;
    case 19:
        if (r = (n & t.childLanes) !== 0,
        e.flags & 128) {
            if (r)
                return xg(e, t, n);
            t.flags |= 128
        }
        if (o = t.memoizedState,
        o !== null && (o.rendering = null,
        o.tail = null,
        o.lastEffect = null),
        ge(ke, ke.current),
        r)
            break;
        return null;
    case 22:
    case 23:
        return t.lanes = 0,
        pg(e, t, n)
    }
    return In(e, t, n)
}
var wg, Ru, bg, Ng;
wg = function(e, t) {
    for (var n = t.child; n !== null; ) {
        if (n.tag === 5 || n.tag === 6)
            e.appendChild(n.stateNode);
        else if (n.tag !== 4 && n.child !== null) {
            n.child.return = n,
            n = n.child;
            continue
        }
        if (n === t)
            break;
        for (; n.sibling === null; ) {
            if (n.return === null || n.return === t)
                return;
            n = n.return
        }
        n.sibling.return = n.return,
        n = n.sibling
    }
}
;
Ru = function() {}
;
bg = function(e, t, n, r) {
    var o = e.memoizedProps;
    if (o !== r) {
        e = t.stateNode,
        Fr(vn.current);
        var s = null;
        switch (n) {
        case "input":
            o = Zc(e, o),
            r = Zc(e, r),
            s = [];
            break;
        case "select":
            o = Te({}, o, {
                value: void 0
            }),
            r = Te({}, r, {
                value: void 0
            }),
            s = [];
            break;
        case "textarea":
            o = nu(e, o),
            r = nu(e, r),
            s = [];
            break;
        default:
            typeof o.onClick != "function" && typeof r.onClick == "function" && (e.onclick = $i)
        }
        ou(n, r);
        var i;
        n = null;
        for (u in o)
            if (!r.hasOwnProperty(u) && o.hasOwnProperty(u) && o[u] != null)
                if (u === "style") {
                    var l = o[u];
                    for (i in l)
                        l.hasOwnProperty(i) && (n || (n = {}),
                        n[i] = "")
                } else
                    u !== "dangerouslySetInnerHTML" && u !== "children" && u !== "suppressContentEditableWarning" && u !== "suppressHydrationWarning" && u !== "autoFocus" && (qs.hasOwnProperty(u) ? s || (s = []) : (s = s || []).push(u, null));
        for (u in r) {
            var c = r[u];
            if (l = o != null ? o[u] : void 0,
            r.hasOwnProperty(u) && c !== l && (c != null || l != null))
                if (u === "style")
                    if (l) {
                        for (i in l)
                            !l.hasOwnProperty(i) || c && c.hasOwnProperty(i) || (n || (n = {}),
                            n[i] = "");
                        for (i in c)
                            c.hasOwnProperty(i) && l[i] !== c[i] && (n || (n = {}),
                            n[i] = c[i])
                    } else
                        n || (s || (s = []),
                        s.push(u, n)),
                        n = c;
                else
                    u === "dangerouslySetInnerHTML" ? (c = c ? c.__html : void 0,
                    l = l ? l.__html : void 0,
                    c != null && l !== c && (s = s || []).push(u, c)) : u === "children" ? typeof c != "string" && typeof c != "number" || (s = s || []).push(u, "" + c) : u !== "suppressContentEditableWarning" && u !== "suppressHydrationWarning" && (qs.hasOwnProperty(u) ? (c != null && u === "onScroll" && be("scroll", e),
                    s || l === c || (s = [])) : (s = s || []).push(u, c))
        }
        n && (s = s || []).push("style", n);
        var u = s;
        (t.updateQueue = u) && (t.flags |= 4)
    }
}
;
Ng = function(e, t, n, r) {
    n !== r && (t.flags |= 4)
}
;
function Ts(e, t) {
    if (!je)
        switch (e.tailMode) {
        case "hidden":
            t = e.tail;
            for (var n = null; t !== null; )
                t.alternate !== null && (n = t),
                t = t.sibling;
            n === null ? e.tail = null : n.sibling = null;
            break;
        case "collapsed":
            n = e.tail;
            for (var r = null; n !== null; )
                n.alternate !== null && (r = n),
                n = n.sibling;
            r === null ? t || e.tail === null ? e.tail = null : e.tail.sibling = null : r.sibling = null
        }
}
function Ge(e) {
    var t = e.alternate !== null && e.alternate.child === e.child
      , n = 0
      , r = 0;
    if (t)
        for (var o = e.child; o !== null; )
            n |= o.lanes | o.childLanes,
            r |= o.subtreeFlags & 14680064,
            r |= o.flags & 14680064,
            o.return = e,
            o = o.sibling;
    else
        for (o = e.child; o !== null; )
            n |= o.lanes | o.childLanes,
            r |= o.subtreeFlags,
            r |= o.flags,
            o.return = e,
            o = o.sibling;
    return e.subtreeFlags |= r,
    e.childLanes = n,
    t
}
function Qb(e, t, n) {
    var r = t.pendingProps;
    switch (zd(t),
    t.tag) {
    case 2:
    case 16:
    case 15:
    case 0:
    case 11:
    case 7:
    case 8:
    case 12:
    case 9:
    case 14:
        return Ge(t),
        null;
    case 1:
        return ft(t.type) && Bi(),
        Ge(t),
        null;
    case 3:
        return r = t.stateNode,
        es(),
        Ne(dt),
        Ne(Je),
        Qd(),
        r.pendingContext && (r.context = r.pendingContext,
        r.pendingContext = null),
        (e === null || e.child === null) && (Ja(t) ? t.flags |= 4 : e === null || e.memoizedState.isDehydrated && !(t.flags & 256) || (t.flags |= 1024,
        Yt !== null && (zu(Yt),
        Yt = null))),
        Ru(e, t),
        Ge(t),
        null;
    case 5:
        Kd(t);
        var o = Fr(la.current);
        if (n = t.type,
        e !== null && t.stateNode != null)
            bg(e, t, n, r, o),
            e.ref !== t.ref && (t.flags |= 512,
            t.flags |= 2097152);
        else {
            if (!r) {
                if (t.stateNode === null)
                    throw Error(_(166));
                return Ge(t),
                null
            }
            if (e = Fr(vn.current),
            Ja(t)) {
                r = t.stateNode,
                n = t.type;
                var s = t.memoizedProps;
                switch (r[dn] = t,
                r[aa] = s,
                e = (t.mode & 1) !== 0,
                n) {
                case "dialog":
                    be("cancel", r),
                    be("close", r);
                    break;
                case "iframe":
                case "object":
                case "embed":
                    be("load", r);
                    break;
                case "video":
                case "audio":
                    for (o = 0; o < Fs.length; o++)
                        be(Fs[o], r);
                    break;
                case "source":
                    be("error", r);
                    break;
                case "img":
                case "image":
                case "link":
                    be("error", r),
                    be("load", r);
                    break;
                case "details":
                    be("toggle", r);
                    break;
                case "input":
                    fm(r, s),
                    be("invalid", r);
                    break;
                case "select":
                    r._wrapperState = {
                        wasMultiple: !!s.multiple
                    },
                    be("invalid", r);
                    break;
                case "textarea":
                    hm(r, s),
                    be("invalid", r)
                }
                ou(n, s),
                o = null;
                for (var i in s)
                    if (s.hasOwnProperty(i)) {
                        var l = s[i];
                        i === "children" ? typeof l == "string" ? r.textContent !== l && (s.suppressHydrationWarning !== !0 && Xa(r.textContent, l, e),
                        o = ["children", l]) : typeof l == "number" && r.textContent !== "" + l && (s.suppressHydrationWarning !== !0 && Xa(r.textContent, l, e),
                        o = ["children", "" + l]) : qs.hasOwnProperty(i) && l != null && i === "onScroll" && be("scroll", r)
                    }
                switch (n) {
                case "input":
                    Ha(r),
                    mm(r, s, !0);
                    break;
                case "textarea":
                    Ha(r),
                    pm(r);
                    break;
                case "select":
                case "option":
                    break;
                default:
                    typeof s.onClick == "function" && (r.onclick = $i)
                }
                r = o,
                t.updateQueue = r,
                r !== null && (t.flags |= 4)
            } else {
                i = o.nodeType === 9 ? o : o.ownerDocument,
                e === "http://www.w3.org/1999/xhtml" && (e = qp(n)),
                e === "http://www.w3.org/1999/xhtml" ? n === "script" ? (e = i.createElement("div"),
                e.innerHTML = "<script><\/script>",
                e = e.removeChild(e.firstChild)) : typeof r.is == "string" ? e = i.createElement(n, {
                    is: r.is
                }) : (e = i.createElement(n),
                n === "select" && (i = e,
                r.multiple ? i.multiple = !0 : r.size && (i.size = r.size))) : e = i.createElementNS(e, n),
                e[dn] = t,
                e[aa] = r,
                wg(e, t, !1, !1),
                t.stateNode = e;
                e: {
                    switch (i = su(n, r),
                    n) {
                    case "dialog":
                        be("cancel", e),
                        be("close", e),
                        o = r;
                        break;
                    case "iframe":
                    case "object":
                    case "embed":
                        be("load", e),
                        o = r;
                        break;
                    case "video":
                    case "audio":
                        for (o = 0; o < Fs.length; o++)
                            be(Fs[o], e);
                        o = r;
                        break;
                    case "source":
                        be("error", e),
                        o = r;
                        break;
                    case "img":
                    case "image":
                    case "link":
                        be("error", e),
                        be("load", e),
                        o = r;
                        break;
                    case "details":
                        be("toggle", e),
                        o = r;
                        break;
                    case "input":
                        fm(e, r),
                        o = Zc(e, r),
                        be("invalid", e);
                        break;
                    case "option":
                        o = r;
                        break;
                    case "select":
                        e._wrapperState = {
                            wasMultiple: !!r.multiple
                        },
                        o = Te({}, r, {
                            value: void 0
                        }),
                        be("invalid", e);
                        break;
                    case "textarea":
                        hm(e, r),
                        o = nu(e, r),
                        be("invalid", e);
                        break;
                    default:
                        o = r
                    }
                    ou(n, o),
                    l = o;
                    for (s in l)
                        if (l.hasOwnProperty(s)) {
                            var c = l[s];
                            s === "style" ? Zp(e, c) : s === "dangerouslySetInnerHTML" ? (c = c ? c.__html : void 0,
                            c != null && Xp(e, c)) : s === "children" ? typeof c == "string" ? (n !== "textarea" || c !== "") && Xs(e, c) : typeof c == "number" && Xs(e, "" + c) : s !== "suppressContentEditableWarning" && s !== "suppressHydrationWarning" && s !== "autoFocus" && (qs.hasOwnProperty(s) ? c != null && s === "onScroll" && be("scroll", e) : c != null && jd(e, s, c, i))
                        }
                    switch (n) {
                    case "input":
                        Ha(e),
                        mm(e, r, !1);
                        break;
                    case "textarea":
                        Ha(e),
                        pm(e);
                        break;
                    case "option":
                        r.value != null && e.setAttribute("value", "" + yr(r.value));
                        break;
                    case "select":
                        e.multiple = !!r.multiple,
                        s = r.value,
                        s != null ? _o(e, !!r.multiple, s, !1) : r.defaultValue != null && _o(e, !!r.multiple, r.defaultValue, !0);
                        break;
                    default:
                        typeof o.onClick == "function" && (e.onclick = $i)
                    }
                    switch (n) {
                    case "button":
                    case "input":
                    case "select":
                    case "textarea":
                        r = !!r.autoFocus;
                        break e;
                    case "img":
                        r = !0;
                        break e;
                    default:
                        r = !1
                    }
                }
                r && (t.flags |= 4)
            }
            t.ref !== null && (t.flags |= 512,
            t.flags |= 2097152)
        }
        return Ge(t),
        null;
    case 6:
        if (e && t.stateNode != null)
            Ng(e, t, e.memoizedProps, r);
        else {
            if (typeof r != "string" && t.stateNode === null)
                throw Error(_(166));
            if (n = Fr(la.current),
            Fr(vn.current),
            Ja(t)) {
                if (r = t.stateNode,
                n = t.memoizedProps,
                r[dn] = t,
                (s = r.nodeValue !== n) && (e = yt,
                e !== null))
                    switch (e.tag) {
                    case 3:
                        Xa(r.nodeValue, n, (e.mode & 1) !== 0);
                        break;
                    case 5:
                        e.memoizedProps.suppressHydrationWarning !== !0 && Xa(r.nodeValue, n, (e.mode & 1) !== 0)
                    }
                s && (t.flags |= 4)
            } else
                r = (n.nodeType === 9 ? n : n.ownerDocument).createTextNode(r),
                r[dn] = t,
                t.stateNode = r
        }
        return Ge(t),
        null;
    case 13:
        if (Ne(ke),
        r = t.memoizedState,
        e === null || e.memoizedState !== null && e.memoizedState.dehydrated !== null) {
            if (je && gt !== null && t.mode & 1 && !(t.flags & 128))
                $v(),
                Jo(),
                t.flags |= 98560,
                s = !1;
            else if (s = Ja(t),
            r !== null && r.dehydrated !== null) {
                if (e === null) {
                    if (!s)
                        throw Error(_(318));
                    if (s = t.memoizedState,
                    s = s !== null ? s.dehydrated : null,
                    !s)
                        throw Error(_(317));
                    s[dn] = t
                } else
                    Jo(),
                    !(t.flags & 128) && (t.memoizedState = null),
                    t.flags |= 4;
                Ge(t),
                s = !1
            } else
                Yt !== null && (zu(Yt),
                Yt = null),
                s = !0;
            if (!s)
                return t.flags & 65536 ? t : null
        }
        return t.flags & 128 ? (t.lanes = n,
        t) : (r = r !== null,
        r !== (e !== null && e.memoizedState !== null) && r && (t.child.flags |= 8192,
        t.mode & 1 && (e === null || ke.current & 1 ? ze === 0 && (ze = 3) : af())),
        t.updateQueue !== null && (t.flags |= 4),
        Ge(t),
        null);
    case 4:
        return es(),
        Ru(e, t),
        e === null && oa(t.stateNode.containerInfo),
        Ge(t),
        null;
    case 10:
        return Hd(t.type._context),
        Ge(t),
        null;
    case 17:
        return ft(t.type) && Bi(),
        Ge(t),
        null;
    case 19:
        if (Ne(ke),
        s = t.memoizedState,
        s === null)
            return Ge(t),
            null;
        if (r = (t.flags & 128) !== 0,
        i = s.rendering,
        i === null)
            if (r)
                Ts(s, !1);
            else {
                if (ze !== 0 || e !== null && e.flags & 128)
                    for (e = t.child; e !== null; ) {
                        if (i = Qi(e),
                        i !== null) {
                            for (t.flags |= 128,
                            Ts(s, !1),
                            r = i.updateQueue,
                            r !== null && (t.updateQueue = r,
                            t.flags |= 4),
                            t.subtreeFlags = 0,
                            r = n,
                            n = t.child; n !== null; )
                                s = n,
                                e = r,
                                s.flags &= 14680066,
                                i = s.alternate,
                                i === null ? (s.childLanes = 0,
                                s.lanes = e,
                                s.child = null,
                                s.subtreeFlags = 0,
                                s.memoizedProps = null,
                                s.memoizedState = null,
                                s.updateQueue = null,
                                s.dependencies = null,
                                s.stateNode = null) : (s.childLanes = i.childLanes,
                                s.lanes = i.lanes,
                                s.child = i.child,
                                s.subtreeFlags = 0,
                                s.deletions = null,
                                s.memoizedProps = i.memoizedProps,
                                s.memoizedState = i.memoizedState,
                                s.updateQueue = i.updateQueue,
                                s.type = i.type,
                                e = i.dependencies,
                                s.dependencies = e === null ? null : {
                                    lanes: e.lanes,
                                    firstContext: e.firstContext
                                }),
                                n = n.sibling;
                            return ge(ke, ke.current & 1 | 2),
                            t.child
                        }
                        e = e.sibling
                    }
                s.tail !== null && Oe() > ns && (t.flags |= 128,
                r = !0,
                Ts(s, !1),
                t.lanes = 4194304)
            }
        else {
            if (!r)
                if (e = Qi(i),
                e !== null) {
                    if (t.flags |= 128,
                    r = !0,
                    n = e.updateQueue,
                    n !== null && (t.updateQueue = n,
                    t.flags |= 4),
                    Ts(s, !0),
                    s.tail === null && s.tailMode === "hidden" && !i.alternate && !je)
                        return Ge(t),
                        null
                } else
                    2 * Oe() - s.renderingStartTime > ns && n !== 1073741824 && (t.flags |= 128,
                    r = !0,
                    Ts(s, !1),
                    t.lanes = 4194304);
            s.isBackwards ? (i.sibling = t.child,
            t.child = i) : (n = s.last,
            n !== null ? n.sibling = i : t.child = i,
            s.last = i)
        }
        return s.tail !== null ? (t = s.tail,
        s.rendering = t,
        s.tail = t.sibling,
        s.renderingStartTime = Oe(),
        t.sibling = null,
        n = ke.current,
        ge(ke, r ? n & 1 | 2 : n & 1),
        t) : (Ge(t),
        null);
    case 22:
    case 23:
        return sf(),
        r = t.memoizedState !== null,
        e !== null && e.memoizedState !== null !== r && (t.flags |= 8192),
        r && t.mode & 1 ? pt & 1073741824 && (Ge(t),
        t.subtreeFlags & 6 && (t.flags |= 8192)) : Ge(t),
        null;
    case 24:
        return null;
    case 25:
        return null
    }
    throw Error(_(156, t.tag))
}
function Gb(e, t) {
    switch (zd(t),
    t.tag) {
    case 1:
        return ft(t.type) && Bi(),
        e = t.flags,
        e & 65536 ? (t.flags = e & -65537 | 128,
        t) : null;
    case 3:
        return es(),
        Ne(dt),
        Ne(Je),
        Qd(),
        e = t.flags,
        e & 65536 && !(e & 128) ? (t.flags = e & -65537 | 128,
        t) : null;
    case 5:
        return Kd(t),
        null;
    case 13:
        if (Ne(ke),
        e = t.memoizedState,
        e !== null && e.dehydrated !== null) {
            if (t.alternate === null)
                throw Error(_(340));
            Jo()
        }
        return e = t.flags,
        e & 65536 ? (t.flags = e & -65537 | 128,
        t) : null;
    case 19:
        return Ne(ke),
        null;
    case 4:
        return es(),
        null;
    case 10:
        return Hd(t.type._context),
        null;
    case 22:
    case 23:
        return sf(),
        null;
    case 24:
        return null;
    default:
        return null
    }
}
var ti = !1
  , Xe = !1
  , qb = typeof WeakSet == "function" ? WeakSet : Set
  , B = null;
function Mo(e, t) {
    var n = e.ref;
    if (n !== null)
        if (typeof n == "function")
            try {
                n(null)
            } catch (r) {
                De(e, t, r)
            }
        else
            n.current = null
}
function _u(e, t, n) {
    try {
        n()
    } catch (r) {
        De(e, t, r)
    }
}
var oh = !1;
function Xb(e, t) {
    if (pu = Li,
    e = Ev(),
    Ld(e)) {
        if ("selectionStart"in e)
            var n = {
                start: e.selectionStart,
                end: e.selectionEnd
            };
        else
            e: {
                n = (n = e.ownerDocument) && n.defaultView || window;
                var r = n.getSelection && n.getSelection();
                if (r && r.rangeCount !== 0) {
                    n = r.anchorNode;
                    var o = r.anchorOffset
                      , s = r.focusNode;
                    r = r.focusOffset;
                    try {
                        n.nodeType,
                        s.nodeType
                    } catch {
                        n = null;
                        break e
                    }
                    var i = 0
                      , l = -1
                      , c = -1
                      , u = 0
                      , d = 0
                      , f = e
                      , g = null;
                    t: for (; ; ) {
                        for (var h; f !== n || o !== 0 && f.nodeType !== 3 || (l = i + o),
                        f !== s || r !== 0 && f.nodeType !== 3 || (c = i + r),
                        f.nodeType === 3 && (i += f.nodeValue.length),
                        (h = f.firstChild) !== null; )
                            g = f,
                            f = h;
                        for (; ; ) {
                            if (f === e)
                                break t;
                            if (g === n && ++u === o && (l = i),
                            g === s && ++d === r && (c = i),
                            (h = f.nextSibling) !== null)
                                break;
                            f = g,
                            g = f.parentNode
                        }
                        f = h
                    }
                    n = l === -1 || c === -1 ? null : {
                        start: l,
                        end: c
                    }
                } else
                    n = null
            }
        n = n || {
            start: 0,
            end: 0
        }
    } else
        n = null;
    for (vu = {
        focusedElem: e,
        selectionRange: n
    },
    Li = !1,
    B = t; B !== null; )
        if (t = B,
        e = t.child,
        (t.subtreeFlags & 1028) !== 0 && e !== null)
            e.return = t,
            B = e;
        else
            for (; B !== null; ) {
                t = B;
                try {
                    var b = t.alternate;
                    if (t.flags & 1024)
                        switch (t.tag) {
                        case 0:
                        case 11:
                        case 15:
                            break;
                        case 1:
                            if (b !== null) {
                                var v = b.memoizedProps
                                  , w = b.memoizedState
                                  , y = t.stateNode
                                  , p = y.getSnapshotBeforeUpdate(t.elementType === t.type ? v : Bt(t.type, v), w);
                                y.__reactInternalSnapshotBeforeUpdate = p
                            }
                            break;
                        case 3:
                            var x = t.stateNode.containerInfo;
                            x.nodeType === 1 ? x.textContent = "" : x.nodeType === 9 && x.documentElement && x.removeChild(x.documentElement);
                            break;
                        case 5:
                        case 6:
                        case 4:
                        case 17:
                            break;
                        default:
                            throw Error(_(163))
                        }
                } catch (N) {
                    De(t, t.return, N)
                }
                if (e = t.sibling,
                e !== null) {
                    e.return = t.return,
                    B = e;
                    break
                }
                B = t.return
            }
    return b = oh,
    oh = !1,
    b
}
function Ys(e, t, n) {
    var r = t.updateQueue;
    if (r = r !== null ? r.lastEffect : null,
    r !== null) {
        var o = r = r.next;
        do {
            if ((o.tag & e) === e) {
                var s = o.destroy;
                o.destroy = void 0,
                s !== void 0 && _u(t, n, s)
            }
            o = o.next
        } while (o !== r)
    }
}
function jl(e, t) {
    if (t = t.updateQueue,
    t = t !== null ? t.lastEffect : null,
    t !== null) {
        var n = t = t.next;
        do {
            if ((n.tag & e) === e) {
                var r = n.create;
                n.destroy = r()
            }
            n = n.next
        } while (n !== t)
    }
}
function Du(e) {
    var t = e.ref;
    if (t !== null) {
        var n = e.stateNode;
        switch (e.tag) {
        case 5:
            e = n;
            break;
        default:
            e = n
        }
        typeof t == "function" ? t(e) : t.current = e
    }
}
function Sg(e) {
    var t = e.alternate;
    t !== null && (e.alternate = null,
    Sg(t)),
    e.child = null,
    e.deletions = null,
    e.sibling = null,
    e.tag === 5 && (t = e.stateNode,
    t !== null && (delete t[dn],
    delete t[aa],
    delete t[xu],
    delete t[Db],
    delete t[Ob])),
    e.stateNode = null,
    e.return = null,
    e.dependencies = null,
    e.memoizedProps = null,
    e.memoizedState = null,
    e.pendingProps = null,
    e.stateNode = null,
    e.updateQueue = null
}
function jg(e) {
    return e.tag === 5 || e.tag === 3 || e.tag === 4
}
function sh(e) {
    e: for (; ; ) {
        for (; e.sibling === null; ) {
            if (e.return === null || jg(e.return))
                return null;
            e = e.return
        }
        for (e.sibling.return = e.return,
        e = e.sibling; e.tag !== 5 && e.tag !== 6 && e.tag !== 18; ) {
            if (e.flags & 2 || e.child === null || e.tag === 4)
                continue e;
            e.child.return = e,
            e = e.child
        }
        if (!(e.flags & 2))
            return e.stateNode
    }
}
function Ou(e, t, n) {
    var r = e.tag;
    if (r === 5 || r === 6)
        e = e.stateNode,
        t ? n.nodeType === 8 ? n.parentNode.insertBefore(e, t) : n.insertBefore(e, t) : (n.nodeType === 8 ? (t = n.parentNode,
        t.insertBefore(e, n)) : (t = n,
        t.appendChild(e)),
        n = n._reactRootContainer,
        n != null || t.onclick !== null || (t.onclick = $i));
    else if (r !== 4 && (e = e.child,
    e !== null))
        for (Ou(e, t, n),
        e = e.sibling; e !== null; )
            Ou(e, t, n),
            e = e.sibling
}
function Au(e, t, n) {
    var r = e.tag;
    if (r === 5 || r === 6)
        e = e.stateNode,
        t ? n.insertBefore(e, t) : n.appendChild(e);
    else if (r !== 4 && (e = e.child,
    e !== null))
        for (Au(e, t, n),
        e = e.sibling; e !== null; )
            Au(e, t, n),
            e = e.sibling
}
var We = null
  , Ut = !1;
function Vn(e, t, n) {
    for (n = n.child; n !== null; )
        Cg(e, t, n),
        n = n.sibling
}
function Cg(e, t, n) {
    if (pn && typeof pn.onCommitFiberUnmount == "function")
        try {
            pn.onCommitFiberUnmount(vl, n)
        } catch {}
    switch (n.tag) {
    case 5:
        Xe || Mo(n, t);
    case 6:
        var r = We
          , o = Ut;
        We = null,
        Vn(e, t, n),
        We = r,
        Ut = o,
        We !== null && (Ut ? (e = We,
        n = n.stateNode,
        e.nodeType === 8 ? e.parentNode.removeChild(n) : e.removeChild(n)) : We.removeChild(n.stateNode));
        break;
    case 18:
        We !== null && (Ut ? (e = We,
        n = n.stateNode,
        e.nodeType === 8 ? vc(e.parentNode, n) : e.nodeType === 1 && vc(e, n),
        ta(e)) : vc(We, n.stateNode));
        break;
    case 4:
        r = We,
        o = Ut,
        We = n.stateNode.containerInfo,
        Ut = !0,
        Vn(e, t, n),
        We = r,
        Ut = o;
        break;
    case 0:
    case 11:
    case 14:
    case 15:
        if (!Xe && (r = n.updateQueue,
        r !== null && (r = r.lastEffect,
        r !== null))) {
            o = r = r.next;
            do {
                var s = o
                  , i = s.destroy;
                s = s.tag,
                i !== void 0 && (s & 2 || s & 4) && _u(n, t, i),
                o = o.next
            } while (o !== r)
        }
        Vn(e, t, n);
        break;
    case 1:
        if (!Xe && (Mo(n, t),
        r = n.stateNode,
        typeof r.componentWillUnmount == "function"))
            try {
                r.props = n.memoizedProps,
                r.state = n.memoizedState,
                r.componentWillUnmount()
            } catch (l) {
                De(n, t, l)
            }
        Vn(e, t, n);
        break;
    case 21:
        Vn(e, t, n);
        break;
    case 22:
        n.mode & 1 ? (Xe = (r = Xe) || n.memoizedState !== null,
        Vn(e, t, n),
        Xe = r) : Vn(e, t, n);
        break;
    default:
        Vn(e, t, n)
    }
}
function ah(e) {
    var t = e.updateQueue;
    if (t !== null) {
        e.updateQueue = null;
        var n = e.stateNode;
        n === null && (n = e.stateNode = new qb),
        t.forEach(function(r) {
            var o = aN.bind(null, e, r);
            n.has(r) || (n.add(r),
            r.then(o, o))
        })
    }
}
function Ft(e, t) {
    var n = t.deletions;
    if (n !== null)
        for (var r = 0; r < n.length; r++) {
            var o = n[r];
            try {
                var s = e
                  , i = t
                  , l = i;
                e: for (; l !== null; ) {
                    switch (l.tag) {
                    case 5:
                        We = l.stateNode,
                        Ut = !1;
                        break e;
                    case 3:
                        We = l.stateNode.containerInfo,
                        Ut = !0;
                        break e;
                    case 4:
                        We = l.stateNode.containerInfo,
                        Ut = !0;
                        break e
                    }
                    l = l.return
                }
                if (We === null)
                    throw Error(_(160));
                Cg(s, i, o),
                We = null,
                Ut = !1;
                var c = o.alternate;
                c !== null && (c.return = null),
                o.return = null
            } catch (u) {
                De(o, t, u)
            }
        }
    if (t.subtreeFlags & 12854)
        for (t = t.child; t !== null; )
            kg(t, e),
            t = t.sibling
}
function kg(e, t) {
    var n = e.alternate
      , r = e.flags;
    switch (e.tag) {
    case 0:
    case 11:
    case 14:
    case 15:
        if (Ft(t, e),
        sn(e),
        r & 4) {
            try {
                Ys(3, e, e.return),
                jl(3, e)
            } catch (v) {
                De(e, e.return, v)
            }
            try {
                Ys(5, e, e.return)
            } catch (v) {
                De(e, e.return, v)
            }
        }
        break;
    case 1:
        Ft(t, e),
        sn(e),
        r & 512 && n !== null && Mo(n, n.return);
        break;
    case 5:
        if (Ft(t, e),
        sn(e),
        r & 512 && n !== null && Mo(n, n.return),
        e.flags & 32) {
            var o = e.stateNode;
            try {
                Xs(o, "")
            } catch (v) {
                De(e, e.return, v)
            }
        }
        if (r & 4 && (o = e.stateNode,
        o != null)) {
            var s = e.memoizedProps
              , i = n !== null ? n.memoizedProps : s
              , l = e.type
              , c = e.updateQueue;
            if (e.updateQueue = null,
            c !== null)
                try {
                    l === "input" && s.type === "radio" && s.name != null && Qp(o, s),
                    su(l, i);
                    var u = su(l, s);
                    for (i = 0; i < c.length; i += 2) {
                        var d = c[i]
                          , f = c[i + 1];
                        d === "style" ? Zp(o, f) : d === "dangerouslySetInnerHTML" ? Xp(o, f) : d === "children" ? Xs(o, f) : jd(o, d, f, u)
                    }
                    switch (l) {
                    case "input":
                        eu(o, s);
                        break;
                    case "textarea":
                        Gp(o, s);
                        break;
                    case "select":
                        var g = o._wrapperState.wasMultiple;
                        o._wrapperState.wasMultiple = !!s.multiple;
                        var h = s.value;
                        h != null ? _o(o, !!s.multiple, h, !1) : g !== !!s.multiple && (s.defaultValue != null ? _o(o, !!s.multiple, s.defaultValue, !0) : _o(o, !!s.multiple, s.multiple ? [] : "", !1))
                    }
                    o[aa] = s
                } catch (v) {
                    De(e, e.return, v)
                }
        }
        break;
    case 6:
        if (Ft(t, e),
        sn(e),
        r & 4) {
            if (e.stateNode === null)
                throw Error(_(162));
            o = e.stateNode,
            s = e.memoizedProps;
            try {
                o.nodeValue = s
            } catch (v) {
                De(e, e.return, v)
            }
        }
        break;
    case 3:
        if (Ft(t, e),
        sn(e),
        r & 4 && n !== null && n.memoizedState.isDehydrated)
            try {
                ta(t.containerInfo)
            } catch (v) {
                De(e, e.return, v)
            }
        break;
    case 4:
        Ft(t, e),
        sn(e);
        break;
    case 13:
        Ft(t, e),
        sn(e),
        o = e.child,
        o.flags & 8192 && (s = o.memoizedState !== null,
        o.stateNode.isHidden = s,
        !s || o.alternate !== null && o.alternate.memoizedState !== null || (rf = Oe())),
        r & 4 && ah(e);
        break;
    case 22:
        if (d = n !== null && n.memoizedState !== null,
        e.mode & 1 ? (Xe = (u = Xe) || d,
        Ft(t, e),
        Xe = u) : Ft(t, e),
        sn(e),
        r & 8192) {
            if (u = e.memoizedState !== null,
            (e.stateNode.isHidden = u) && !d && e.mode & 1)
                for (B = e,
                d = e.child; d !== null; ) {
                    for (f = B = d; B !== null; ) {
                        switch (g = B,
                        h = g.child,
                        g.tag) {
                        case 0:
                        case 11:
                        case 14:
                        case 15:
                            Ys(4, g, g.return);
                            break;
                        case 1:
                            Mo(g, g.return);
                            var b = g.stateNode;
                            if (typeof b.componentWillUnmount == "function") {
                                r = g,
                                n = g.return;
                                try {
                                    t = r,
                                    b.props = t.memoizedProps,
                                    b.state = t.memoizedState,
                                    b.componentWillUnmount()
                                } catch (v) {
                                    De(r, n, v)
                                }
                            }
                            break;
                        case 5:
                            Mo(g, g.return);
                            break;
                        case 22:
                            if (g.memoizedState !== null) {
                                lh(f);
                                continue
                            }
                        }
                        h !== null ? (h.return = g,
                        B = h) : lh(f)
                    }
                    d = d.sibling
                }
            e: for (d = null,
            f = e; ; ) {
                if (f.tag === 5) {
                    if (d === null) {
                        d = f;
                        try {
                            o = f.stateNode,
                            u ? (s = o.style,
                            typeof s.setProperty == "function" ? s.setProperty("display", "none", "important") : s.display = "none") : (l = f.stateNode,
                            c = f.memoizedProps.style,
                            i = c != null && c.hasOwnProperty("display") ? c.display : null,
                            l.style.display = Jp("display", i))
                        } catch (v) {
                            De(e, e.return, v)
                        }
                    }
                } else if (f.tag === 6) {
                    if (d === null)
                        try {
                            f.stateNode.nodeValue = u ? "" : f.memoizedProps
                        } catch (v) {
                            De(e, e.return, v)
                        }
                } else if ((f.tag !== 22 && f.tag !== 23 || f.memoizedState === null || f === e) && f.child !== null) {
                    f.child.return = f,
                    f = f.child;
                    continue
                }
                if (f === e)
                    break e;
                for (; f.sibling === null; ) {
                    if (f.return === null || f.return === e)
                        break e;
                    d === f && (d = null),
                    f = f.return
                }
                d === f && (d = null),
                f.sibling.return = f.return,
                f = f.sibling
            }
        }
        break;
    case 19:
        Ft(t, e),
        sn(e),
        r & 4 && ah(e);
        break;
    case 21:
        break;
    default:
        Ft(t, e),
        sn(e)
    }
}
function sn(e) {
    var t = e.flags;
    if (t & 2) {
        try {
            e: {
                for (var n = e.return; n !== null; ) {
                    if (jg(n)) {
                        var r = n;
                        break e
                    }
                    n = n.return
                }
                throw Error(_(160))
            }
            switch (r.tag) {
            case 5:
                var o = r.stateNode;
                r.flags & 32 && (Xs(o, ""),
                r.flags &= -33);
                var s = sh(e);
                Au(e, s, o);
                break;
            case 3:
            case 4:
                var i = r.stateNode.containerInfo
                  , l = sh(e);
                Ou(e, l, i);
                break;
            default:
                throw Error(_(161))
            }
        } catch (c) {
            De(e, e.return, c)
        }
        e.flags &= -3
    }
    t & 4096 && (e.flags &= -4097)
}
function Jb(e, t, n) {
    B = e,
    Eg(e)
}
function Eg(e, t, n) {
    for (var r = (e.mode & 1) !== 0; B !== null; ) {
        var o = B
          , s = o.child;
        if (o.tag === 22 && r) {
            var i = o.memoizedState !== null || ti;
            if (!i) {
                var l = o.alternate
                  , c = l !== null && l.memoizedState !== null || Xe;
                l = ti;
                var u = Xe;
                if (ti = i,
                (Xe = c) && !u)
                    for (B = o; B !== null; )
                        i = B,
                        c = i.child,
                        i.tag === 22 && i.memoizedState !== null ? ch(o) : c !== null ? (c.return = i,
                        B = c) : ch(o);
                for (; s !== null; )
                    B = s,
                    Eg(s),
                    s = s.sibling;
                B = o,
                ti = l,
                Xe = u
            }
            ih(e)
        } else
            o.subtreeFlags & 8772 && s !== null ? (s.return = o,
            B = s) : ih(e)
    }
}
function ih(e) {
    for (; B !== null; ) {
        var t = B;
        if (t.flags & 8772) {
            var n = t.alternate;
            try {
                if (t.flags & 8772)
                    switch (t.tag) {
                    case 0:
                    case 11:
                    case 15:
                        Xe || jl(5, t);
                        break;
                    case 1:
                        var r = t.stateNode;
                        if (t.flags & 4 && !Xe)
                            if (n === null)
                                r.componentDidMount();
                            else {
                                var o = t.elementType === t.type ? n.memoizedProps : Bt(t.type, n.memoizedProps);
                                r.componentDidUpdate(o, n.memoizedState, r.__reactInternalSnapshotBeforeUpdate)
                            }
                        var s = t.updateQueue;
                        s !== null && Um(t, s, r);
                        break;
                    case 3:
                        var i = t.updateQueue;
                        if (i !== null) {
                            if (n = null,
                            t.child !== null)
                                switch (t.child.tag) {
                                case 5:
                                    n = t.child.stateNode;
                                    break;
                                case 1:
                                    n = t.child.stateNode
                                }
                            Um(t, i, n)
                        }
                        break;
                    case 5:
                        var l = t.stateNode;
                        if (n === null && t.flags & 4) {
                            n = l;
                            var c = t.memoizedProps;
                            switch (t.type) {
                            case "button":
                            case "input":
                            case "select":
                            case "textarea":
                                c.autoFocus && n.focus();
                                break;
                            case "img":
                                c.src && (n.src = c.src)
                            }
                        }
                        break;
                    case 6:
                        break;
                    case 4:
                        break;
                    case 12:
                        break;
                    case 13:
                        if (t.memoizedState === null) {
                            var u = t.alternate;
                            if (u !== null) {
                                var d = u.memoizedState;
                                if (d !== null) {
                                    var f = d.dehydrated;
                                    f !== null && ta(f)
                                }
                            }
                        }
                        break;
                    case 19:
                    case 17:
                    case 21:
                    case 22:
                    case 23:
                    case 25:
                        break;
                    default:
                        throw Error(_(163))
                    }
                Xe || t.flags & 512 && Du(t)
            } catch (g) {
                De(t, t.return, g)
            }
        }
        if (t === e) {
            B = null;
            break
        }
        if (n = t.sibling,
        n !== null) {
            n.return = t.return,
            B = n;
            break
        }
        B = t.return
    }
}
function lh(e) {
    for (; B !== null; ) {
        var t = B;
        if (t === e) {
            B = null;
            break
        }
        var n = t.sibling;
        if (n !== null) {
            n.return = t.return,
            B = n;
            break
        }
        B = t.return
    }
}
function ch(e) {
    for (; B !== null; ) {
        var t = B;
        try {
            switch (t.tag) {
            case 0:
            case 11:
            case 15:
                var n = t.return;
                try {
                    jl(4, t)
                } catch (c) {
                    De(t, n, c)
                }
                break;
            case 1:
                var r = t.stateNode;
                if (typeof r.componentDidMount == "function") {
                    var o = t.return;
                    try {
                        r.componentDidMount()
                    } catch (c) {
                        De(t, o, c)
                    }
                }
                var s = t.return;
                try {
                    Du(t)
                } catch (c) {
                    De(t, s, c)
                }
                break;
            case 5:
                var i = t.return;
                try {
                    Du(t)
                } catch (c) {
                    De(t, i, c)
                }
            }
        } catch (c) {
            De(t, t.return, c)
        }
        if (t === e) {
            B = null;
            break
        }
        var l = t.sibling;
        if (l !== null) {
            l.return = t.return,
            B = l;
            break
        }
        B = t.return
    }
}
var Zb = Math.ceil
  , Xi = zn.ReactCurrentDispatcher
  , tf = zn.ReactCurrentOwner
  , _t = zn.ReactCurrentBatchConfig
  , ie = 0
  , Be = null
  , Ae = null
  , He = 0
  , pt = 0
  , Ro = jr(0)
  , ze = 0
  , fa = null
  , qr = 0
  , Cl = 0
  , nf = 0
  , Ks = null
  , lt = null
  , rf = 0
  , ns = 1 / 0
  , kn = null
  , Ji = !1
  , Iu = null
  , hr = null
  , ni = !1
  , ar = null
  , Zi = 0
  , Qs = 0
  , Lu = null
  , Ni = -1
  , Si = 0;
function ot() {
    return ie & 6 ? Oe() : Ni !== -1 ? Ni : Ni = Oe()
}
function pr(e) {
    return e.mode & 1 ? ie & 2 && He !== 0 ? He & -He : Ib.transition !== null ? (Si === 0 && (Si = dv()),
    Si) : (e = pe,
    e !== 0 || (e = window.event,
    e = e === void 0 ? 16 : yv(e.type)),
    e) : 1
}
function qt(e, t, n, r) {
    if (50 < Qs)
        throw Qs = 0,
        Lu = null,
        Error(_(185));
    Ca(e, n, r),
    (!(ie & 2) || e !== Be) && (e === Be && (!(ie & 2) && (Cl |= n),
    ze === 4 && Zn(e, He)),
    mt(e, r),
    n === 1 && ie === 0 && !(t.mode & 1) && (ns = Oe() + 500,
    bl && Cr()))
}
function mt(e, t) {
    var n = e.callbackNode;
    I1(e, t);
    var r = Ii(e, e === Be ? He : 0);
    if (r === 0)
        n !== null && ym(n),
        e.callbackNode = null,
        e.callbackPriority = 0;
    else if (t = r & -r,
    e.callbackPriority !== t) {
        if (n != null && ym(n),
        t === 1)
            e.tag === 0 ? Ab(uh.bind(null, e)) : Lv(uh.bind(null, e)),
            Rb(function() {
                !(ie & 6) && Cr()
            }),
            n = null;
        else {
            switch (fv(r)) {
            case 1:
                n = Td;
                break;
            case 4:
                n = cv;
                break;
            case 16:
                n = Ai;
                break;
            case 536870912:
                n = uv;
                break;
            default:
                n = Ai
            }
            n = Ag(n, Pg.bind(null, e))
        }
        e.callbackPriority = t,
        e.callbackNode = n
    }
}
function Pg(e, t) {
    if (Ni = -1,
    Si = 0,
    ie & 6)
        throw Error(_(327));
    var n = e.callbackNode;
    if (Lo() && e.callbackNode !== n)
        return null;
    var r = Ii(e, e === Be ? He : 0);
    if (r === 0)
        return null;
    if (r & 30 || r & e.expiredLanes || t)
        t = el(e, r);
    else {
        t = r;
        var o = ie;
        ie |= 2;
        var s = Mg();
        (Be !== e || He !== t) && (kn = null,
        ns = Oe() + 500,
        Ur(e, t));
        do
            try {
                nN();
                break
            } catch (l) {
                Tg(e, l)
            }
        while (!0);
        Wd(),
        Xi.current = s,
        ie = o,
        Ae !== null ? t = 0 : (Be = null,
        He = 0,
        t = ze)
    }
    if (t !== 0) {
        if (t === 2 && (o = uu(e),
        o !== 0 && (r = o,
        t = Fu(e, o))),
        t === 1)
            throw n = fa,
            Ur(e, 0),
            Zn(e, r),
            mt(e, Oe()),
            n;
        if (t === 6)
            Zn(e, r);
        else {
            if (o = e.current.alternate,
            !(r & 30) && !eN(o) && (t = el(e, r),
            t === 2 && (s = uu(e),
            s !== 0 && (r = s,
            t = Fu(e, s))),
            t === 1))
                throw n = fa,
                Ur(e, 0),
                Zn(e, r),
                mt(e, Oe()),
                n;
            switch (e.finishedWork = o,
            e.finishedLanes = r,
            t) {
            case 0:
            case 1:
                throw Error(_(345));
            case 2:
                Or(e, lt, kn);
                break;
            case 3:
                if (Zn(e, r),
                (r & 130023424) === r && (t = rf + 500 - Oe(),
                10 < t)) {
                    if (Ii(e, 0) !== 0)
                        break;
                    if (o = e.suspendedLanes,
                    (o & r) !== r) {
                        ot(),
                        e.pingedLanes |= e.suspendedLanes & o;
                        break
                    }
                    e.timeoutHandle = yu(Or.bind(null, e, lt, kn), t);
                    break
                }
                Or(e, lt, kn);
                break;
            case 4:
                if (Zn(e, r),
                (r & 4194240) === r)
                    break;
                for (t = e.eventTimes,
                o = -1; 0 < r; ) {
                    var i = 31 - Gt(r);
                    s = 1 << i,
                    i = t[i],
                    i > o && (o = i),
                    r &= ~s
                }
                if (r = o,
                r = Oe() - r,
                r = (120 > r ? 120 : 480 > r ? 480 : 1080 > r ? 1080 : 1920 > r ? 1920 : 3e3 > r ? 3e3 : 4320 > r ? 4320 : 1960 * Zb(r / 1960)) - r,
                10 < r) {
                    e.timeoutHandle = yu(Or.bind(null, e, lt, kn), r);
                    break
                }
                Or(e, lt, kn);
                break;
            case 5:
                Or(e, lt, kn);
                break;
            default:
                throw Error(_(329))
            }
        }
    }
    return mt(e, Oe()),
    e.callbackNode === n ? Pg.bind(null, e) : null
}
function Fu(e, t) {
    var n = Ks;
    return e.current.memoizedState.isDehydrated && (Ur(e, t).flags |= 256),
    e = el(e, t),
    e !== 2 && (t = lt,
    lt = n,
    t !== null && zu(t)),
    e
}
function zu(e) {
    lt === null ? lt = e : lt.push.apply(lt, e)
}
function eN(e) {
    for (var t = e; ; ) {
        if (t.flags & 16384) {
            var n = t.updateQueue;
            if (n !== null && (n = n.stores,
            n !== null))
                for (var r = 0; r < n.length; r++) {
                    var o = n[r]
                      , s = o.getSnapshot;
                    o = o.value;
                    try {
                        if (!Jt(s(), o))
                            return !1
                    } catch {
                        return !1
                    }
                }
        }
        if (n = t.child,
        t.subtreeFlags & 16384 && n !== null)
            n.return = t,
            t = n;
        else {
            if (t === e)
                break;
            for (; t.sibling === null; ) {
                if (t.return === null || t.return === e)
                    return !0;
                t = t.return
            }
            t.sibling.return = t.return,
            t = t.sibling
        }
    }
    return !0
}
function Zn(e, t) {
    for (t &= ~nf,
    t &= ~Cl,
    e.suspendedLanes |= t,
    e.pingedLanes &= ~t,
    e = e.expirationTimes; 0 < t; ) {
        var n = 31 - Gt(t)
          , r = 1 << n;
        e[n] = -1,
        t &= ~r
    }
}
function uh(e) {
    if (ie & 6)
        throw Error(_(327));
    Lo();
    var t = Ii(e, 0);
    if (!(t & 1))
        return mt(e, Oe()),
        null;
    var n = el(e, t);
    if (e.tag !== 0 && n === 2) {
        var r = uu(e);
        r !== 0 && (t = r,
        n = Fu(e, r))
    }
    if (n === 1)
        throw n = fa,
        Ur(e, 0),
        Zn(e, t),
        mt(e, Oe()),
        n;
    if (n === 6)
        throw Error(_(345));
    return e.finishedWork = e.current.alternate,
    e.finishedLanes = t,
    Or(e, lt, kn),
    mt(e, Oe()),
    null
}
function of(e, t) {
    var n = ie;
    ie |= 1;
    try {
        return e(t)
    } finally {
        ie = n,
        ie === 0 && (ns = Oe() + 500,
        bl && Cr())
    }
}
function Xr(e) {
    ar !== null && ar.tag === 0 && !(ie & 6) && Lo();
    var t = ie;
    ie |= 1;
    var n = _t.transition
      , r = pe;
    try {
        if (_t.transition = null,
        pe = 1,
        e)
            return e()
    } finally {
        pe = r,
        _t.transition = n,
        ie = t,
        !(ie & 6) && Cr()
    }
}
function sf() {
    pt = Ro.current,
    Ne(Ro)
}
function Ur(e, t) {
    e.finishedWork = null,
    e.finishedLanes = 0;
    var n = e.timeoutHandle;
    if (n !== -1 && (e.timeoutHandle = -1,
    Mb(n)),
    Ae !== null)
        for (n = Ae.return; n !== null; ) {
            var r = n;
            switch (zd(r),
            r.tag) {
            case 1:
                r = r.type.childContextTypes,
                r != null && Bi();
                break;
            case 3:
                es(),
                Ne(dt),
                Ne(Je),
                Qd();
                break;
            case 5:
                Kd(r);
                break;
            case 4:
                es();
                break;
            case 13:
                Ne(ke);
                break;
            case 19:
                Ne(ke);
                break;
            case 10:
                Hd(r.type._context);
                break;
            case 22:
            case 23:
                sf()
            }
            n = n.return
        }
    if (Be = e,
    Ae = e = vr(e.current, null),
    He = pt = t,
    ze = 0,
    fa = null,
    nf = Cl = qr = 0,
    lt = Ks = null,
    Lr !== null) {
        for (t = 0; t < Lr.length; t++)
            if (n = Lr[t],
            r = n.interleaved,
            r !== null) {
                n.interleaved = null;
                var o = r.next
                  , s = n.pending;
                if (s !== null) {
                    var i = s.next;
                    s.next = o,
                    r.next = i
                }
                n.pending = r
            }
        Lr = null
    }
    return e
}
function Tg(e, t) {
    do {
        var n = Ae;
        try {
            if (Wd(),
            xi.current = qi,
            Gi) {
                for (var r = Pe.memoizedState; r !== null; ) {
                    var o = r.queue;
                    o !== null && (o.pending = null),
                    r = r.next
                }
                Gi = !1
            }
            if (Gr = 0,
            $e = Le = Pe = null,
            Us = !1,
            ca = 0,
            tf.current = null,
            n === null || n.return === null) {
                ze = 1,
                fa = t,
                Ae = null;
                break
            }
            e: {
                var s = e
                  , i = n.return
                  , l = n
                  , c = t;
                if (t = He,
                l.flags |= 32768,
                c !== null && typeof c == "object" && typeof c.then == "function") {
                    var u = c
                      , d = l
                      , f = d.tag;
                    if (!(d.mode & 1) && (f === 0 || f === 11 || f === 15)) {
                        var g = d.alternate;
                        g ? (d.updateQueue = g.updateQueue,
                        d.memoizedState = g.memoizedState,
                        d.lanes = g.lanes) : (d.updateQueue = null,
                        d.memoizedState = null)
                    }
                    var h = Xm(i);
                    if (h !== null) {
                        h.flags &= -257,
                        Jm(h, i, l, s, t),
                        h.mode & 1 && qm(s, u, t),
                        t = h,
                        c = u;
                        var b = t.updateQueue;
                        if (b === null) {
                            var v = new Set;
                            v.add(c),
                            t.updateQueue = v
                        } else
                            b.add(c);
                        break e
                    } else {
                        if (!(t & 1)) {
                            qm(s, u, t),
                            af();
                            break e
                        }
                        c = Error(_(426))
                    }
                } else if (je && l.mode & 1) {
                    var w = Xm(i);
                    if (w !== null) {
                        !(w.flags & 65536) && (w.flags |= 256),
                        Jm(w, i, l, s, t),
                        $d(ts(c, l));
                        break e
                    }
                }
                s = c = ts(c, l),
                ze !== 4 && (ze = 2),
                Ks === null ? Ks = [s] : Ks.push(s),
                s = i;
                do {
                    switch (s.tag) {
                    case 3:
                        s.flags |= 65536,
                        t &= -t,
                        s.lanes |= t;
                        var y = fg(s, c, t);
                        Vm(s, y);
                        break e;
                    case 1:
                        l = c;
                        var p = s.type
                          , x = s.stateNode;
                        if (!(s.flags & 128) && (typeof p.getDerivedStateFromError == "function" || x !== null && typeof x.componentDidCatch == "function" && (hr === null || !hr.has(x)))) {
                            s.flags |= 65536,
                            t &= -t,
                            s.lanes |= t;
                            var N = mg(s, l, t);
                            Vm(s, N);
                            break e
                        }
                    }
                    s = s.return
                } while (s !== null)
            }
            _g(n)
        } catch (S) {
            t = S,
            Ae === n && n !== null && (Ae = n = n.return);
            continue
        }
        break
    } while (!0)
}
function Mg() {
    var e = Xi.current;
    return Xi.current = qi,
    e === null ? qi : e
}
function af() {
    (ze === 0 || ze === 3 || ze === 2) && (ze = 4),
    Be === null || !(qr & 268435455) && !(Cl & 268435455) || Zn(Be, He)
}
function el(e, t) {
    var n = ie;
    ie |= 2;
    var r = Mg();
    (Be !== e || He !== t) && (kn = null,
    Ur(e, t));
    do
        try {
            tN();
            break
        } catch (o) {
            Tg(e, o)
        }
    while (!0);
    if (Wd(),
    ie = n,
    Xi.current = r,
    Ae !== null)
        throw Error(_(261));
    return Be = null,
    He = 0,
    ze
}
function tN() {
    for (; Ae !== null; )
        Rg(Ae)
}
function nN() {
    for (; Ae !== null && !E1(); )
        Rg(Ae)
}
function Rg(e) {
    var t = Og(e.alternate, e, pt);
    e.memoizedProps = e.pendingProps,
    t === null ? _g(e) : Ae = t,
    tf.current = null
}
function _g(e) {
    var t = e;
    do {
        var n = t.alternate;
        if (e = t.return,
        t.flags & 32768) {
            if (n = Gb(n, t),
            n !== null) {
                n.flags &= 32767,
                Ae = n;
                return
            }
            if (e !== null)
                e.flags |= 32768,
                e.subtreeFlags = 0,
                e.deletions = null;
            else {
                ze = 6,
                Ae = null;
                return
            }
        } else if (n = Qb(n, t, pt),
        n !== null) {
            Ae = n;
            return
        }
        if (t = t.sibling,
        t !== null) {
            Ae = t;
            return
        }
        Ae = t = e
    } while (t !== null);
    ze === 0 && (ze = 5)
}
function Or(e, t, n) {
    var r = pe
      , o = _t.transition;
    try {
        _t.transition = null,
        pe = 1,
        rN(e, t, n, r)
    } finally {
        _t.transition = o,
        pe = r
    }
    return null
}
function rN(e, t, n, r) {
    do
        Lo();
    while (ar !== null);
    if (ie & 6)
        throw Error(_(327));
    n = e.finishedWork;
    var o = e.finishedLanes;
    if (n === null)
        return null;
    if (e.finishedWork = null,
    e.finishedLanes = 0,
    n === e.current)
        throw Error(_(177));
    e.callbackNode = null,
    e.callbackPriority = 0;
    var s = n.lanes | n.childLanes;
    if (L1(e, s),
    e === Be && (Ae = Be = null,
    He = 0),
    !(n.subtreeFlags & 2064) && !(n.flags & 2064) || ni || (ni = !0,
    Ag(Ai, function() {
        return Lo(),
        null
    })),
    s = (n.flags & 15990) !== 0,
    n.subtreeFlags & 15990 || s) {
        s = _t.transition,
        _t.transition = null;
        var i = pe;
        pe = 1;
        var l = ie;
        ie |= 4,
        tf.current = null,
        Xb(e, n),
        kg(n, e),
        Sb(vu),
        Li = !!pu,
        vu = pu = null,
        e.current = n,
        Jb(n),
        P1(),
        ie = l,
        pe = i,
        _t.transition = s
    } else
        e.current = n;
    if (ni && (ni = !1,
    ar = e,
    Zi = o),
    s = e.pendingLanes,
    s === 0 && (hr = null),
    R1(n.stateNode),
    mt(e, Oe()),
    t !== null)
        for (r = e.onRecoverableError,
        n = 0; n < t.length; n++)
            o = t[n],
            r(o.value, {
                componentStack: o.stack,
                digest: o.digest
            });
    if (Ji)
        throw Ji = !1,
        e = Iu,
        Iu = null,
        e;
    return Zi & 1 && e.tag !== 0 && Lo(),
    s = e.pendingLanes,
    s & 1 ? e === Lu ? Qs++ : (Qs = 0,
    Lu = e) : Qs = 0,
    Cr(),
    null
}
function Lo() {
    if (ar !== null) {
        var e = fv(Zi)
          , t = _t.transition
          , n = pe;
        try {
            if (_t.transition = null,
            pe = 16 > e ? 16 : e,
            ar === null)
                var r = !1;
            else {
                if (e = ar,
                ar = null,
                Zi = 0,
                ie & 6)
                    throw Error(_(331));
                var o = ie;
                for (ie |= 4,
                B = e.current; B !== null; ) {
                    var s = B
                      , i = s.child;
                    if (B.flags & 16) {
                        var l = s.deletions;
                        if (l !== null) {
                            for (var c = 0; c < l.length; c++) {
                                var u = l[c];
                                for (B = u; B !== null; ) {
                                    var d = B;
                                    switch (d.tag) {
                                    case 0:
                                    case 11:
                                    case 15:
                                        Ys(8, d, s)
                                    }
                                    var f = d.child;
                                    if (f !== null)
                                        f.return = d,
                                        B = f;
                                    else
                                        for (; B !== null; ) {
                                            d = B;
                                            var g = d.sibling
                                              , h = d.return;
                                            if (Sg(d),
                                            d === u) {
                                                B = null;
                                                break
                                            }
                                            if (g !== null) {
                                                g.return = h,
                                                B = g;
                                                break
                                            }
                                            B = h
                                        }
                                }
                            }
                            var b = s.alternate;
                            if (b !== null) {
                                var v = b.child;
                                if (v !== null) {
                                    b.child = null;
                                    do {
                                        var w = v.sibling;
                                        v.sibling = null,
                                        v = w
                                    } while (v !== null)
                                }
                            }
                            B = s
                        }
                    }
                    if (s.subtreeFlags & 2064 && i !== null)
                        i.return = s,
                        B = i;
                    else
                        e: for (; B !== null; ) {
                            if (s = B,
                            s.flags & 2048)
                                switch (s.tag) {
                                case 0:
                                case 11:
                                case 15:
                                    Ys(9, s, s.return)
                                }
                            var y = s.sibling;
                            if (y !== null) {
                                y.return = s.return,
                                B = y;
                                break e
                            }
                            B = s.return
                        }
                }
                var p = e.current;
                for (B = p; B !== null; ) {
                    i = B;
                    var x = i.child;
                    if (i.subtreeFlags & 2064 && x !== null)
                        x.return = i,
                        B = x;
                    else
                        e: for (i = p; B !== null; ) {
                            if (l = B,
                            l.flags & 2048)
                                try {
                                    switch (l.tag) {
                                    case 0:
                                    case 11:
                                    case 15:
                                        jl(9, l)
                                    }
                                } catch (S) {
                                    De(l, l.return, S)
                                }
                            if (l === i) {
                                B = null;
                                break e
                            }
                            var N = l.sibling;
                            if (N !== null) {
                                N.return = l.return,
                                B = N;
                                break e
                            }
                            B = l.return
                        }
                }
                if (ie = o,
                Cr(),
                pn && typeof pn.onPostCommitFiberRoot == "function")
                    try {
                        pn.onPostCommitFiberRoot(vl, e)
                    } catch {}
                r = !0
            }
            return r
        } finally {
            pe = n,
            _t.transition = t
        }
    }
    return !1
}
function dh(e, t, n) {
    t = ts(n, t),
    t = fg(e, t, 1),
    e = mr(e, t, 1),
    t = ot(),
    e !== null && (Ca(e, 1, t),
    mt(e, t))
}
function De(e, t, n) {
    if (e.tag === 3)
        dh(e, e, n);
    else
        for (; t !== null; ) {
            if (t.tag === 3) {
                dh(t, e, n);
                break
            } else if (t.tag === 1) {
                var r = t.stateNode;
                if (typeof t.type.getDerivedStateFromError == "function" || typeof r.componentDidCatch == "function" && (hr === null || !hr.has(r))) {
                    e = ts(n, e),
                    e = mg(t, e, 1),
                    t = mr(t, e, 1),
                    e = ot(),
                    t !== null && (Ca(t, 1, e),
                    mt(t, e));
                    break
                }
            }
            t = t.return
        }
}
function oN(e, t, n) {
    var r = e.pingCache;
    r !== null && r.delete(t),
    t = ot(),
    e.pingedLanes |= e.suspendedLanes & n,
    Be === e && (He & n) === n && (ze === 4 || ze === 3 && (He & 130023424) === He && 500 > Oe() - rf ? Ur(e, 0) : nf |= n),
    mt(e, t)
}
function Dg(e, t) {
    t === 0 && (e.mode & 1 ? (t = Ya,
    Ya <<= 1,
    !(Ya & 130023424) && (Ya = 4194304)) : t = 1);
    var n = ot();
    e = An(e, t),
    e !== null && (Ca(e, t, n),
    mt(e, n))
}
function sN(e) {
    var t = e.memoizedState
      , n = 0;
    t !== null && (n = t.retryLane),
    Dg(e, n)
}
function aN(e, t) {
    var n = 0;
    switch (e.tag) {
    case 13:
        var r = e.stateNode
          , o = e.memoizedState;
        o !== null && (n = o.retryLane);
        break;
    case 19:
        r = e.stateNode;
        break;
    default:
        throw Error(_(314))
    }
    r !== null && r.delete(t),
    Dg(e, n)
}
var Og;
Og = function(e, t, n) {
    if (e !== null)
        if (e.memoizedProps !== t.pendingProps || dt.current)
            ct = !0;
        else {
            if (!(e.lanes & n) && !(t.flags & 128))
                return ct = !1,
                Kb(e, t, n);
            ct = !!(e.flags & 131072)
        }
    else
        ct = !1,
        je && t.flags & 1048576 && Fv(t, Vi, t.index);
    switch (t.lanes = 0,
    t.tag) {
    case 2:
        var r = t.type;
        bi(e, t),
        e = t.pendingProps;
        var o = Xo(t, Je.current);
        Io(t, n),
        o = qd(null, t, r, e, o, n);
        var s = Xd();
        return t.flags |= 1,
        typeof o == "object" && o !== null && typeof o.render == "function" && o.$$typeof === void 0 ? (t.tag = 1,
        t.memoizedState = null,
        t.updateQueue = null,
        ft(r) ? (s = !0,
        Wi(t)) : s = !1,
        t.memoizedState = o.state !== null && o.state !== void 0 ? o.state : null,
        Ud(t),
        o.updater = Sl,
        t.stateNode = o,
        o._reactInternals = t,
        Cu(t, r, e, n),
        t = Pu(null, t, r, !0, s, n)) : (t.tag = 0,
        je && s && Fd(t),
        et(null, t, o, n),
        t = t.child),
        t;
    case 16:
        r = t.elementType;
        e: {
            switch (bi(e, t),
            e = t.pendingProps,
            o = r._init,
            r = o(r._payload),
            t.type = r,
            o = t.tag = lN(r),
            e = Bt(r, e),
            o) {
            case 0:
                t = Eu(null, t, r, e, n);
                break e;
            case 1:
                t = th(null, t, r, e, n);
                break e;
            case 11:
                t = Zm(null, t, r, e, n);
                break e;
            case 14:
                t = eh(null, t, r, Bt(r.type, e), n);
                break e
            }
            throw Error(_(306, r, ""))
        }
        return t;
    case 0:
        return r = t.type,
        o = t.pendingProps,
        o = t.elementType === r ? o : Bt(r, o),
        Eu(e, t, r, o, n);
    case 1:
        return r = t.type,
        o = t.pendingProps,
        o = t.elementType === r ? o : Bt(r, o),
        th(e, t, r, o, n);
    case 3:
        e: {
            if (gg(t),
            e === null)
                throw Error(_(387));
            r = t.pendingProps,
            s = t.memoizedState,
            o = s.element,
            Vv(e, t),
            Ki(t, r, null, n);
            var i = t.memoizedState;
            if (r = i.element,
            s.isDehydrated)
                if (s = {
                    element: r,
                    isDehydrated: !1,
                    cache: i.cache,
                    pendingSuspenseBoundaries: i.pendingSuspenseBoundaries,
                    transitions: i.transitions
                },
                t.updateQueue.baseState = s,
                t.memoizedState = s,
                t.flags & 256) {
                    o = ts(Error(_(423)), t),
                    t = nh(e, t, r, n, o);
                    break e
                } else if (r !== o) {
                    o = ts(Error(_(424)), t),
                    t = nh(e, t, r, n, o);
                    break e
                } else
                    for (gt = fr(t.stateNode.containerInfo.firstChild),
                    yt = t,
                    je = !0,
                    Yt = null,
                    n = Wv(t, null, r, n),
                    t.child = n; n; )
                        n.flags = n.flags & -3 | 4096,
                        n = n.sibling;
            else {
                if (Jo(),
                r === o) {
                    t = In(e, t, n);
                    break e
                }
                et(e, t, r, n)
            }
            t = t.child
        }
        return t;
    case 5:
        return Uv(t),
        e === null && Nu(t),
        r = t.type,
        o = t.pendingProps,
        s = e !== null ? e.memoizedProps : null,
        i = o.children,
        gu(r, o) ? i = null : s !== null && gu(r, s) && (t.flags |= 32),
        vg(e, t),
        et(e, t, i, n),
        t.child;
    case 6:
        return e === null && Nu(t),
        null;
    case 13:
        return yg(e, t, n);
    case 4:
        return Yd(t, t.stateNode.containerInfo),
        r = t.pendingProps,
        e === null ? t.child = Zo(t, null, r, n) : et(e, t, r, n),
        t.child;
    case 11:
        return r = t.type,
        o = t.pendingProps,
        o = t.elementType === r ? o : Bt(r, o),
        Zm(e, t, r, o, n);
    case 7:
        return et(e, t, t.pendingProps, n),
        t.child;
    case 8:
        return et(e, t, t.pendingProps.children, n),
        t.child;
    case 12:
        return et(e, t, t.pendingProps.children, n),
        t.child;
    case 10:
        e: {
            if (r = t.type._context,
            o = t.pendingProps,
            s = t.memoizedProps,
            i = o.value,
            ge(Ui, r._currentValue),
            r._currentValue = i,
            s !== null)
                if (Jt(s.value, i)) {
                    if (s.children === o.children && !dt.current) {
                        t = In(e, t, n);
                        break e
                    }
                } else
                    for (s = t.child,
                    s !== null && (s.return = t); s !== null; ) {
                        var l = s.dependencies;
                        if (l !== null) {
                            i = s.child;
                            for (var c = l.firstContext; c !== null; ) {
                                if (c.context === r) {
                                    if (s.tag === 1) {
                                        c = Rn(-1, n & -n),
                                        c.tag = 2;
                                        var u = s.updateQueue;
                                        if (u !== null) {
                                            u = u.shared;
                                            var d = u.pending;
                                            d === null ? c.next = c : (c.next = d.next,
                                            d.next = c),
                                            u.pending = c
                                        }
                                    }
                                    s.lanes |= n,
                                    c = s.alternate,
                                    c !== null && (c.lanes |= n),
                                    Su(s.return, n, t),
                                    l.lanes |= n;
                                    break
                                }
                                c = c.next
                            }
                        } else if (s.tag === 10)
                            i = s.type === t.type ? null : s.child;
                        else if (s.tag === 18) {
                            if (i = s.return,
                            i === null)
                                throw Error(_(341));
                            i.lanes |= n,
                            l = i.alternate,
                            l !== null && (l.lanes |= n),
                            Su(i, n, t),
                            i = s.sibling
                        } else
                            i = s.child;
                        if (i !== null)
                            i.return = s;
                        else
                            for (i = s; i !== null; ) {
                                if (i === t) {
                                    i = null;
                                    break
                                }
                                if (s = i.sibling,
                                s !== null) {
                                    s.return = i.return,
                                    i = s;
                                    break
                                }
                                i = i.return
                            }
                        s = i
                    }
            et(e, t, o.children, n),
            t = t.child
        }
        return t;
    case 9:
        return o = t.type,
        r = t.pendingProps.children,
        Io(t, n),
        o = Dt(o),
        r = r(o),
        t.flags |= 1,
        et(e, t, r, n),
        t.child;
    case 14:
        return r = t.type,
        o = Bt(r, t.pendingProps),
        o = Bt(r.type, o),
        eh(e, t, r, o, n);
    case 15:
        return hg(e, t, t.type, t.pendingProps, n);
    case 17:
        return r = t.type,
        o = t.pendingProps,
        o = t.elementType === r ? o : Bt(r, o),
        bi(e, t),
        t.tag = 1,
        ft(r) ? (e = !0,
        Wi(t)) : e = !1,
        Io(t, n),
        dg(t, r, o),
        Cu(t, r, o, n),
        Pu(null, t, r, !0, e, n);
    case 19:
        return xg(e, t, n);
    case 22:
        return pg(e, t, n)
    }
    throw Error(_(156, t.tag))
}
;
function Ag(e, t) {
    return lv(e, t)
}
function iN(e, t, n, r) {
    this.tag = e,
    this.key = n,
    this.sibling = this.child = this.return = this.stateNode = this.type = this.elementType = null,
    this.index = 0,
    this.ref = null,
    this.pendingProps = t,
    this.dependencies = this.memoizedState = this.updateQueue = this.memoizedProps = null,
    this.mode = r,
    this.subtreeFlags = this.flags = 0,
    this.deletions = null,
    this.childLanes = this.lanes = 0,
    this.alternate = null
}
function Tt(e, t, n, r) {
    return new iN(e,t,n,r)
}
function lf(e) {
    return e = e.prototype,
    !(!e || !e.isReactComponent)
}
function lN(e) {
    if (typeof e == "function")
        return lf(e) ? 1 : 0;
    if (e != null) {
        if (e = e.$$typeof,
        e === kd)
            return 11;
        if (e === Ed)
            return 14
    }
    return 2
}
function vr(e, t) {
    var n = e.alternate;
    return n === null ? (n = Tt(e.tag, t, e.key, e.mode),
    n.elementType = e.elementType,
    n.type = e.type,
    n.stateNode = e.stateNode,
    n.alternate = e,
    e.alternate = n) : (n.pendingProps = t,
    n.type = e.type,
    n.flags = 0,
    n.subtreeFlags = 0,
    n.deletions = null),
    n.flags = e.flags & 14680064,
    n.childLanes = e.childLanes,
    n.lanes = e.lanes,
    n.child = e.child,
    n.memoizedProps = e.memoizedProps,
    n.memoizedState = e.memoizedState,
    n.updateQueue = e.updateQueue,
    t = e.dependencies,
    n.dependencies = t === null ? null : {
        lanes: t.lanes,
        firstContext: t.firstContext
    },
    n.sibling = e.sibling,
    n.index = e.index,
    n.ref = e.ref,
    n
}
function ji(e, t, n, r, o, s) {
    var i = 2;
    if (r = e,
    typeof e == "function")
        lf(e) && (i = 1);
    else if (typeof e == "string")
        i = 5;
    else
        e: switch (e) {
        case bo:
            return Yr(n.children, o, s, t);
        case Cd:
            i = 8,
            o |= 8;
            break;
        case Gc:
            return e = Tt(12, n, t, o | 2),
            e.elementType = Gc,
            e.lanes = s,
            e;
        case qc:
            return e = Tt(13, n, t, o),
            e.elementType = qc,
            e.lanes = s,
            e;
        case Xc:
            return e = Tt(19, n, t, o),
            e.elementType = Xc,
            e.lanes = s,
            e;
        case Up:
            return kl(n, o, s, t);
        default:
            if (typeof e == "object" && e !== null)
                switch (e.$$typeof) {
                case Hp:
                    i = 10;
                    break e;
                case Vp:
                    i = 9;
                    break e;
                case kd:
                    i = 11;
                    break e;
                case Ed:
                    i = 14;
                    break e;
                case qn:
                    i = 16,
                    r = null;
                    break e
                }
            throw Error(_(130, e == null ? e : typeof e, ""))
        }
    return t = Tt(i, n, t, o),
    t.elementType = e,
    t.type = r,
    t.lanes = s,
    t
}
function Yr(e, t, n, r) {
    return e = Tt(7, e, r, t),
    e.lanes = n,
    e
}
function kl(e, t, n, r) {
    return e = Tt(22, e, r, t),
    e.elementType = Up,
    e.lanes = n,
    e.stateNode = {
        isHidden: !1
    },
    e
}
function jc(e, t, n) {
    return e = Tt(6, e, null, t),
    e.lanes = n,
    e
}
function Cc(e, t, n) {
    return t = Tt(4, e.children !== null ? e.children : [], e.key, t),
    t.lanes = n,
    t.stateNode = {
        containerInfo: e.containerInfo,
        pendingChildren: null,
        implementation: e.implementation
    },
    t
}
function cN(e, t, n, r, o) {
    this.tag = t,
    this.containerInfo = e,
    this.finishedWork = this.pingCache = this.current = this.pendingChildren = null,
    this.timeoutHandle = -1,
    this.callbackNode = this.pendingContext = this.context = null,
    this.callbackPriority = 0,
    this.eventTimes = sc(0),
    this.expirationTimes = sc(-1),
    this.entangledLanes = this.finishedLanes = this.mutableReadLanes = this.expiredLanes = this.pingedLanes = this.suspendedLanes = this.pendingLanes = 0,
    this.entanglements = sc(0),
    this.identifierPrefix = r,
    this.onRecoverableError = o,
    this.mutableSourceEagerHydrationData = null
}
function cf(e, t, n, r, o, s, i, l, c) {
    return e = new cN(e,t,n,l,c),
    t === 1 ? (t = 1,
    s === !0 && (t |= 8)) : t = 0,
    s = Tt(3, null, null, t),
    e.current = s,
    s.stateNode = e,
    s.memoizedState = {
        element: r,
        isDehydrated: n,
        cache: null,
        transitions: null,
        pendingSuspenseBoundaries: null
    },
    Ud(s),
    e
}
function uN(e, t, n) {
    var r = 3 < arguments.length && arguments[3] !== void 0 ? arguments[3] : null;
    return {
        $$typeof: wo,
        key: r == null ? null : "" + r,
        children: e,
        containerInfo: t,
        implementation: n
    }
}
function Ig(e) {
    if (!e)
        return xr;
    e = e._reactInternals;
    e: {
        if (so(e) !== e || e.tag !== 1)
            throw Error(_(170));
        var t = e;
        do {
            switch (t.tag) {
            case 3:
                t = t.stateNode.context;
                break e;
            case 1:
                if (ft(t.type)) {
                    t = t.stateNode.__reactInternalMemoizedMergedChildContext;
                    break e
                }
            }
            t = t.return
        } while (t !== null);
        throw Error(_(171))
    }
    if (e.tag === 1) {
        var n = e.type;
        if (ft(n))
            return Iv(e, n, t)
    }
    return t
}
function Lg(e, t, n, r, o, s, i, l, c) {
    return e = cf(n, r, !0, e, o, s, i, l, c),
    e.context = Ig(null),
    n = e.current,
    r = ot(),
    o = pr(n),
    s = Rn(r, o),
    s.callback = t ?? null,
    mr(n, s, o),
    e.current.lanes = o,
    Ca(e, o, r),
    mt(e, r),
    e
}
function El(e, t, n, r) {
    var o = t.current
      , s = ot()
      , i = pr(o);
    return n = Ig(n),
    t.context === null ? t.context = n : t.pendingContext = n,
    t = Rn(s, i),
    t.payload = {
        element: e
    },
    r = r === void 0 ? null : r,
    r !== null && (t.callback = r),
    e = mr(o, t, i),
    e !== null && (qt(e, o, i, s),
    yi(e, o, i)),
    i
}
function tl(e) {
    if (e = e.current,
    !e.child)
        return null;
    switch (e.child.tag) {
    case 5:
        return e.child.stateNode;
    default:
        return e.child.stateNode
    }
}
function fh(e, t) {
    if (e = e.memoizedState,
    e !== null && e.dehydrated !== null) {
        var n = e.retryLane;
        e.retryLane = n !== 0 && n < t ? n : t
    }
}
function uf(e, t) {
    fh(e, t),
    (e = e.alternate) && fh(e, t)
}
function dN() {
    return null
}
var Fg = typeof reportError == "function" ? reportError : function(e) {
    console.error(e)
}
;
function df(e) {
    this._internalRoot = e
}
Pl.prototype.render = df.prototype.render = function(e) {
    var t = this._internalRoot;
    if (t === null)
        throw Error(_(409));
    El(e, t, null, null)
}
;
Pl.prototype.unmount = df.prototype.unmount = function() {
    var e = this._internalRoot;
    if (e !== null) {
        this._internalRoot = null;
        var t = e.containerInfo;
        Xr(function() {
            El(null, e, null, null)
        }),
        t[On] = null
    }
}
;
function Pl(e) {
    this._internalRoot = e
}
Pl.prototype.unstable_scheduleHydration = function(e) {
    if (e) {
        var t = pv();
        e = {
            blockedOn: null,
            target: e,
            priority: t
        };
        for (var n = 0; n < Jn.length && t !== 0 && t < Jn[n].priority; n++)
            ;
        Jn.splice(n, 0, e),
        n === 0 && gv(e)
    }
}
;
function ff(e) {
    return !(!e || e.nodeType !== 1 && e.nodeType !== 9 && e.nodeType !== 11)
}
function Tl(e) {
    return !(!e || e.nodeType !== 1 && e.nodeType !== 9 && e.nodeType !== 11 && (e.nodeType !== 8 || e.nodeValue !== " react-mount-point-unstable "))
}
function mh() {}
function fN(e, t, n, r, o) {
    if (o) {
        if (typeof r == "function") {
            var s = r;
            r = function() {
                var u = tl(i);
                s.call(u)
            }
        }
        var i = Lg(t, r, e, 0, null, !1, !1, "", mh);
        return e._reactRootContainer = i,
        e[On] = i.current,
        oa(e.nodeType === 8 ? e.parentNode : e),
        Xr(),
        i
    }
    for (; o = e.lastChild; )
        e.removeChild(o);
    if (typeof r == "function") {
        var l = r;
        r = function() {
            var u = tl(c);
            l.call(u)
        }
    }
    var c = cf(e, 0, !1, null, null, !1, !1, "", mh);
    return e._reactRootContainer = c,
    e[On] = c.current,
    oa(e.nodeType === 8 ? e.parentNode : e),
    Xr(function() {
        El(t, c, n, r)
    }),
    c
}
function Ml(e, t, n, r, o) {
    var s = n._reactRootContainer;
    if (s) {
        var i = s;
        if (typeof o == "function") {
            var l = o;
            o = function() {
                var c = tl(i);
                l.call(c)
            }
        }
        El(t, i, e, o)
    } else
        i = fN(n, t, e, o, r);
    return tl(i)
}
mv = function(e) {
    switch (e.tag) {
    case 3:
        var t = e.stateNode;
        if (t.current.memoizedState.isDehydrated) {
            var n = Ls(t.pendingLanes);
            n !== 0 && (Md(t, n | 1),
            mt(t, Oe()),
            !(ie & 6) && (ns = Oe() + 500,
            Cr()))
        }
        break;
    case 13:
        Xr(function() {
            var r = An(e, 1);
            if (r !== null) {
                var o = ot();
                qt(r, e, 1, o)
            }
        }),
        uf(e, 1)
    }
}
;
Rd = function(e) {
    if (e.tag === 13) {
        var t = An(e, 134217728);
        if (t !== null) {
            var n = ot();
            qt(t, e, 134217728, n)
        }
        uf(e, 134217728)
    }
}
;
hv = function(e) {
    if (e.tag === 13) {
        var t = pr(e)
          , n = An(e, t);
        if (n !== null) {
            var r = ot();
            qt(n, e, t, r)
        }
        uf(e, t)
    }
}
;
pv = function() {
    return pe
}
;
vv = function(e, t) {
    var n = pe;
    try {
        return pe = e,
        t()
    } finally {
        pe = n
    }
}
;
iu = function(e, t, n) {
    switch (t) {
    case "input":
        if (eu(e, n),
        t = n.name,
        n.type === "radio" && t != null) {
            for (n = e; n.parentNode; )
                n = n.parentNode;
            for (n = n.querySelectorAll("input[name=" + JSON.stringify("" + t) + '][type="radio"]'),
            t = 0; t < n.length; t++) {
                var r = n[t];
                if (r !== e && r.form === e.form) {
                    var o = wl(r);
                    if (!o)
                        throw Error(_(90));
                    Kp(r),
                    eu(r, o)
                }
            }
        }
        break;
    case "textarea":
        Gp(e, n);
        break;
    case "select":
        t = n.value,
        t != null && _o(e, !!n.multiple, t, !1)
    }
}
;
nv = of;
rv = Xr;
var mN = {
    usingClientEntryPoint: !1,
    Events: [Ea, Co, wl, ev, tv, of]
}
  , Ms = {
    findFiberByHostInstance: Ir,
    bundleType: 0,
    version: "18.3.1",
    rendererPackageName: "react-dom"
}
  , hN = {
    bundleType: Ms.bundleType,
    version: Ms.version,
    rendererPackageName: Ms.rendererPackageName,
    rendererConfig: Ms.rendererConfig,
    overrideHookState: null,
    overrideHookStateDeletePath: null,
    overrideHookStateRenamePath: null,
    overrideProps: null,
    overridePropsDeletePath: null,
    overridePropsRenamePath: null,
    setErrorHandler: null,
    setSuspenseHandler: null,
    scheduleUpdate: null,
    currentDispatcherRef: zn.ReactCurrentDispatcher,
    findHostInstanceByFiber: function(e) {
        return e = av(e),
        e === null ? null : e.stateNode
    },
    findFiberByHostInstance: Ms.findFiberByHostInstance || dN,
    findHostInstancesForRefresh: null,
    scheduleRefresh: null,
    scheduleRoot: null,
    setRefreshHandler: null,
    getCurrentFiber: null,
    reconcilerVersion: "18.3.1-next-f1338f8080-20240426"
};
if (typeof __REACT_DEVTOOLS_GLOBAL_HOOK__ < "u") {
    var ri = __REACT_DEVTOOLS_GLOBAL_HOOK__;
    if (!ri.isDisabled && ri.supportsFiber)
        try {
            vl = ri.inject(hN),
            pn = ri
        } catch {}
}
Nt.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED = mN;
Nt.createPortal = function(e, t) {
    var n = 2 < arguments.length && arguments[2] !== void 0 ? arguments[2] : null;
    if (!ff(t))
        throw Error(_(200));
    return uN(e, t, null, n)
}
;
Nt.createRoot = function(e, t) {
    if (!ff(e))
        throw Error(_(299));
    var n = !1
      , r = ""
      , o = Fg;
    return t != null && (t.unstable_strictMode === !0 && (n = !0),
    t.identifierPrefix !== void 0 && (r = t.identifierPrefix),
    t.onRecoverableError !== void 0 && (o = t.onRecoverableError)),
    t = cf(e, 1, !1, null, null, n, !1, r, o),
    e[On] = t.current,
    oa(e.nodeType === 8 ? e.parentNode : e),
    new df(t)
}
;
Nt.findDOMNode = function(e) {
    if (e == null)
        return null;
    if (e.nodeType === 1)
        return e;
    var t = e._reactInternals;
    if (t === void 0)
        throw typeof e.render == "function" ? Error(_(188)) : (e = Object.keys(e).join(","),
        Error(_(268, e)));
    return e = av(t),
    e = e === null ? null : e.stateNode,
    e
}
;
Nt.flushSync = function(e) {
    return Xr(e)
}
;
Nt.hydrate = function(e, t, n) {
    if (!Tl(t))
        throw Error(_(200));
    return Ml(null, e, t, !0, n)
}
;
Nt.hydrateRoot = function(e, t, n) {
    if (!ff(e))
        throw Error(_(405));
    var r = n != null && n.hydratedSources || null
      , o = !1
      , s = ""
      , i = Fg;
    if (n != null && (n.unstable_strictMode === !0 && (o = !0),
    n.identifierPrefix !== void 0 && (s = n.identifierPrefix),
    n.onRecoverableError !== void 0 && (i = n.onRecoverableError)),
    t = Lg(t, null, e, 1, n ?? null, o, !1, s, i),
    e[On] = t.current,
    oa(e),
    r)
        for (e = 0; e < r.length; e++)
            n = r[e],
            o = n._getVersion,
            o = o(n._source),
            t.mutableSourceEagerHydrationData == null ? t.mutableSourceEagerHydrationData = [n, o] : t.mutableSourceEagerHydrationData.push(n, o);
    return new Pl(t)
}
;
Nt.render = function(e, t, n) {
    if (!Tl(t))
        throw Error(_(200));
    return Ml(null, e, t, !1, n)
}
;
Nt.unmountComponentAtNode = function(e) {
    if (!Tl(e))
        throw Error(_(40));
    return e._reactRootContainer ? (Xr(function() {
        Ml(null, null, e, !1, function() {
            e._reactRootContainer = null,
            e[On] = null
        })
    }),
    !0) : !1
}
;
Nt.unstable_batchedUpdates = of;
Nt.unstable_renderSubtreeIntoContainer = function(e, t, n, r) {
    if (!Tl(n))
        throw Error(_(200));
    if (e == null || e._reactInternals === void 0)
        throw Error(_(38));
    return Ml(e, t, n, !1, r)
}
;
Nt.version = "18.3.1-next-f1338f8080-20240426";
function zg() {
    if (!(typeof __REACT_DEVTOOLS_GLOBAL_HOOK__ > "u" || typeof __REACT_DEVTOOLS_GLOBAL_HOOK__.checkDCE != "function"))
        try {
            __REACT_DEVTOOLS_GLOBAL_HOOK__.checkDCE(zg)
        } catch (e) {
            console.error(e)
        }
}
zg(),
zp.exports = Nt;
var ao = zp.exports;
const $g = Ep(ao);
var Bg, hh = ao;
Bg = hh.createRoot,
hh.hydrateRoot;
const pN = 1
  , vN = 1e6;
let kc = 0;
function gN() {
    return kc = (kc + 1) % Number.MAX_SAFE_INTEGER,
    kc.toString()
}
const Ec = new Map
  , ph = e => {
    if (Ec.has(e))
        return;
    const t = setTimeout( () => {
        Ec.delete(e),
        Gs({
            type: "REMOVE_TOAST",
            toastId: e
        })
    }
    , vN);
    Ec.set(e, t)
}
  , yN = (e, t) => {
    switch (t.type) {
    case "ADD_TOAST":
        return {
            ...e,
            toasts: [t.toast, ...e.toasts].slice(0, pN)
        };
    case "UPDATE_TOAST":
        return {
            ...e,
            toasts: e.toasts.map(n => n.id === t.toast.id ? {
                ...n,
                ...t.toast
            } : n)
        };
    case "DISMISS_TOAST":
        {
            const {toastId: n} = t;
            return n ? ph(n) : e.toasts.forEach(r => {
                ph(r.id)
            }
            ),
            {
                ...e,
                toasts: e.toasts.map(r => r.id === n || n === void 0 ? {
                    ...r,
                    open: !1
                } : r)
            }
        }
    case "REMOVE_TOAST":
        return t.toastId === void 0 ? {
            ...e,
            toasts: []
        } : {
            ...e,
            toasts: e.toasts.filter(n => n.id !== t.toastId)
        }
    }
}
  , Ci = [];
let ki = {
    toasts: []
};
function Gs(e) {
    ki = yN(ki, e),
    Ci.forEach(t => {
        t(ki)
    }
    )
}
function xN({...e}) {
    const t = gN()
      , n = o => Gs({
        type: "UPDATE_TOAST",
        toast: {
            ...o,
            id: t
        }
    })
      , r = () => Gs({
        type: "DISMISS_TOAST",
        toastId: t
    });
    return Gs({
        type: "ADD_TOAST",
        toast: {
            ...e,
            id: t,
            open: !0,
            onOpenChange: o => {
                o || r()
            }
        }
    }),
    {
        id: t,
        dismiss: r,
        update: n
    }
}
function wN() {
    const [e,t] = m.useState(ki);
    return m.useEffect( () => (Ci.push(t),
    () => {
        const n = Ci.indexOf(t);
        n > -1 && Ci.splice(n, 1)
    }
    ), [e]),
    {
        ...e,
        toast: xN,
        dismiss: n => Gs({
            type: "DISMISS_TOAST",
            toastId: n
        })
    }
}
function Q(e, t, {checkForDefaultPrevented: n=!0}={}) {
    return function(o) {
        if (e == null || e(o),
        n === !1 || !o.defaultPrevented)
            return t == null ? void 0 : t(o)
    }
}
function vh(e, t) {
    if (typeof e == "function")
        return e(t);
    e != null && (e.current = t)
}
function Wg(...e) {
    return t => {
        let n = !1;
        const r = e.map(o => {
            const s = vh(o, t);
            return !n && typeof s == "function" && (n = !0),
            s
        }
        );
        if (n)
            return () => {
                for (let o = 0; o < r.length; o++) {
                    const s = r[o];
                    typeof s == "function" ? s() : vh(e[o], null)
                }
            }
    }
}
function fe(...e) {
    return m.useCallback(Wg(...e), e)
}
function bN(e, t) {
    const n = m.createContext(t)
      , r = s => {
        const {children: i, ...l} = s
          , c = m.useMemo( () => l, Object.values(l));
        return a.jsx(n.Provider, {
            value: c,
            children: i
        })
    }
    ;
    r.displayName = e + "Provider";
    function o(s) {
        const i = m.useContext(n);
        if (i)
            return i;
        if (t !== void 0)
            return t;
        throw new Error(`\`${s}\` must be used within \`${e}\``)
    }
    return [r, o]
}
function io(e, t=[]) {
    let n = [];
    function r(s, i) {
        const l = m.createContext(i)
          , c = n.length;
        n = [...n, i];
        const u = f => {
            var y;
            const {scope: g, children: h, ...b} = f
              , v = ((y = g == null ? void 0 : g[e]) == null ? void 0 : y[c]) || l
              , w = m.useMemo( () => b, Object.values(b));
            return a.jsx(v.Provider, {
                value: w,
                children: h
            })
        }
        ;
        u.displayName = s + "Provider";
        function d(f, g) {
            var v;
            const h = ((v = g == null ? void 0 : g[e]) == null ? void 0 : v[c]) || l
              , b = m.useContext(h);
            if (b)
                return b;
            if (i !== void 0)
                return i;
            throw new Error(`\`${f}\` must be used within \`${s}\``)
        }
        return [u, d]
    }
    const o = () => {
        const s = n.map(i => m.createContext(i));
        return function(l) {
            const c = (l == null ? void 0 : l[e]) || s;
            return m.useMemo( () => ({
                [`__scope${e}`]: {
                    ...l,
                    [e]: c
                }
            }), [l, c])
        }
    }
    ;
    return o.scopeName = e,
    [r, NN(o, ...t)]
}
function NN(...e) {
    const t = e[0];
    if (e.length === 1)
        return t;
    const n = () => {
        const r = e.map(o => ({
            useScope: o(),
            scopeName: o.scopeName
        }));
        return function(s) {
            const i = r.reduce( (l, {useScope: c, scopeName: u}) => {
                const f = c(s)[`__scope${u}`];
                return {
                    ...l,
                    ...f
                }
            }
            , {});
            return m.useMemo( () => ({
                [`__scope${t.scopeName}`]: i
            }), [i])
        }
    }
    ;
    return n.scopeName = t.scopeName,
    n
}
function rs(e) {
    const t = jN(e)
      , n = m.forwardRef( (r, o) => {
        const {children: s, ...i} = r
          , l = m.Children.toArray(s)
          , c = l.find(kN);
        if (c) {
            const u = c.props.children
              , d = l.map(f => f === c ? m.Children.count(u) > 1 ? m.Children.only(null) : m.isValidElement(u) ? u.props.children : null : f);
            return a.jsx(t, {
                ...i,
                ref: o,
                children: m.isValidElement(u) ? m.cloneElement(u, void 0, d) : null
            })
        }
        return a.jsx(t, {
            ...i,
            ref: o,
            children: s
        })
    }
    );
    return n.displayName = `${e}.Slot`,
    n
}
var SN = rs("Slot");
function jN(e) {
    const t = m.forwardRef( (n, r) => {
        const {children: o, ...s} = n;
        if (m.isValidElement(o)) {
            const i = PN(o)
              , l = EN(s, o.props);
            return o.type !== m.Fragment && (l.ref = r ? Wg(r, i) : i),
            m.cloneElement(o, l)
        }
        return m.Children.count(o) > 1 ? m.Children.only(null) : null
    }
    );
    return t.displayName = `${e}.SlotClone`,
    t
}
var Hg = Symbol("radix.slottable");
function CN(e) {
    const t = ({children: n}) => a.jsx(a.Fragment, {
        children: n
    });
    return t.displayName = `${e}.Slottable`,
    t.__radixId = Hg,
    t
}
function kN(e) {
    return m.isValidElement(e) && typeof e.type == "function" && "__radixId"in e.type && e.type.__radixId === Hg
}
function EN(e, t) {
    const n = {
        ...t
    };
    for (const r in t) {
        const o = e[r]
          , s = t[r];
        /^on[A-Z]/.test(r) ? o && s ? n[r] = (...l) => {
            const c = s(...l);
            return o(...l),
            c
        }
        : o && (n[r] = o) : r === "style" ? n[r] = {
            ...o,
            ...s
        } : r === "className" && (n[r] = [o, s].filter(Boolean).join(" "))
    }
    return {
        ...e,
        ...n
    }
}
function PN(e) {
    var r, o;
    let t = (r = Object.getOwnPropertyDescriptor(e.props, "ref")) == null ? void 0 : r.get
      , n = t && "isReactWarning"in t && t.isReactWarning;
    return n ? e.ref : (t = (o = Object.getOwnPropertyDescriptor(e, "ref")) == null ? void 0 : o.get,
    n = t && "isReactWarning"in t && t.isReactWarning,
    n ? e.props.ref : e.props.ref || e.ref)
}
function mf(e) {
    const t = e + "CollectionProvider"
      , [n,r] = io(t)
      , [o,s] = n(t, {
        collectionRef: {
            current: null
        },
        itemMap: new Map
    })
      , i = v => {
        const {scope: w, children: y} = v
          , p = I.useRef(null)
          , x = I.useRef(new Map).current;
        return a.jsx(o, {
            scope: w,
            itemMap: x,
            collectionRef: p,
            children: y
        })
    }
    ;
    i.displayName = t;
    const l = e + "CollectionSlot"
      , c = rs(l)
      , u = I.forwardRef( (v, w) => {
        const {scope: y, children: p} = v
          , x = s(l, y)
          , N = fe(w, x.collectionRef);
        return a.jsx(c, {
            ref: N,
            children: p
        })
    }
    );
    u.displayName = l;
    const d = e + "CollectionItemSlot"
      , f = "data-radix-collection-item"
      , g = rs(d)
      , h = I.forwardRef( (v, w) => {
        const {scope: y, children: p, ...x} = v
          , N = I.useRef(null)
          , S = fe(w, N)
          , k = s(d, y);
        return I.useEffect( () => (k.itemMap.set(N, {
            ref: N,
            ...x
        }),
        () => void k.itemMap.delete(N))),
        a.jsx(g, {
            [f]: "",
            ref: S,
            children: p
        })
    }
    );
    h.displayName = d;
    function b(v) {
        const w = s(e + "CollectionConsumer", v);
        return I.useCallback( () => {
            const p = w.collectionRef.current;
            if (!p)
                return [];
            const x = Array.from(p.querySelectorAll(`[${f}]`));
            return Array.from(w.itemMap.values()).sort( (k, C) => x.indexOf(k.ref.current) - x.indexOf(C.ref.current))
        }
        , [w.collectionRef, w.itemMap])
    }
    return [{
        Provider: i,
        Slot: u,
        ItemSlot: h
    }, b, r]
}
var TN = ["a", "button", "div", "form", "h2", "h3", "img", "input", "label", "li", "nav", "ol", "p", "select", "span", "svg", "ul"]
  , te = TN.reduce( (e, t) => {
    const n = rs(`Primitive.${t}`)
      , r = m.forwardRef( (o, s) => {
        const {asChild: i, ...l} = o
          , c = i ? n : t;
        return typeof window < "u" && (window[Symbol.for("radix-ui")] = !0),
        a.jsx(c, {
            ...l,
            ref: s
        })
    }
    );
    return r.displayName = `Primitive.${t}`,
    {
        ...e,
        [t]: r
    }
}
, {});
function Vg(e, t) {
    e && ao.flushSync( () => e.dispatchEvent(t))
}
function Zt(e) {
    const t = m.useRef(e);
    return m.useEffect( () => {
        t.current = e
    }
    ),
    m.useMemo( () => (...n) => {
        var r;
        return (r = t.current) == null ? void 0 : r.call(t, ...n)
    }
    , [])
}
function MN(e, t=globalThis == null ? void 0 : globalThis.document) {
    const n = Zt(e);
    m.useEffect( () => {
        const r = o => {
            o.key === "Escape" && n(o)
        }
        ;
        return t.addEventListener("keydown", r, {
            capture: !0
        }),
        () => t.removeEventListener("keydown", r, {
            capture: !0
        })
    }
    , [n, t])
}
var RN = "DismissableLayer", $u = "dismissableLayer.update", _N = "dismissableLayer.pointerDownOutside", DN = "dismissableLayer.focusOutside", gh, Ug = m.createContext({
    layers: new Set,
    layersWithOutsidePointerEventsDisabled: new Set,
    branches: new Set
}), Ta = m.forwardRef( (e, t) => {
    const {disableOutsidePointerEvents: n=!1, onEscapeKeyDown: r, onPointerDownOutside: o, onFocusOutside: s, onInteractOutside: i, onDismiss: l, ...c} = e
      , u = m.useContext(Ug)
      , [d,f] = m.useState(null)
      , g = (d == null ? void 0 : d.ownerDocument) ?? (globalThis == null ? void 0 : globalThis.document)
      , [,h] = m.useState({})
      , b = fe(t, C => f(C))
      , v = Array.from(u.layers)
      , [w] = [...u.layersWithOutsidePointerEventsDisabled].slice(-1)
      , y = v.indexOf(w)
      , p = d ? v.indexOf(d) : -1
      , x = u.layersWithOutsidePointerEventsDisabled.size > 0
      , N = p >= y
      , S = AN(C => {
        const T = C.target
          , D = [...u.branches].some(R => R.contains(T));
        !N || D || (o == null || o(C),
        i == null || i(C),
        C.defaultPrevented || l == null || l())
    }
    , g)
      , k = IN(C => {
        const T = C.target;
        [...u.branches].some(R => R.contains(T)) || (s == null || s(C),
        i == null || i(C),
        C.defaultPrevented || l == null || l())
    }
    , g);
    return MN(C => {
        p === u.layers.size - 1 && (r == null || r(C),
        !C.defaultPrevented && l && (C.preventDefault(),
        l()))
    }
    , g),
    m.useEffect( () => {
        if (d)
            return n && (u.layersWithOutsidePointerEventsDisabled.size === 0 && (gh = g.body.style.pointerEvents,
            g.body.style.pointerEvents = "none"),
            u.layersWithOutsidePointerEventsDisabled.add(d)),
            u.layers.add(d),
            yh(),
            () => {
                n && u.layersWithOutsidePointerEventsDisabled.size === 1 && (g.body.style.pointerEvents = gh)
            }
    }
    , [d, g, n, u]),
    m.useEffect( () => () => {
        d && (u.layers.delete(d),
        u.layersWithOutsidePointerEventsDisabled.delete(d),
        yh())
    }
    , [d, u]),
    m.useEffect( () => {
        const C = () => h({});
        return document.addEventListener($u, C),
        () => document.removeEventListener($u, C)
    }
    , []),
    a.jsx(te.div, {
        ...c,
        ref: b,
        style: {
            pointerEvents: x ? N ? "auto" : "none" : void 0,
            ...e.style
        },
        onFocusCapture: Q(e.onFocusCapture, k.onFocusCapture),
        onBlurCapture: Q(e.onBlurCapture, k.onBlurCapture),
        onPointerDownCapture: Q(e.onPointerDownCapture, S.onPointerDownCapture)
    })
}
);
Ta.displayName = RN;
var ON = "DismissableLayerBranch"
  , Yg = m.forwardRef( (e, t) => {
    const n = m.useContext(Ug)
      , r = m.useRef(null)
      , o = fe(t, r);
    return m.useEffect( () => {
        const s = r.current;
        if (s)
            return n.branches.add(s),
            () => {
                n.branches.delete(s)
            }
    }
    , [n.branches]),
    a.jsx(te.div, {
        ...e,
        ref: o
    })
}
);
Yg.displayName = ON;
function AN(e, t=globalThis == null ? void 0 : globalThis.document) {
    const n = Zt(e)
      , r = m.useRef(!1)
      , o = m.useRef( () => {}
    );
    return m.useEffect( () => {
        const s = l => {
            if (l.target && !r.current) {
                let c = function() {
                    Kg(_N, n, u, {
                        discrete: !0
                    })
                };
                const u = {
                    originalEvent: l
                };
                l.pointerType === "touch" ? (t.removeEventListener("click", o.current),
                o.current = c,
                t.addEventListener("click", o.current, {
                    once: !0
                })) : c()
            } else
                t.removeEventListener("click", o.current);
            r.current = !1
        }
          , i = window.setTimeout( () => {
            t.addEventListener("pointerdown", s)
        }
        , 0);
        return () => {
            window.clearTimeout(i),
            t.removeEventListener("pointerdown", s),
            t.removeEventListener("click", o.current)
        }
    }
    , [t, n]),
    {
        onPointerDownCapture: () => r.current = !0
    }
}
function IN(e, t=globalThis == null ? void 0 : globalThis.document) {
    const n = Zt(e)
      , r = m.useRef(!1);
    return m.useEffect( () => {
        const o = s => {
            s.target && !r.current && Kg(DN, n, {
                originalEvent: s
            }, {
                discrete: !1
            })
        }
        ;
        return t.addEventListener("focusin", o),
        () => t.removeEventListener("focusin", o)
    }
    , [t, n]),
    {
        onFocusCapture: () => r.current = !0,
        onBlurCapture: () => r.current = !1
    }
}
function yh() {
    const e = new CustomEvent($u);
    document.dispatchEvent(e)
}
function Kg(e, t, n, {discrete: r}) {
    const o = n.originalEvent.target
      , s = new CustomEvent(e,{
        bubbles: !1,
        cancelable: !0,
        detail: n
    });
    t && o.addEventListener(e, t, {
        once: !0
    }),
    r ? Vg(o, s) : o.dispatchEvent(s)
}
var LN = Ta
  , FN = Yg
  , Ue = globalThis != null && globalThis.document ? m.useLayoutEffect : () => {}
  , zN = "Portal"
  , Rl = m.forwardRef( (e, t) => {
    var l;
    const {container: n, ...r} = e
      , [o,s] = m.useState(!1);
    Ue( () => s(!0), []);
    const i = n || o && ((l = globalThis == null ? void 0 : globalThis.document) == null ? void 0 : l.body);
    return i ? $g.createPortal(a.jsx(te.div, {
        ...r,
        ref: t
    }), i) : null
}
);
Rl.displayName = zN;
function $N(e, t) {
    return m.useReducer( (n, r) => t[n][r] ?? n, e)
}
var ms = e => {
    const {present: t, children: n} = e
      , r = BN(t)
      , o = typeof n == "function" ? n({
        present: r.isPresent
    }) : m.Children.only(n)
      , s = fe(r.ref, WN(o));
    return typeof n == "function" || r.isPresent ? m.cloneElement(o, {
        ref: s
    }) : null
}
;
ms.displayName = "Presence";
function BN(e) {
    const [t,n] = m.useState()
      , r = m.useRef(null)
      , o = m.useRef(e)
      , s = m.useRef("none")
      , i = e ? "mounted" : "unmounted"
      , [l,c] = $N(i, {
        mounted: {
            UNMOUNT: "unmounted",
            ANIMATION_OUT: "unmountSuspended"
        },
        unmountSuspended: {
            MOUNT: "mounted",
            ANIMATION_END: "unmounted"
        },
        unmounted: {
            MOUNT: "mounted"
        }
    });
    return m.useEffect( () => {
        const u = oi(r.current);
        s.current = l === "mounted" ? u : "none"
    }
    , [l]),
    Ue( () => {
        const u = r.current
          , d = o.current;
        if (d !== e) {
            const g = s.current
              , h = oi(u);
            e ? c("MOUNT") : h === "none" || (u == null ? void 0 : u.display) === "none" ? c("UNMOUNT") : c(d && g !== h ? "ANIMATION_OUT" : "UNMOUNT"),
            o.current = e
        }
    }
    , [e, c]),
    Ue( () => {
        if (t) {
            let u;
            const d = t.ownerDocument.defaultView ?? window
              , f = h => {
                const v = oi(r.current).includes(h.animationName);
                if (h.target === t && v && (c("ANIMATION_END"),
                !o.current)) {
                    const w = t.style.animationFillMode;
                    t.style.animationFillMode = "forwards",
                    u = d.setTimeout( () => {
                        t.style.animationFillMode === "forwards" && (t.style.animationFillMode = w)
                    }
                    )
                }
            }
              , g = h => {
                h.target === t && (s.current = oi(r.current))
            }
            ;
            return t.addEventListener("animationstart", g),
            t.addEventListener("animationcancel", f),
            t.addEventListener("animationend", f),
            () => {
                d.clearTimeout(u),
                t.removeEventListener("animationstart", g),
                t.removeEventListener("animationcancel", f),
                t.removeEventListener("animationend", f)
            }
        } else
            c("ANIMATION_END")
    }
    , [t, c]),
    {
        isPresent: ["mounted", "unmountSuspended"].includes(l),
        ref: m.useCallback(u => {
            r.current = u ? getComputedStyle(u) : null,
            n(u)
        }
        , [])
    }
}
function oi(e) {
    return (e == null ? void 0 : e.animationName) || "none"
}
function WN(e) {
    var r, o;
    let t = (r = Object.getOwnPropertyDescriptor(e.props, "ref")) == null ? void 0 : r.get
      , n = t && "isReactWarning"in t && t.isReactWarning;
    return n ? e.ref : (t = (o = Object.getOwnPropertyDescriptor(e, "ref")) == null ? void 0 : o.get,
    n = t && "isReactWarning"in t && t.isReactWarning,
    n ? e.props.ref : e.props.ref || e.ref)
}
var HN = bd[" useInsertionEffect ".trim().toString()] || Ue;
function ma({prop: e, defaultProp: t, onChange: n= () => {}
, caller: r}) {
    const [o,s,i] = VN({
        defaultProp: t,
        onChange: n
    })
      , l = e !== void 0
      , c = l ? e : o;
    {
        const d = m.useRef(e !== void 0);
        m.useEffect( () => {
            const f = d.current;
            f !== l && console.warn(`${r} is changing from ${f ? "controlled" : "uncontrolled"} to ${l ? "controlled" : "uncontrolled"}. Components should not switch from controlled to uncontrolled (or vice versa). Decide between using a controlled or uncontrolled value for the lifetime of the component.`),
            d.current = l
        }
        , [l, r])
    }
    const u = m.useCallback(d => {
        var f;
        if (l) {
            const g = UN(d) ? d(e) : d;
            g !== e && ((f = i.current) == null || f.call(i, g))
        } else
            s(d)
    }
    , [l, e, s, i]);
    return [c, u]
}
function VN({defaultProp: e, onChange: t}) {
    const [n,r] = m.useState(e)
      , o = m.useRef(n)
      , s = m.useRef(t);
    return HN( () => {
        s.current = t
    }
    , [t]),
    m.useEffect( () => {
        var i;
        o.current !== n && ((i = s.current) == null || i.call(s, n),
        o.current = n)
    }
    , [n, o]),
    [n, r, s]
}
function UN(e) {
    return typeof e == "function"
}
var Qg = Object.freeze({
    position: "absolute",
    border: 0,
    width: 1,
    height: 1,
    padding: 0,
    margin: -1,
    overflow: "hidden",
    clip: "rect(0, 0, 0, 0)",
    whiteSpace: "nowrap",
    wordWrap: "normal"
})
  , YN = "VisuallyHidden"
  , _l = m.forwardRef( (e, t) => a.jsx(te.span, {
    ...e,
    ref: t,
    style: {
        ...Qg,
        ...e.style
    }
}));
_l.displayName = YN;
var KN = _l
  , hf = "ToastProvider"
  , [pf,QN,GN] = mf("Toast")
  , [Gg,NR] = io("Toast", [GN])
  , [qN,Dl] = Gg(hf)
  , qg = e => {
    const {__scopeToast: t, label: n="Notification", duration: r=5e3, swipeDirection: o="right", swipeThreshold: s=50, children: i} = e
      , [l,c] = m.useState(null)
      , [u,d] = m.useState(0)
      , f = m.useRef(!1)
      , g = m.useRef(!1);
    return n.trim() || console.error(`Invalid prop \`label\` supplied to \`${hf}\`. Expected non-empty \`string\`.`),
    a.jsx(pf.Provider, {
        scope: t,
        children: a.jsx(qN, {
            scope: t,
            label: n,
            duration: r,
            swipeDirection: o,
            swipeThreshold: s,
            toastCount: u,
            viewport: l,
            onViewportChange: c,
            onToastAdd: m.useCallback( () => d(h => h + 1), []),
            onToastRemove: m.useCallback( () => d(h => h - 1), []),
            isFocusedToastEscapeKeyDownRef: f,
            isClosePausedRef: g,
            children: i
        })
    })
}
;
qg.displayName = hf;
var Xg = "ToastViewport"
  , XN = ["F8"]
  , Bu = "toast.viewportPause"
  , Wu = "toast.viewportResume"
  , Jg = m.forwardRef( (e, t) => {
    const {__scopeToast: n, hotkey: r=XN, label: o="Notifications ({hotkey})", ...s} = e
      , i = Dl(Xg, n)
      , l = QN(n)
      , c = m.useRef(null)
      , u = m.useRef(null)
      , d = m.useRef(null)
      , f = m.useRef(null)
      , g = fe(t, f, i.onViewportChange)
      , h = r.join("+").replace(/Key/g, "").replace(/Digit/g, "")
      , b = i.toastCount > 0;
    m.useEffect( () => {
        const w = y => {
            var x;
            r.length !== 0 && r.every(N => y[N] || y.code === N) && ((x = f.current) == null || x.focus())
        }
        ;
        return document.addEventListener("keydown", w),
        () => document.removeEventListener("keydown", w)
    }
    , [r]),
    m.useEffect( () => {
        const w = c.current
          , y = f.current;
        if (b && w && y) {
            const p = () => {
                if (!i.isClosePausedRef.current) {
                    const k = new CustomEvent(Bu);
                    y.dispatchEvent(k),
                    i.isClosePausedRef.current = !0
                }
            }
              , x = () => {
                if (i.isClosePausedRef.current) {
                    const k = new CustomEvent(Wu);
                    y.dispatchEvent(k),
                    i.isClosePausedRef.current = !1
                }
            }
              , N = k => {
                !w.contains(k.relatedTarget) && x()
            }
              , S = () => {
                w.contains(document.activeElement) || x()
            }
            ;
            return w.addEventListener("focusin", p),
            w.addEventListener("focusout", N),
            w.addEventListener("pointermove", p),
            w.addEventListener("pointerleave", S),
            window.addEventListener("blur", p),
            window.addEventListener("focus", x),
            () => {
                w.removeEventListener("focusin", p),
                w.removeEventListener("focusout", N),
                w.removeEventListener("pointermove", p),
                w.removeEventListener("pointerleave", S),
                window.removeEventListener("blur", p),
                window.removeEventListener("focus", x)
            }
        }
    }
    , [b, i.isClosePausedRef]);
    const v = m.useCallback( ({tabbingDirection: w}) => {
        const p = l().map(x => {
            const N = x.ref.current
              , S = [N, ...uS(N)];
            return w === "forwards" ? S : S.reverse()
        }
        );
        return (w === "forwards" ? p.reverse() : p).flat()
    }
    , [l]);
    return m.useEffect( () => {
        const w = f.current;
        if (w) {
            const y = p => {
                var S, k, C;
                const x = p.altKey || p.ctrlKey || p.metaKey;
                if (p.key === "Tab" && !x) {
                    const T = document.activeElement
                      , D = p.shiftKey;
                    if (p.target === w && D) {
                        (S = u.current) == null || S.focus();
                        return
                    }
                    const A = v({
                        tabbingDirection: D ? "backwards" : "forwards"
                    })
                      , W = A.findIndex(O => O === T);
                    Pc(A.slice(W + 1)) ? p.preventDefault() : D ? (k = u.current) == null || k.focus() : (C = d.current) == null || C.focus()
                }
            }
            ;
            return w.addEventListener("keydown", y),
            () => w.removeEventListener("keydown", y)
        }
    }
    , [l, v]),
    a.jsxs(FN, {
        ref: c,
        role: "region",
        "aria-label": o.replace("{hotkey}", h),
        tabIndex: -1,
        style: {
            pointerEvents: b ? void 0 : "none"
        },
        children: [b && a.jsx(Hu, {
            ref: u,
            onFocusFromOutsideViewport: () => {
                const w = v({
                    tabbingDirection: "forwards"
                });
                Pc(w)
            }
        }), a.jsx(pf.Slot, {
            scope: n,
            children: a.jsx(te.ol, {
                tabIndex: -1,
                ...s,
                ref: g
            })
        }), b && a.jsx(Hu, {
            ref: d,
            onFocusFromOutsideViewport: () => {
                const w = v({
                    tabbingDirection: "backwards"
                });
                Pc(w)
            }
        })]
    })
}
);
Jg.displayName = Xg;
var Zg = "ToastFocusProxy"
  , Hu = m.forwardRef( (e, t) => {
    const {__scopeToast: n, onFocusFromOutsideViewport: r, ...o} = e
      , s = Dl(Zg, n);
    return a.jsx(_l, {
        "aria-hidden": !0,
        tabIndex: 0,
        ...o,
        ref: t,
        style: {
            position: "fixed"
        },
        onFocus: i => {
            var u;
            const l = i.relatedTarget;
            !((u = s.viewport) != null && u.contains(l)) && r()
        }
    })
}
);
Hu.displayName = Zg;
var Ma = "Toast"
  , JN = "toast.swipeStart"
  , ZN = "toast.swipeMove"
  , eS = "toast.swipeCancel"
  , tS = "toast.swipeEnd"
  , ey = m.forwardRef( (e, t) => {
    const {forceMount: n, open: r, defaultOpen: o, onOpenChange: s, ...i} = e
      , [l,c] = ma({
        prop: r,
        defaultProp: o ?? !0,
        onChange: s,
        caller: Ma
    });
    return a.jsx(ms, {
        present: n || l,
        children: a.jsx(oS, {
            open: l,
            ...i,
            ref: t,
            onClose: () => c(!1),
            onPause: Zt(e.onPause),
            onResume: Zt(e.onResume),
            onSwipeStart: Q(e.onSwipeStart, u => {
                u.currentTarget.setAttribute("data-swipe", "start")
            }
            ),
            onSwipeMove: Q(e.onSwipeMove, u => {
                const {x: d, y: f} = u.detail.delta;
                u.currentTarget.setAttribute("data-swipe", "move"),
                u.currentTarget.style.setProperty("--radix-toast-swipe-move-x", `${d}px`),
                u.currentTarget.style.setProperty("--radix-toast-swipe-move-y", `${f}px`)
            }
            ),
            onSwipeCancel: Q(e.onSwipeCancel, u => {
                u.currentTarget.setAttribute("data-swipe", "cancel"),
                u.currentTarget.style.removeProperty("--radix-toast-swipe-move-x"),
                u.currentTarget.style.removeProperty("--radix-toast-swipe-move-y"),
                u.currentTarget.style.removeProperty("--radix-toast-swipe-end-x"),
                u.currentTarget.style.removeProperty("--radix-toast-swipe-end-y")
            }
            ),
            onSwipeEnd: Q(e.onSwipeEnd, u => {
                const {x: d, y: f} = u.detail.delta;
                u.currentTarget.setAttribute("data-swipe", "end"),
                u.currentTarget.style.removeProperty("--radix-toast-swipe-move-x"),
                u.currentTarget.style.removeProperty("--radix-toast-swipe-move-y"),
                u.currentTarget.style.setProperty("--radix-toast-swipe-end-x", `${d}px`),
                u.currentTarget.style.setProperty("--radix-toast-swipe-end-y", `${f}px`),
                c(!1)
            }
            )
        })
    })
}
);
ey.displayName = Ma;
var [nS,rS] = Gg(Ma, {
    onClose() {}
})
  , oS = m.forwardRef( (e, t) => {
    const {__scopeToast: n, type: r="foreground", duration: o, open: s, onClose: i, onEscapeKeyDown: l, onPause: c, onResume: u, onSwipeStart: d, onSwipeMove: f, onSwipeCancel: g, onSwipeEnd: h, ...b} = e
      , v = Dl(Ma, n)
      , [w,y] = m.useState(null)
      , p = fe(t, O => y(O))
      , x = m.useRef(null)
      , N = m.useRef(null)
      , S = o || v.duration
      , k = m.useRef(0)
      , C = m.useRef(S)
      , T = m.useRef(0)
      , {onToastAdd: D, onToastRemove: R} = v
      , F = Zt( () => {
        var V;
        (w == null ? void 0 : w.contains(document.activeElement)) && ((V = v.viewport) == null || V.focus()),
        i()
    }
    )
      , A = m.useCallback(O => {
        !O || O === 1 / 0 || (window.clearTimeout(T.current),
        k.current = new Date().getTime(),
        T.current = window.setTimeout(F, O))
    }
    , [F]);
    m.useEffect( () => {
        const O = v.viewport;
        if (O) {
            const V = () => {
                A(C.current),
                u == null || u()
            }
              , $ = () => {
                const M = new Date().getTime() - k.current;
                C.current = C.current - M,
                window.clearTimeout(T.current),
                c == null || c()
            }
            ;
            return O.addEventListener(Bu, $),
            O.addEventListener(Wu, V),
            () => {
                O.removeEventListener(Bu, $),
                O.removeEventListener(Wu, V)
            }
        }
    }
    , [v.viewport, S, c, u, A]),
    m.useEffect( () => {
        s && !v.isClosePausedRef.current && A(S)
    }
    , [s, S, v.isClosePausedRef, A]),
    m.useEffect( () => (D(),
    () => R()), [D, R]);
    const W = m.useMemo( () => w ? iy(w) : null, [w]);
    return v.viewport ? a.jsxs(a.Fragment, {
        children: [W && a.jsx(sS, {
            __scopeToast: n,
            role: "status",
            "aria-live": r === "foreground" ? "assertive" : "polite",
            "aria-atomic": !0,
            children: W
        }), a.jsx(nS, {
            scope: n,
            onClose: F,
            children: ao.createPortal(a.jsx(pf.ItemSlot, {
                scope: n,
                children: a.jsx(LN, {
                    asChild: !0,
                    onEscapeKeyDown: Q(l, () => {
                        v.isFocusedToastEscapeKeyDownRef.current || F(),
                        v.isFocusedToastEscapeKeyDownRef.current = !1
                    }
                    ),
                    children: a.jsx(te.li, {
                        role: "status",
                        "aria-live": "off",
                        "aria-atomic": !0,
                        tabIndex: 0,
                        "data-state": s ? "open" : "closed",
                        "data-swipe-direction": v.swipeDirection,
                        ...b,
                        ref: p,
                        style: {
                            userSelect: "none",
                            touchAction: "none",
                            ...e.style
                        },
                        onKeyDown: Q(e.onKeyDown, O => {
                            O.key === "Escape" && (l == null || l(O.nativeEvent),
                            O.nativeEvent.defaultPrevented || (v.isFocusedToastEscapeKeyDownRef.current = !0,
                            F()))
                        }
                        ),
                        onPointerDown: Q(e.onPointerDown, O => {
                            O.button === 0 && (x.current = {
                                x: O.clientX,
                                y: O.clientY
                            })
                        }
                        ),
                        onPointerMove: Q(e.onPointerMove, O => {
                            if (!x.current)
                                return;
                            const V = O.clientX - x.current.x
                              , $ = O.clientY - x.current.y
                              , M = !!N.current
                              , j = ["left", "right"].includes(v.swipeDirection)
                              , E = ["left", "up"].includes(v.swipeDirection) ? Math.min : Math.max
                              , L = j ? E(0, V) : 0
                              , U = j ? 0 : E(0, $)
                              , H = O.pointerType === "touch" ? 10 : 2
                              , J = {
                                x: L,
                                y: U
                            }
                              , G = {
                                originalEvent: O,
                                delta: J
                            };
                            M ? (N.current = J,
                            si(ZN, f, G, {
                                discrete: !1
                            })) : xh(J, v.swipeDirection, H) ? (N.current = J,
                            si(JN, d, G, {
                                discrete: !1
                            }),
                            O.target.setPointerCapture(O.pointerId)) : (Math.abs(V) > H || Math.abs($) > H) && (x.current = null)
                        }
                        ),
                        onPointerUp: Q(e.onPointerUp, O => {
                            const V = N.current
                              , $ = O.target;
                            if ($.hasPointerCapture(O.pointerId) && $.releasePointerCapture(O.pointerId),
                            N.current = null,
                            x.current = null,
                            V) {
                                const M = O.currentTarget
                                  , j = {
                                    originalEvent: O,
                                    delta: V
                                };
                                xh(V, v.swipeDirection, v.swipeThreshold) ? si(tS, h, j, {
                                    discrete: !0
                                }) : si(eS, g, j, {
                                    discrete: !0
                                }),
                                M.addEventListener("click", E => E.preventDefault(), {
                                    once: !0
                                })
                            }
                        }
                        )
                    })
                })
            }), v.viewport)
        })]
    }) : null
}
)
  , sS = e => {
    const {__scopeToast: t, children: n, ...r} = e
      , o = Dl(Ma, t)
      , [s,i] = m.useState(!1)
      , [l,c] = m.useState(!1);
    return lS( () => i(!0)),
    m.useEffect( () => {
        const u = window.setTimeout( () => c(!0), 1e3);
        return () => window.clearTimeout(u)
    }
    , []),
    l ? null : a.jsx(Rl, {
        asChild: !0,
        children: a.jsx(_l, {
            ...r,
            children: s && a.jsxs(a.Fragment, {
                children: [o.label, " ", n]
            })
        })
    })
}
  , aS = "ToastTitle"
  , ty = m.forwardRef( (e, t) => {
    const {__scopeToast: n, ...r} = e;
    return a.jsx(te.div, {
        ...r,
        ref: t
    })
}
);
ty.displayName = aS;
var iS = "ToastDescription"
  , ny = m.forwardRef( (e, t) => {
    const {__scopeToast: n, ...r} = e;
    return a.jsx(te.div, {
        ...r,
        ref: t
    })
}
);
ny.displayName = iS;
var ry = "ToastAction"
  , oy = m.forwardRef( (e, t) => {
    const {altText: n, ...r} = e;
    return n.trim() ? a.jsx(ay, {
        altText: n,
        asChild: !0,
        children: a.jsx(vf, {
            ...r,
            ref: t
        })
    }) : (console.error(`Invalid prop \`altText\` supplied to \`${ry}\`. Expected non-empty \`string\`.`),
    null)
}
);
oy.displayName = ry;
var sy = "ToastClose"
  , vf = m.forwardRef( (e, t) => {
    const {__scopeToast: n, ...r} = e
      , o = rS(sy, n);
    return a.jsx(ay, {
        asChild: !0,
        children: a.jsx(te.button, {
            type: "button",
            ...r,
            ref: t,
            onClick: Q(e.onClick, o.onClose)
        })
    })
}
);
vf.displayName = sy;
var ay = m.forwardRef( (e, t) => {
    const {__scopeToast: n, altText: r, ...o} = e;
    return a.jsx(te.div, {
        "data-radix-toast-announce-exclude": "",
        "data-radix-toast-announce-alt": r || void 0,
        ...o,
        ref: t
    })
}
);
function iy(e) {
    const t = [];
    return Array.from(e.childNodes).forEach(r => {
        if (r.nodeType === r.TEXT_NODE && r.textContent && t.push(r.textContent),
        cS(r)) {
            const o = r.ariaHidden || r.hidden || r.style.display === "none"
              , s = r.dataset.radixToastAnnounceExclude === "";
            if (!o)
                if (s) {
                    const i = r.dataset.radixToastAnnounceAlt;
                    i && t.push(i)
                } else
                    t.push(...iy(r))
        }
    }
    ),
    t
}
function si(e, t, n, {discrete: r}) {
    const o = n.originalEvent.currentTarget
      , s = new CustomEvent(e,{
        bubbles: !0,
        cancelable: !0,
        detail: n
    });
    t && o.addEventListener(e, t, {
        once: !0
    }),
    r ? Vg(o, s) : o.dispatchEvent(s)
}
var xh = (e, t, n=0) => {
    const r = Math.abs(e.x)
      , o = Math.abs(e.y)
      , s = r > o;
    return t === "left" || t === "right" ? s && r > n : !s && o > n
}
;
function lS(e= () => {}
) {
    const t = Zt(e);
    Ue( () => {
        let n = 0
          , r = 0;
        return n = window.requestAnimationFrame( () => r = window.requestAnimationFrame(t)),
        () => {
            window.cancelAnimationFrame(n),
            window.cancelAnimationFrame(r)
        }
    }
    , [t])
}
function cS(e) {
    return e.nodeType === e.ELEMENT_NODE
}
function uS(e) {
    const t = []
      , n = document.createTreeWalker(e, NodeFilter.SHOW_ELEMENT, {
        acceptNode: r => {
            const o = r.tagName === "INPUT" && r.type === "hidden";
            return r.disabled || r.hidden || o ? NodeFilter.FILTER_SKIP : r.tabIndex >= 0 ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_SKIP
        }
    });
    for (; n.nextNode(); )
        t.push(n.currentNode);
    return t
}
function Pc(e) {
    const t = document.activeElement;
    return e.some(n => n === t ? !0 : (n.focus(),
    document.activeElement !== t))
}
var dS = qg
  , ly = Jg
  , cy = ey
  , uy = ty
  , dy = ny
  , fy = oy
  , my = vf;
function hy(e) {
    var t, n, r = "";
    if (typeof e == "string" || typeof e == "number")
        r += e;
    else if (typeof e == "object")
        if (Array.isArray(e)) {
            var o = e.length;
            for (t = 0; t < o; t++)
                e[t] && (n = hy(e[t])) && (r && (r += " "),
                r += n)
        } else
            for (n in e)
                e[n] && (r && (r += " "),
                r += n);
    return r
}
function py() {
    for (var e, t, n = 0, r = "", o = arguments.length; n < o; n++)
        (e = arguments[n]) && (t = hy(e)) && (r && (r += " "),
        r += t);
    return r
}
const wh = e => typeof e == "boolean" ? `${e}` : e === 0 ? "0" : e
  , bh = py
  , Ol = (e, t) => n => {
    var r;
    if ((t == null ? void 0 : t.variants) == null)
        return bh(e, n == null ? void 0 : n.class, n == null ? void 0 : n.className);
    const {variants: o, defaultVariants: s} = t
      , i = Object.keys(o).map(u => {
        const d = n == null ? void 0 : n[u]
          , f = s == null ? void 0 : s[u];
        if (d === null)
            return null;
        const g = wh(d) || wh(f);
        return o[u][g]
    }
    )
      , l = n && Object.entries(n).reduce( (u, d) => {
        let[f,g] = d;
        return g === void 0 || (u[f] = g),
        u
    }
    , {})
      , c = t == null || (r = t.compoundVariants) === null || r === void 0 ? void 0 : r.reduce( (u, d) => {
        let {class: f, className: g, ...h} = d;
        return Object.entries(h).every(b => {
            let[v,w] = b;
            return Array.isArray(w) ? w.includes({
                ...s,
                ...l
            }[v]) : {
                ...s,
                ...l
            }[v] === w
        }
        ) ? [...u, f, g] : u
    }
    , []);
    return bh(e, i, c, n == null ? void 0 : n.class, n == null ? void 0 : n.className)
}
;
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const fS = e => e.replace(/([a-z0-9])([A-Z])/g, "$1-$2").toLowerCase()
  , vy = (...e) => e.filter( (t, n, r) => !!t && t.trim() !== "" && r.indexOf(t) === n).join(" ").trim();
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
var mS = {
    xmlns: "http://www.w3.org/2000/svg",
    width: 24,
    height: 24,
    viewBox: "0 0 24 24",
    fill: "none",
    stroke: "currentColor",
    strokeWidth: 2,
    strokeLinecap: "round",
    strokeLinejoin: "round"
};
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const hS = m.forwardRef( ({color: e="currentColor", size: t=24, strokeWidth: n=2, absoluteStrokeWidth: r, className: o="", children: s, iconNode: i, ...l}, c) => m.createElement("svg", {
    ref: c,
    ...mS,
    width: t,
    height: t,
    stroke: e,
    strokeWidth: r ? Number(n) * 24 / Number(t) : n,
    className: vy("lucide", o),
    ...l
}, [...i.map( ([u,d]) => m.createElement(u, d)), ...Array.isArray(s) ? s : [s]]));
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const ee = (e, t) => {
    const n = m.forwardRef( ({className: r, ...o}, s) => m.createElement(hS, {
        ref: s,
        iconNode: t,
        className: vy(`lucide-${fS(e)}`, r),
        ...o
    }));
    return n.displayName = `${e}`,
    n
}
;
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const pS = ee("ArrowLeft", [["path", {
    d: "m12 19-7-7 7-7",
    key: "1l729n"
}], ["path", {
    d: "M19 12H5",
    key: "x3x0zl"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const ha = ee("ArrowRight", [["path", {
    d: "M5 12h14",
    key: "1ays0h"
}], ["path", {
    d: "m12 5 7 7-7 7",
    key: "xquz4c"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const gy = ee("Award", [["path", {
    d: "m15.477 12.89 1.515 8.526a.5.5 0 0 1-.81.47l-3.58-2.687a1 1 0 0 0-1.197 0l-3.586 2.686a.5.5 0 0 1-.81-.469l1.514-8.526",
    key: "1yiouv"
}], ["circle", {
    cx: "12",
    cy: "8",
    r: "6",
    key: "1vp47v"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const vS = ee("Bath", [["path", {
    d: "M10 4 8 6",
    key: "1rru8s"
}], ["path", {
    d: "M17 19v2",
    key: "ts1sot"
}], ["path", {
    d: "M2 12h20",
    key: "9i4pu4"
}], ["path", {
    d: "M7 19v2",
    key: "12npes"
}], ["path", {
    d: "M9 5 7.621 3.621A2.121 2.121 0 0 0 4 5v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-5",
    key: "14ym8i"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const gS = ee("Bed", [["path", {
    d: "M2 4v16",
    key: "vw9hq8"
}], ["path", {
    d: "M2 8h18a2 2 0 0 1 2 2v10",
    key: "1dgv2r"
}], ["path", {
    d: "M2 17h20",
    key: "18nfp3"
}], ["path", {
    d: "M6 8v9",
    key: "1yriud"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const yS = ee("BookOpen", [["path", {
    d: "M12 7v14",
    key: "1akyts"
}], ["path", {
    d: "M3 18a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h5a4 4 0 0 1 4 4 4 4 0 0 1 4-4h5a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1h-6a3 3 0 0 0-3 3 3 3 0 0 0-3-3z",
    key: "ruj8y"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const xS = ee("Bookmark", [["path", {
    d: "m19 21-7-4-7 4V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v16z",
    key: "1fy3hk"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const Vu = ee("Building", [["rect", {
    width: "16",
    height: "20",
    x: "4",
    y: "2",
    rx: "2",
    ry: "2",
    key: "76otgf"
}], ["path", {
    d: "M9 22v-4h6v4",
    key: "r93iot"
}], ["path", {
    d: "M8 6h.01",
    key: "1dz90k"
}], ["path", {
    d: "M16 6h.01",
    key: "1x0f13"
}], ["path", {
    d: "M12 6h.01",
    key: "1vi96p"
}], ["path", {
    d: "M12 10h.01",
    key: "1nrarc"
}], ["path", {
    d: "M12 14h.01",
    key: "1etili"
}], ["path", {
    d: "M16 10h.01",
    key: "1m94wz"
}], ["path", {
    d: "M16 14h.01",
    key: "1gbofw"
}], ["path", {
    d: "M8 10h.01",
    key: "19clt8"
}], ["path", {
    d: "M8 14h.01",
    key: "6423bh"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const Uu = ee("Calculator", [["rect", {
    width: "16",
    height: "20",
    x: "4",
    y: "2",
    rx: "2",
    key: "1nb95v"
}], ["line", {
    x1: "8",
    x2: "16",
    y1: "6",
    y2: "6",
    key: "x4nwl0"
}], ["line", {
    x1: "16",
    x2: "16",
    y1: "14",
    y2: "18",
    key: "wjye3r"
}], ["path", {
    d: "M16 10h.01",
    key: "1m94wz"
}], ["path", {
    d: "M12 10h.01",
    key: "1nrarc"
}], ["path", {
    d: "M8 10h.01",
    key: "19clt8"
}], ["path", {
    d: "M12 14h.01",
    key: "1etili"
}], ["path", {
    d: "M8 14h.01",
    key: "6423bh"
}], ["path", {
    d: "M12 18h.01",
    key: "mhygvu"
}], ["path", {
    d: "M8 18h.01",
    key: "lrp35t"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const Jr = ee("Calendar", [["path", {
    d: "M8 2v4",
    key: "1cmpym"
}], ["path", {
    d: "M16 2v4",
    key: "4m81vk"
}], ["rect", {
    width: "18",
    height: "18",
    x: "3",
    y: "4",
    rx: "2",
    key: "1hopcy"
}], ["path", {
    d: "M3 10h18",
    key: "8toen8"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const wS = ee("Check", [["path", {
    d: "M20 6 9 17l-5-5",
    key: "1gmf2c"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const yy = ee("ChevronDown", [["path", {
    d: "m6 9 6 6 6-6",
    key: "qrunsl"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const bS = ee("ChevronLeft", [["path", {
    d: "m15 18-6-6 6-6",
    key: "1wnfg3"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const NS = ee("ChevronRight", [["path", {
    d: "m9 18 6-6-6-6",
    key: "mthhwq"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const SS = ee("ChevronUp", [["path", {
    d: "m18 15-6-6-6 6",
    key: "153udz"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const ir = ee("CircleCheckBig", [["path", {
    d: "M21.801 10A10 10 0 1 1 17 3.335",
    key: "yps3ct"
}], ["path", {
    d: "m9 11 3 3L22 4",
    key: "1pflzl"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const os = ee("Clock", [["circle", {
    cx: "12",
    cy: "12",
    r: "10",
    key: "1mglay"
}], ["polyline", {
    points: "12 6 12 12 16 14",
    key: "68esgv"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const Yu = ee("DollarSign", [["line", {
    x1: "12",
    x2: "12",
    y1: "2",
    y2: "22",
    key: "7eqyqh"
}], ["path", {
    d: "M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6",
    key: "1b0p4s"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const jS = ee("Facebook", [["path", {
    d: "M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z",
    key: "1jg4f8"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const CS = ee("Filter", [["polygon", {
    points: "22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3",
    key: "1yg77f"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const kS = ee("Heart", [["path", {
    d: "M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z",
    key: "c3ymky"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const gf = ee("House", [["path", {
    d: "M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8",
    key: "5wwlr5"
}], ["path", {
    d: "M3 10a2 2 0 0 1 .709-1.528l7-5.999a2 2 0 0 1 2.582 0l7 5.999A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z",
    key: "1d0kgt"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const ES = ee("Instagram", [["rect", {
    width: "20",
    height: "20",
    x: "2",
    y: "2",
    rx: "5",
    ry: "5",
    key: "2e1cvw"
}], ["path", {
    d: "M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z",
    key: "9exkf1"
}], ["line", {
    x1: "17.5",
    x2: "17.51",
    y1: "6.5",
    y2: "6.5",
    key: "r4j83e"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const PS = ee("Linkedin", [["path", {
    d: "M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z",
    key: "c2jq9f"
}], ["rect", {
    width: "4",
    height: "12",
    x: "2",
    y: "9",
    key: "mk3on5"
}], ["circle", {
    cx: "4",
    cy: "4",
    r: "2",
    key: "bt5ra8"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const ss = ee("Mail", [["rect", {
    width: "20",
    height: "16",
    x: "2",
    y: "4",
    rx: "2",
    key: "18n3k1"
}], ["path", {
    d: "m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7",
    key: "1ocrg3"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const Ra = ee("MapPin", [["path", {
    d: "M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0",
    key: "1r0f0z"
}], ["circle", {
    cx: "12",
    cy: "10",
    r: "3",
    key: "ilqhr7"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const TS = ee("Menu", [["line", {
    x1: "4",
    x2: "20",
    y1: "12",
    y2: "12",
    key: "1e0a9i"
}], ["line", {
    x1: "4",
    x2: "20",
    y1: "6",
    y2: "6",
    key: "1owob3"
}], ["line", {
    x1: "4",
    x2: "20",
    y1: "18",
    y2: "18",
    key: "yk5zj1"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const as = ee("Phone", [["path", {
    d: "M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z",
    key: "foiqr5"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const xy = ee("PiggyBank", [["path", {
    d: "M19 5c-1.5 0-2.8 1.4-3 2-3.5-1.5-11-.3-11 5 0 1.8 0 3 2 4.5V20h4v-2h3v2h4v-4c1-.5 1.7-1 2-2h2v-4h-2c0-1-.5-1.5-1-2V5z",
    key: "1ivx2i"
}], ["path", {
    d: "M2 9v1c0 1.1.9 2 2 2h1",
    key: "nm575m"
}], ["path", {
    d: "M16 11h.01",
    key: "xkw8gn"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const MS = ee("Play", [["polygon", {
    points: "6 3 20 12 6 21 6 3",
    key: "1oa8hb"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const RS = ee("Quote", [["path", {
    d: "M16 3a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2 1 1 0 0 1 1 1v1a2 2 0 0 1-2 2 1 1 0 0 0-1 1v2a1 1 0 0 0 1 1 6 6 0 0 0 6-6V5a2 2 0 0 0-2-2z",
    key: "rib7q0"
}], ["path", {
    d: "M5 3a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2 1 1 0 0 1 1 1v1a2 2 0 0 1-2 2 1 1 0 0 0-1 1v2a1 1 0 0 0 1 1 6 6 0 0 0 6-6V5a2 2 0 0 0-2-2z",
    key: "1ymkrd"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const wy = ee("Search", [["circle", {
    cx: "11",
    cy: "11",
    r: "8",
    key: "4ej97u"
}], ["path", {
    d: "m21 21-4.3-4.3",
    key: "1qie3q"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const _S = ee("Share2", [["circle", {
    cx: "18",
    cy: "5",
    r: "3",
    key: "gq8acd"
}], ["circle", {
    cx: "6",
    cy: "12",
    r: "3",
    key: "w7nqdw"
}], ["circle", {
    cx: "18",
    cy: "19",
    r: "3",
    key: "1xt0gg"
}], ["line", {
    x1: "8.59",
    x2: "15.42",
    y1: "13.51",
    y2: "17.49",
    key: "47mynk"
}], ["line", {
    x1: "15.41",
    x2: "8.59",
    y1: "6.51",
    y2: "10.49",
    key: "1n3mei"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const Ku = ee("Shield", [["path", {
    d: "M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z",
    key: "oel41y"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const DS = ee("Square", [["rect", {
    width: "18",
    height: "18",
    x: "3",
    y: "3",
    rx: "2",
    key: "afitv7"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const Nh = ee("Star", [["path", {
    d: "M11.525 2.295a.53.53 0 0 1 .95 0l2.31 4.679a2.123 2.123 0 0 0 1.595 1.16l5.166.756a.53.53 0 0 1 .294.904l-3.736 3.638a2.123 2.123 0 0 0-.611 1.878l.882 5.14a.53.53 0 0 1-.771.56l-4.618-2.428a2.122 2.122 0 0 0-1.973 0L6.396 21.01a.53.53 0 0 1-.77-.56l.881-5.139a2.122 2.122 0 0 0-.611-1.879L2.16 9.795a.53.53 0 0 1 .294-.906l5.165-.755a2.122 2.122 0 0 0 1.597-1.16z",
    key: "r04s7s"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const nl = ee("TrendingUp", [["polyline", {
    points: "22 7 13.5 15.5 8.5 10.5 2 17",
    key: "126l90"
}], ["polyline", {
    points: "16 7 22 7 22 13",
    key: "kwv8wd"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const OS = ee("Twitter", [["path", {
    d: "M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6 2.2.1 4.4-.6 6-2C3 15.5.5 9.6 3 5c2.2 2.6 5.6 4.1 9 4-.9-4.2 4-6.6 7-3.8 1.1 0 3-1.2 3-1.2z",
    key: "pff0z6"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const wr = ee("User", [["path", {
    d: "M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2",
    key: "975kel"
}], ["circle", {
    cx: "12",
    cy: "7",
    r: "4",
    key: "17ys0d"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const AS = ee("Users", [["path", {
    d: "M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2",
    key: "1yyitq"
}], ["circle", {
    cx: "9",
    cy: "7",
    r: "4",
    key: "nufk8"
}], ["path", {
    d: "M22 21v-2a4 4 0 0 0-3-3.87",
    key: "kshegd"
}], ["path", {
    d: "M16 3.13a4 4 0 0 1 0 7.75",
    key: "1da9ce"
}]]);
/**
 * @license lucide-react v0.462.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */
const yf = ee("X", [["path", {
    d: "M18 6 6 18",
    key: "1bl5f8"
}], ["path", {
    d: "m6 6 12 12",
    key: "d8bk6v"
}]])
  , xf = "-"
  , IS = e => {
    const t = FS(e)
      , {conflictingClassGroups: n, conflictingClassGroupModifiers: r} = e;
    return {
        getClassGroupId: i => {
            const l = i.split(xf);
            return l[0] === "" && l.length !== 1 && l.shift(),
            by(l, t) || LS(i)
        }
        ,
        getConflictingClassGroupIds: (i, l) => {
            const c = n[i] || [];
            return l && r[i] ? [...c, ...r[i]] : c
        }
    }
}
  , by = (e, t) => {
    var i;
    if (e.length === 0)
        return t.classGroupId;
    const n = e[0]
      , r = t.nextPart.get(n)
      , o = r ? by(e.slice(1), r) : void 0;
    if (o)
        return o;
    if (t.validators.length === 0)
        return;
    const s = e.join(xf);
    return (i = t.validators.find( ({validator: l}) => l(s))) == null ? void 0 : i.classGroupId
}
  , Sh = /^\[(.+)\]$/
  , LS = e => {
    if (Sh.test(e)) {
        const t = Sh.exec(e)[1]
          , n = t == null ? void 0 : t.substring(0, t.indexOf(":"));
        if (n)
            return "arbitrary.." + n
    }
}
  , FS = e => {
    const {theme: t, prefix: n} = e
      , r = {
        nextPart: new Map,
        validators: []
    };
    return $S(Object.entries(e.classGroups), n).forEach( ([s,i]) => {
        Qu(i, r, s, t)
    }
    ),
    r
}
  , Qu = (e, t, n, r) => {
    e.forEach(o => {
        if (typeof o == "string") {
            const s = o === "" ? t : jh(t, o);
            s.classGroupId = n;
            return
        }
        if (typeof o == "function") {
            if (zS(o)) {
                Qu(o(r), t, n, r);
                return
            }
            t.validators.push({
                validator: o,
                classGroupId: n
            });
            return
        }
        Object.entries(o).forEach( ([s,i]) => {
            Qu(i, jh(t, s), n, r)
        }
        )
    }
    )
}
  , jh = (e, t) => {
    let n = e;
    return t.split(xf).forEach(r => {
        n.nextPart.has(r) || n.nextPart.set(r, {
            nextPart: new Map,
            validators: []
        }),
        n = n.nextPart.get(r)
    }
    ),
    n
}
  , zS = e => e.isThemeGetter
  , $S = (e, t) => t ? e.map( ([n,r]) => {
    const o = r.map(s => typeof s == "string" ? t + s : typeof s == "object" ? Object.fromEntries(Object.entries(s).map( ([i,l]) => [t + i, l])) : s);
    return [n, o]
}
) : e
  , BS = e => {
    if (e < 1)
        return {
            get: () => {}
            ,
            set: () => {}
        };
    let t = 0
      , n = new Map
      , r = new Map;
    const o = (s, i) => {
        n.set(s, i),
        t++,
        t > e && (t = 0,
        r = n,
        n = new Map)
    }
    ;
    return {
        get(s) {
            let i = n.get(s);
            if (i !== void 0)
                return i;
            if ((i = r.get(s)) !== void 0)
                return o(s, i),
                i
        },
        set(s, i) {
            n.has(s) ? n.set(s, i) : o(s, i)
        }
    }
}
  , Ny = "!"
  , WS = e => {
    const {separator: t, experimentalParseClassName: n} = e
      , r = t.length === 1
      , o = t[0]
      , s = t.length
      , i = l => {
        const c = [];
        let u = 0, d = 0, f;
        for (let w = 0; w < l.length; w++) {
            let y = l[w];
            if (u === 0) {
                if (y === o && (r || l.slice(w, w + s) === t)) {
                    c.push(l.slice(d, w)),
                    d = w + s;
                    continue
                }
                if (y === "/") {
                    f = w;
                    continue
                }
            }
            y === "[" ? u++ : y === "]" && u--
        }
        const g = c.length === 0 ? l : l.substring(d)
          , h = g.startsWith(Ny)
          , b = h ? g.substring(1) : g
          , v = f && f > d ? f - d : void 0;
        return {
            modifiers: c,
            hasImportantModifier: h,
            baseClassName: b,
            maybePostfixModifierPosition: v
        }
    }
    ;
    return n ? l => n({
        className: l,
        parseClassName: i
    }) : i
}
  , HS = e => {
    if (e.length <= 1)
        return e;
    const t = [];
    let n = [];
    return e.forEach(r => {
        r[0] === "[" ? (t.push(...n.sort(), r),
        n = []) : n.push(r)
    }
    ),
    t.push(...n.sort()),
    t
}
  , VS = e => ({
    cache: BS(e.cacheSize),
    parseClassName: WS(e),
    ...IS(e)
})
  , US = /\s+/
  , YS = (e, t) => {
    const {parseClassName: n, getClassGroupId: r, getConflictingClassGroupIds: o} = t
      , s = []
      , i = e.trim().split(US);
    let l = "";
    for (let c = i.length - 1; c >= 0; c -= 1) {
        const u = i[c]
          , {modifiers: d, hasImportantModifier: f, baseClassName: g, maybePostfixModifierPosition: h} = n(u);
        let b = !!h
          , v = r(b ? g.substring(0, h) : g);
        if (!v) {
            if (!b) {
                l = u + (l.length > 0 ? " " + l : l);
                continue
            }
            if (v = r(g),
            !v) {
                l = u + (l.length > 0 ? " " + l : l);
                continue
            }
            b = !1
        }
        const w = HS(d).join(":")
          , y = f ? w + Ny : w
          , p = y + v;
        if (s.includes(p))
            continue;
        s.push(p);
        const x = o(v, b);
        for (let N = 0; N < x.length; ++N) {
            const S = x[N];
            s.push(y + S)
        }
        l = u + (l.length > 0 ? " " + l : l)
    }
    return l
}
;
function KS() {
    let e = 0, t, n, r = "";
    for (; e < arguments.length; )
        (t = arguments[e++]) && (n = Sy(t)) && (r && (r += " "),
        r += n);
    return r
}
const Sy = e => {
    if (typeof e == "string")
        return e;
    let t, n = "";
    for (let r = 0; r < e.length; r++)
        e[r] && (t = Sy(e[r])) && (n && (n += " "),
        n += t);
    return n
}
;
function QS(e, ...t) {
    let n, r, o, s = i;
    function i(c) {
        const u = t.reduce( (d, f) => f(d), e());
        return n = VS(u),
        r = n.cache.get,
        o = n.cache.set,
        s = l,
        l(c)
    }
    function l(c) {
        const u = r(c);
        if (u)
            return u;
        const d = YS(c, n);
        return o(c, d),
        d
    }
    return function() {
        return s(KS.apply(null, arguments))
    }
}
const we = e => {
    const t = n => n[e] || [];
    return t.isThemeGetter = !0,
    t
}
  , jy = /^\[(?:([a-z-]+):)?(.+)\]$/i
  , GS = /^\d+\/\d+$/
  , qS = new Set(["px", "full", "screen"])
  , XS = /^(\d+(\.\d+)?)?(xs|sm|md|lg|xl)$/
  , JS = /\d+(%|px|r?em|[sdl]?v([hwib]|min|max)|pt|pc|in|cm|mm|cap|ch|ex|r?lh|cq(w|h|i|b|min|max))|\b(calc|min|max|clamp)\(.+\)|^0$/
  , ZS = /^(rgba?|hsla?|hwb|(ok)?(lab|lch))\(.+\)$/
  , ej = /^(inset_)?-?((\d+)?\.?(\d+)[a-z]+|0)_-?((\d+)?\.?(\d+)[a-z]+|0)/
  , tj = /^(url|image|image-set|cross-fade|element|(repeating-)?(linear|radial|conic)-gradient)\(.+\)$/
  , Nn = e => Fo(e) || qS.has(e) || GS.test(e)
  , Un = e => hs(e, "length", cj)
  , Fo = e => !!e && !Number.isNaN(Number(e))
  , Tc = e => hs(e, "number", Fo)
  , Rs = e => !!e && Number.isInteger(Number(e))
  , nj = e => e.endsWith("%") && Fo(e.slice(0, -1))
  , Z = e => jy.test(e)
  , Yn = e => XS.test(e)
  , rj = new Set(["length", "size", "percentage"])
  , oj = e => hs(e, rj, Cy)
  , sj = e => hs(e, "position", Cy)
  , aj = new Set(["image", "url"])
  , ij = e => hs(e, aj, dj)
  , lj = e => hs(e, "", uj)
  , _s = () => !0
  , hs = (e, t, n) => {
    const r = jy.exec(e);
    return r ? r[1] ? typeof t == "string" ? r[1] === t : t.has(r[1]) : n(r[2]) : !1
}
  , cj = e => JS.test(e) && !ZS.test(e)
  , Cy = () => !1
  , uj = e => ej.test(e)
  , dj = e => tj.test(e)
  , fj = () => {
    const e = we("colors")
      , t = we("spacing")
      , n = we("blur")
      , r = we("brightness")
      , o = we("borderColor")
      , s = we("borderRadius")
      , i = we("borderSpacing")
      , l = we("borderWidth")
      , c = we("contrast")
      , u = we("grayscale")
      , d = we("hueRotate")
      , f = we("invert")
      , g = we("gap")
      , h = we("gradientColorStops")
      , b = we("gradientColorStopPositions")
      , v = we("inset")
      , w = we("margin")
      , y = we("opacity")
      , p = we("padding")
      , x = we("saturate")
      , N = we("scale")
      , S = we("sepia")
      , k = we("skew")
      , C = we("space")
      , T = we("translate")
      , D = () => ["auto", "contain", "none"]
      , R = () => ["auto", "hidden", "clip", "visible", "scroll"]
      , F = () => ["auto", Z, t]
      , A = () => [Z, t]
      , W = () => ["", Nn, Un]
      , O = () => ["auto", Fo, Z]
      , V = () => ["bottom", "center", "left", "left-bottom", "left-top", "right", "right-bottom", "right-top", "top"]
      , $ = () => ["solid", "dashed", "dotted", "double", "none"]
      , M = () => ["normal", "multiply", "screen", "overlay", "darken", "lighten", "color-dodge", "color-burn", "hard-light", "soft-light", "difference", "exclusion", "hue", "saturation", "color", "luminosity"]
      , j = () => ["start", "end", "center", "between", "around", "evenly", "stretch"]
      , E = () => ["", "0", Z]
      , L = () => ["auto", "avoid", "all", "avoid-page", "page", "left", "right", "column"]
      , U = () => [Fo, Z];
    return {
        cacheSize: 500,
        separator: ":",
        theme: {
            colors: [_s],
            spacing: [Nn, Un],
            blur: ["none", "", Yn, Z],
            brightness: U(),
            borderColor: [e],
            borderRadius: ["none", "", "full", Yn, Z],
            borderSpacing: A(),
            borderWidth: W(),
            contrast: U(),
            grayscale: E(),
            hueRotate: U(),
            invert: E(),
            gap: A(),
            gradientColorStops: [e],
            gradientColorStopPositions: [nj, Un],
            inset: F(),
            margin: F(),
            opacity: U(),
            padding: A(),
            saturate: U(),
            scale: U(),
            sepia: E(),
            skew: U(),
            space: A(),
            translate: A()
        },
        classGroups: {
            aspect: [{
                aspect: ["auto", "square", "video", Z]
            }],
            container: ["container"],
            columns: [{
                columns: [Yn]
            }],
            "break-after": [{
                "break-after": L()
            }],
            "break-before": [{
                "break-before": L()
            }],
            "break-inside": [{
                "break-inside": ["auto", "avoid", "avoid-page", "avoid-column"]
            }],
            "box-decoration": [{
                "box-decoration": ["slice", "clone"]
            }],
            box: [{
                box: ["border", "content"]
            }],
            display: ["block", "inline-block", "inline", "flex", "inline-flex", "table", "inline-table", "table-caption", "table-cell", "table-column", "table-column-group", "table-footer-group", "table-header-group", "table-row-group", "table-row", "flow-root", "grid", "inline-grid", "contents", "list-item", "hidden"],
            float: [{
                float: ["right", "left", "none", "start", "end"]
            }],
            clear: [{
                clear: ["left", "right", "both", "none", "start", "end"]
            }],
            isolation: ["isolate", "isolation-auto"],
            "object-fit": [{
                object: ["contain", "cover", "fill", "none", "scale-down"]
            }],
            "object-position": [{
                object: [...V(), Z]
            }],
            overflow: [{
                overflow: R()
            }],
            "overflow-x": [{
                "overflow-x": R()
            }],
            "overflow-y": [{
                "overflow-y": R()
            }],
            overscroll: [{
                overscroll: D()
            }],
            "overscroll-x": [{
                "overscroll-x": D()
            }],
            "overscroll-y": [{
                "overscroll-y": D()
            }],
            position: ["static", "fixed", "absolute", "relative", "sticky"],
            inset: [{
                inset: [v]
            }],
            "inset-x": [{
                "inset-x": [v]
            }],
            "inset-y": [{
                "inset-y": [v]
            }],
            start: [{
                start: [v]
            }],
            end: [{
                end: [v]
            }],
            top: [{
                top: [v]
            }],
            right: [{
                right: [v]
            }],
            bottom: [{
                bottom: [v]
            }],
            left: [{
                left: [v]
            }],
            visibility: ["visible", "invisible", "collapse"],
            z: [{
                z: ["auto", Rs, Z]
            }],
            basis: [{
                basis: F()
            }],
            "flex-direction": [{
                flex: ["row", "row-reverse", "col", "col-reverse"]
            }],
            "flex-wrap": [{
                flex: ["wrap", "wrap-reverse", "nowrap"]
            }],
            flex: [{
                flex: ["1", "auto", "initial", "none", Z]
            }],
            grow: [{
                grow: E()
            }],
            shrink: [{
                shrink: E()
            }],
            order: [{
                order: ["first", "last", "none", Rs, Z]
            }],
            "grid-cols": [{
                "grid-cols": [_s]
            }],
            "col-start-end": [{
                col: ["auto", {
                    span: ["full", Rs, Z]
                }, Z]
            }],
            "col-start": [{
                "col-start": O()
            }],
            "col-end": [{
                "col-end": O()
            }],
            "grid-rows": [{
                "grid-rows": [_s]
            }],
            "row-start-end": [{
                row: ["auto", {
                    span: [Rs, Z]
                }, Z]
            }],
            "row-start": [{
                "row-start": O()
            }],
            "row-end": [{
                "row-end": O()
            }],
            "grid-flow": [{
                "grid-flow": ["row", "col", "dense", "row-dense", "col-dense"]
            }],
            "auto-cols": [{
                "auto-cols": ["auto", "min", "max", "fr", Z]
            }],
            "auto-rows": [{
                "auto-rows": ["auto", "min", "max", "fr", Z]
            }],
            gap: [{
                gap: [g]
            }],
            "gap-x": [{
                "gap-x": [g]
            }],
            "gap-y": [{
                "gap-y": [g]
            }],
            "justify-content": [{
                justify: ["normal", ...j()]
            }],
            "justify-items": [{
                "justify-items": ["start", "end", "center", "stretch"]
            }],
            "justify-self": [{
                "justify-self": ["auto", "start", "end", "center", "stretch"]
            }],
            "align-content": [{
                content: ["normal", ...j(), "baseline"]
            }],
            "align-items": [{
                items: ["start", "end", "center", "baseline", "stretch"]
            }],
            "align-self": [{
                self: ["auto", "start", "end", "center", "stretch", "baseline"]
            }],
            "place-content": [{
                "place-content": [...j(), "baseline"]
            }],
            "place-items": [{
                "place-items": ["start", "end", "center", "baseline", "stretch"]
            }],
            "place-self": [{
                "place-self": ["auto", "start", "end", "center", "stretch"]
            }],
            p: [{
                p: [p]
            }],
            px: [{
                px: [p]
            }],
            py: [{
                py: [p]
            }],
            ps: [{
                ps: [p]
            }],
            pe: [{
                pe: [p]
            }],
            pt: [{
                pt: [p]
            }],
            pr: [{
                pr: [p]
            }],
            pb: [{
                pb: [p]
            }],
            pl: [{
                pl: [p]
            }],
            m: [{
                m: [w]
            }],
            mx: [{
                mx: [w]
            }],
            my: [{
                my: [w]
            }],
            ms: [{
                ms: [w]
            }],
            me: [{
                me: [w]
            }],
            mt: [{
                mt: [w]
            }],
            mr: [{
                mr: [w]
            }],
            mb: [{
                mb: [w]
            }],
            ml: [{
                ml: [w]
            }],
            "space-x": [{
                "space-x": [C]
            }],
            "space-x-reverse": ["space-x-reverse"],
            "space-y": [{
                "space-y": [C]
            }],
            "space-y-reverse": ["space-y-reverse"],
            w: [{
                w: ["auto", "min", "max", "fit", "svw", "lvw", "dvw", Z, t]
            }],
            "min-w": [{
                "min-w": [Z, t, "min", "max", "fit"]
            }],
            "max-w": [{
                "max-w": [Z, t, "none", "full", "min", "max", "fit", "prose", {
                    screen: [Yn]
                }, Yn]
            }],
            h: [{
                h: [Z, t, "auto", "min", "max", "fit", "svh", "lvh", "dvh"]
            }],
            "min-h": [{
                "min-h": [Z, t, "min", "max", "fit", "svh", "lvh", "dvh"]
            }],
            "max-h": [{
                "max-h": [Z, t, "min", "max", "fit", "svh", "lvh", "dvh"]
            }],
            size: [{
                size: [Z, t, "auto", "min", "max", "fit"]
            }],
            "font-size": [{
                text: ["base", Yn, Un]
            }],
            "font-smoothing": ["antialiased", "subpixel-antialiased"],
            "font-style": ["italic", "not-italic"],
            "font-weight": [{
                font: ["thin", "extralight", "light", "normal", "medium", "semibold", "bold", "extrabold", "black", Tc]
            }],
            "font-family": [{
                font: [_s]
            }],
            "fvn-normal": ["normal-nums"],
            "fvn-ordinal": ["ordinal"],
            "fvn-slashed-zero": ["slashed-zero"],
            "fvn-figure": ["lining-nums", "oldstyle-nums"],
            "fvn-spacing": ["proportional-nums", "tabular-nums"],
            "fvn-fraction": ["diagonal-fractions", "stacked-fractions"],
            tracking: [{
                tracking: ["tighter", "tight", "normal", "wide", "wider", "widest", Z]
            }],
            "line-clamp": [{
                "line-clamp": ["none", Fo, Tc]
            }],
            leading: [{
                leading: ["none", "tight", "snug", "normal", "relaxed", "loose", Nn, Z]
            }],
            "list-image": [{
                "list-image": ["none", Z]
            }],
            "list-style-type": [{
                list: ["none", "disc", "decimal", Z]
            }],
            "list-style-position": [{
                list: ["inside", "outside"]
            }],
            "placeholder-color": [{
                placeholder: [e]
            }],
            "placeholder-opacity": [{
                "placeholder-opacity": [y]
            }],
            "text-alignment": [{
                text: ["left", "center", "right", "justify", "start", "end"]
            }],
            "text-color": [{
                text: [e]
            }],
            "text-opacity": [{
                "text-opacity": [y]
            }],
            "text-decoration": ["underline", "overline", "line-through", "no-underline"],
            "text-decoration-style": [{
                decoration: [...$(), "wavy"]
            }],
            "text-decoration-thickness": [{
                decoration: ["auto", "from-font", Nn, Un]
            }],
            "underline-offset": [{
                "underline-offset": ["auto", Nn, Z]
            }],
            "text-decoration-color": [{
                decoration: [e]
            }],
            "text-transform": ["uppercase", "lowercase", "capitalize", "normal-case"],
            "text-overflow": ["truncate", "text-ellipsis", "text-clip"],
            "text-wrap": [{
                text: ["wrap", "nowrap", "balance", "pretty"]
            }],
            indent: [{
                indent: A()
            }],
            "vertical-align": [{
                align: ["baseline", "top", "middle", "bottom", "text-top", "text-bottom", "sub", "super", Z]
            }],
            whitespace: [{
                whitespace: ["normal", "nowrap", "pre", "pre-line", "pre-wrap", "break-spaces"]
            }],
            break: [{
                break: ["normal", "words", "all", "keep"]
            }],
            hyphens: [{
                hyphens: ["none", "manual", "auto"]
            }],
            content: [{
                content: ["none", Z]
            }],
            "bg-attachment": [{
                bg: ["fixed", "local", "scroll"]
            }],
            "bg-clip": [{
                "bg-clip": ["border", "padding", "content", "text"]
            }],
            "bg-opacity": [{
                "bg-opacity": [y]
            }],
            "bg-origin": [{
                "bg-origin": ["border", "padding", "content"]
            }],
            "bg-position": [{
                bg: [...V(), sj]
            }],
            "bg-repeat": [{
                bg: ["no-repeat", {
                    repeat: ["", "x", "y", "round", "space"]
                }]
            }],
            "bg-size": [{
                bg: ["auto", "cover", "contain", oj]
            }],
            "bg-image": [{
                bg: ["none", {
                    "gradient-to": ["t", "tr", "r", "br", "b", "bl", "l", "tl"]
                }, ij]
            }],
            "bg-color": [{
                bg: [e]
            }],
            "gradient-from-pos": [{
                from: [b]
            }],
            "gradient-via-pos": [{
                via: [b]
            }],
            "gradient-to-pos": [{
                to: [b]
            }],
            "gradient-from": [{
                from: [h]
            }],
            "gradient-via": [{
                via: [h]
            }],
            "gradient-to": [{
                to: [h]
            }],
            rounded: [{
                rounded: [s]
            }],
            "rounded-s": [{
                "rounded-s": [s]
            }],
            "rounded-e": [{
                "rounded-e": [s]
            }],
            "rounded-t": [{
                "rounded-t": [s]
            }],
            "rounded-r": [{
                "rounded-r": [s]
            }],
            "rounded-b": [{
                "rounded-b": [s]
            }],
            "rounded-l": [{
                "rounded-l": [s]
            }],
            "rounded-ss": [{
                "rounded-ss": [s]
            }],
            "rounded-se": [{
                "rounded-se": [s]
            }],
            "rounded-ee": [{
                "rounded-ee": [s]
            }],
            "rounded-es": [{
                "rounded-es": [s]
            }],
            "rounded-tl": [{
                "rounded-tl": [s]
            }],
            "rounded-tr": [{
                "rounded-tr": [s]
            }],
            "rounded-br": [{
                "rounded-br": [s]
            }],
            "rounded-bl": [{
                "rounded-bl": [s]
            }],
            "border-w": [{
                border: [l]
            }],
            "border-w-x": [{
                "border-x": [l]
            }],
            "border-w-y": [{
                "border-y": [l]
            }],
            "border-w-s": [{
                "border-s": [l]
            }],
            "border-w-e": [{
                "border-e": [l]
            }],
            "border-w-t": [{
                "border-t": [l]
            }],
            "border-w-r": [{
                "border-r": [l]
            }],
            "border-w-b": [{
                "border-b": [l]
            }],
            "border-w-l": [{
                "border-l": [l]
            }],
            "border-opacity": [{
                "border-opacity": [y]
            }],
            "border-style": [{
                border: [...$(), "hidden"]
            }],
            "divide-x": [{
                "divide-x": [l]
            }],
            "divide-x-reverse": ["divide-x-reverse"],
            "divide-y": [{
                "divide-y": [l]
            }],
            "divide-y-reverse": ["divide-y-reverse"],
            "divide-opacity": [{
                "divide-opacity": [y]
            }],
            "divide-style": [{
                divide: $()
            }],
            "border-color": [{
                border: [o]
            }],
            "border-color-x": [{
                "border-x": [o]
            }],
            "border-color-y": [{
                "border-y": [o]
            }],
            "border-color-s": [{
                "border-s": [o]
            }],
            "border-color-e": [{
                "border-e": [o]
            }],
            "border-color-t": [{
                "border-t": [o]
            }],
            "border-color-r": [{
                "border-r": [o]
            }],
            "border-color-b": [{
                "border-b": [o]
            }],
            "border-color-l": [{
                "border-l": [o]
            }],
            "divide-color": [{
                divide: [o]
            }],
            "outline-style": [{
                outline: ["", ...$()]
            }],
            "outline-offset": [{
                "outline-offset": [Nn, Z]
            }],
            "outline-w": [{
                outline: [Nn, Un]
            }],
            "outline-color": [{
                outline: [e]
            }],
            "ring-w": [{
                ring: W()
            }],
            "ring-w-inset": ["ring-inset"],
            "ring-color": [{
                ring: [e]
            }],
            "ring-opacity": [{
                "ring-opacity": [y]
            }],
            "ring-offset-w": [{
                "ring-offset": [Nn, Un]
            }],
            "ring-offset-color": [{
                "ring-offset": [e]
            }],
            shadow: [{
                shadow: ["", "inner", "none", Yn, lj]
            }],
            "shadow-color": [{
                shadow: [_s]
            }],
            opacity: [{
                opacity: [y]
            }],
            "mix-blend": [{
                "mix-blend": [...M(), "plus-lighter", "plus-darker"]
            }],
            "bg-blend": [{
                "bg-blend": M()
            }],
            filter: [{
                filter: ["", "none"]
            }],
            blur: [{
                blur: [n]
            }],
            brightness: [{
                brightness: [r]
            }],
            contrast: [{
                contrast: [c]
            }],
            "drop-shadow": [{
                "drop-shadow": ["", "none", Yn, Z]
            }],
            grayscale: [{
                grayscale: [u]
            }],
            "hue-rotate": [{
                "hue-rotate": [d]
            }],
            invert: [{
                invert: [f]
            }],
            saturate: [{
                saturate: [x]
            }],
            sepia: [{
                sepia: [S]
            }],
            "backdrop-filter": [{
                "backdrop-filter": ["", "none"]
            }],
            "backdrop-blur": [{
                "backdrop-blur": [n]
            }],
            "backdrop-brightness": [{
                "backdrop-brightness": [r]
            }],
            "backdrop-contrast": [{
                "backdrop-contrast": [c]
            }],
            "backdrop-grayscale": [{
                "backdrop-grayscale": [u]
            }],
            "backdrop-hue-rotate": [{
                "backdrop-hue-rotate": [d]
            }],
            "backdrop-invert": [{
                "backdrop-invert": [f]
            }],
            "backdrop-opacity": [{
                "backdrop-opacity": [y]
            }],
            "backdrop-saturate": [{
                "backdrop-saturate": [x]
            }],
            "backdrop-sepia": [{
                "backdrop-sepia": [S]
            }],
            "border-collapse": [{
                border: ["collapse", "separate"]
            }],
            "border-spacing": [{
                "border-spacing": [i]
            }],
            "border-spacing-x": [{
                "border-spacing-x": [i]
            }],
            "border-spacing-y": [{
                "border-spacing-y": [i]
            }],
            "table-layout": [{
                table: ["auto", "fixed"]
            }],
            caption: [{
                caption: ["top", "bottom"]
            }],
            transition: [{
                transition: ["none", "all", "", "colors", "opacity", "shadow", "transform", Z]
            }],
            duration: [{
                duration: U()
            }],
            ease: [{
                ease: ["linear", "in", "out", "in-out", Z]
            }],
            delay: [{
                delay: U()
            }],
            animate: [{
                animate: ["none", "spin", "ping", "pulse", "bounce", Z]
            }],
            transform: [{
                transform: ["", "gpu", "none"]
            }],
            scale: [{
                scale: [N]
            }],
            "scale-x": [{
                "scale-x": [N]
            }],
            "scale-y": [{
                "scale-y": [N]
            }],
            rotate: [{
                rotate: [Rs, Z]
            }],
            "translate-x": [{
                "translate-x": [T]
            }],
            "translate-y": [{
                "translate-y": [T]
            }],
            "skew-x": [{
                "skew-x": [k]
            }],
            "skew-y": [{
                "skew-y": [k]
            }],
            "transform-origin": [{
                origin: ["center", "top", "top-right", "right", "bottom-right", "bottom", "bottom-left", "left", "top-left", Z]
            }],
            accent: [{
                accent: ["auto", e]
            }],
            appearance: [{
                appearance: ["none", "auto"]
            }],
            cursor: [{
                cursor: ["auto", "default", "pointer", "wait", "text", "move", "help", "not-allowed", "none", "context-menu", "progress", "cell", "crosshair", "vertical-text", "alias", "copy", "no-drop", "grab", "grabbing", "all-scroll", "col-resize", "row-resize", "n-resize", "e-resize", "s-resize", "w-resize", "ne-resize", "nw-resize", "se-resize", "sw-resize", "ew-resize", "ns-resize", "nesw-resize", "nwse-resize", "zoom-in", "zoom-out", Z]
            }],
            "caret-color": [{
                caret: [e]
            }],
            "pointer-events": [{
                "pointer-events": ["none", "auto"]
            }],
            resize: [{
                resize: ["none", "y", "x", ""]
            }],
            "scroll-behavior": [{
                scroll: ["auto", "smooth"]
            }],
            "scroll-m": [{
                "scroll-m": A()
            }],
            "scroll-mx": [{
                "scroll-mx": A()
            }],
            "scroll-my": [{
                "scroll-my": A()
            }],
            "scroll-ms": [{
                "scroll-ms": A()
            }],
            "scroll-me": [{
                "scroll-me": A()
            }],
            "scroll-mt": [{
                "scroll-mt": A()
            }],
            "scroll-mr": [{
                "scroll-mr": A()
            }],
            "scroll-mb": [{
                "scroll-mb": A()
            }],
            "scroll-ml": [{
                "scroll-ml": A()
            }],
            "scroll-p": [{
                "scroll-p": A()
            }],
            "scroll-px": [{
                "scroll-px": A()
            }],
            "scroll-py": [{
                "scroll-py": A()
            }],
            "scroll-ps": [{
                "scroll-ps": A()
            }],
            "scroll-pe": [{
                "scroll-pe": A()
            }],
            "scroll-pt": [{
                "scroll-pt": A()
            }],
            "scroll-pr": [{
                "scroll-pr": A()
            }],
            "scroll-pb": [{
                "scroll-pb": A()
            }],
            "scroll-pl": [{
                "scroll-pl": A()
            }],
            "snap-align": [{
                snap: ["start", "end", "center", "align-none"]
            }],
            "snap-stop": [{
                snap: ["normal", "always"]
            }],
            "snap-type": [{
                snap: ["none", "x", "y", "both"]
            }],
            "snap-strictness": [{
                snap: ["mandatory", "proximity"]
            }],
            touch: [{
                touch: ["auto", "none", "manipulation"]
            }],
            "touch-x": [{
                "touch-pan": ["x", "left", "right"]
            }],
            "touch-y": [{
                "touch-pan": ["y", "up", "down"]
            }],
            "touch-pz": ["touch-pinch-zoom"],
            select: [{
                select: ["none", "text", "all", "auto"]
            }],
            "will-change": [{
                "will-change": ["auto", "scroll", "contents", "transform", Z]
            }],
            fill: [{
                fill: [e, "none"]
            }],
            "stroke-w": [{
                stroke: [Nn, Un, Tc]
            }],
            stroke: [{
                stroke: [e, "none"]
            }],
            sr: ["sr-only", "not-sr-only"],
            "forced-color-adjust": [{
                "forced-color-adjust": ["auto", "none"]
            }]
        },
        conflictingClassGroups: {
            overflow: ["overflow-x", "overflow-y"],
            overscroll: ["overscroll-x", "overscroll-y"],
            inset: ["inset-x", "inset-y", "start", "end", "top", "right", "bottom", "left"],
            "inset-x": ["right", "left"],
            "inset-y": ["top", "bottom"],
            flex: ["basis", "grow", "shrink"],
            gap: ["gap-x", "gap-y"],
            p: ["px", "py", "ps", "pe", "pt", "pr", "pb", "pl"],
            px: ["pr", "pl"],
            py: ["pt", "pb"],
            m: ["mx", "my", "ms", "me", "mt", "mr", "mb", "ml"],
            mx: ["mr", "ml"],
            my: ["mt", "mb"],
            size: ["w", "h"],
            "font-size": ["leading"],
            "fvn-normal": ["fvn-ordinal", "fvn-slashed-zero", "fvn-figure", "fvn-spacing", "fvn-fraction"],
            "fvn-ordinal": ["fvn-normal"],
            "fvn-slashed-zero": ["fvn-normal"],
            "fvn-figure": ["fvn-normal"],
            "fvn-spacing": ["fvn-normal"],
            "fvn-fraction": ["fvn-normal"],
            "line-clamp": ["display", "overflow"],
            rounded: ["rounded-s", "rounded-e", "rounded-t", "rounded-r", "rounded-b", "rounded-l", "rounded-ss", "rounded-se", "rounded-ee", "rounded-es", "rounded-tl", "rounded-tr", "rounded-br", "rounded-bl"],
            "rounded-s": ["rounded-ss", "rounded-es"],
            "rounded-e": ["rounded-se", "rounded-ee"],
            "rounded-t": ["rounded-tl", "rounded-tr"],
            "rounded-r": ["rounded-tr", "rounded-br"],
            "rounded-b": ["rounded-br", "rounded-bl"],
            "rounded-l": ["rounded-tl", "rounded-bl"],
            "border-spacing": ["border-spacing-x", "border-spacing-y"],
            "border-w": ["border-w-s", "border-w-e", "border-w-t", "border-w-r", "border-w-b", "border-w-l"],
            "border-w-x": ["border-w-r", "border-w-l"],
            "border-w-y": ["border-w-t", "border-w-b"],
            "border-color": ["border-color-s", "border-color-e", "border-color-t", "border-color-r", "border-color-b", "border-color-l"],
            "border-color-x": ["border-color-r", "border-color-l"],
            "border-color-y": ["border-color-t", "border-color-b"],
            "scroll-m": ["scroll-mx", "scroll-my", "scroll-ms", "scroll-me", "scroll-mt", "scroll-mr", "scroll-mb", "scroll-ml"],
            "scroll-mx": ["scroll-mr", "scroll-ml"],
            "scroll-my": ["scroll-mt", "scroll-mb"],
            "scroll-p": ["scroll-px", "scroll-py", "scroll-ps", "scroll-pe", "scroll-pt", "scroll-pr", "scroll-pb", "scroll-pl"],
            "scroll-px": ["scroll-pr", "scroll-pl"],
            "scroll-py": ["scroll-pt", "scroll-pb"],
            touch: ["touch-x", "touch-y", "touch-pz"],
            "touch-x": ["touch"],
            "touch-y": ["touch"],
            "touch-pz": ["touch"]
        },
        conflictingClassGroupModifiers: {
            "font-size": ["leading"]
        }
    }
}
  , mj = QS(fj);
function re(...e) {
    return mj(py(e))
}
const hj = dS
  , ky = m.forwardRef( ({className: e, ...t}, n) => a.jsx(ly, {
    ref: n,
    className: re("fixed top-0 z-[100] flex max-h-screen w-full flex-col-reverse p-4 sm:bottom-0 sm:right-0 sm:top-auto sm:flex-col md:max-w-[420px]", e),
    ...t
}));
ky.displayName = ly.displayName;
const pj = Ol("group pointer-events-auto relative flex w-full items-center justify-between space-x-4 overflow-hidden rounded-md border p-6 pr-8 shadow-lg transition-all data-[swipe=cancel]:translate-x-0 data-[swipe=end]:translate-x-[var(--radix-toast-swipe-end-x)] data-[swipe=move]:translate-x-[var(--radix-toast-swipe-move-x)] data-[swipe=move]:transition-none data-[state=open]:animate-in data-[state=closed]:animate-out data-[swipe=end]:animate-out data-[state=closed]:fade-out-80 data-[state=closed]:slide-out-to-right-full data-[state=open]:slide-in-from-top-full data-[state=open]:sm:slide-in-from-bottom-full", {
    variants: {
        variant: {
            default: "border bg-background text-foreground",
            destructive: "destructive group border-destructive bg-destructive text-destructive-foreground"
        }
    },
    defaultVariants: {
        variant: "default"
    }
})
  , Ey = m.forwardRef( ({className: e, variant: t, ...n}, r) => a.jsx(cy, {
    ref: r,
    className: re(pj({
        variant: t
    }), e),
    ...n
}));
Ey.displayName = cy.displayName;
const vj = m.forwardRef( ({className: e, ...t}, n) => a.jsx(fy, {
    ref: n,
    className: re("inline-flex h-8 shrink-0 items-center justify-center rounded-md border bg-transparent px-3 text-sm font-medium ring-offset-background transition-colors group-[.destructive]:border-muted/40 hover:bg-secondary group-[.destructive]:hover:border-destructive/30 group-[.destructive]:hover:bg-destructive group-[.destructive]:hover:text-destructive-foreground focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 group-[.destructive]:focus:ring-destructive disabled:pointer-events-none disabled:opacity-50", e),
    ...t
}));
vj.displayName = fy.displayName;
const Py = m.forwardRef( ({className: e, ...t}, n) => a.jsx(my, {
    ref: n,
    className: re("absolute right-2 top-2 rounded-md p-1 text-foreground/50 opacity-0 transition-opacity group-hover:opacity-100 group-[.destructive]:text-red-300 hover:text-foreground group-[.destructive]:hover:text-red-50 focus:opacity-100 focus:outline-none focus:ring-2 group-[.destructive]:focus:ring-red-400 group-[.destructive]:focus:ring-offset-red-600", e),
    "toast-close": "",
    ...t,
    children: a.jsx(yf, {
        className: "h-4 w-4"
    })
}));
Py.displayName = my.displayName;
const Ty = m.forwardRef( ({className: e, ...t}, n) => a.jsx(uy, {
    ref: n,
    className: re("text-sm font-semibold", e),
    ...t
}));
Ty.displayName = uy.displayName;
const My = m.forwardRef( ({className: e, ...t}, n) => a.jsx(dy, {
    ref: n,
    className: re("text-sm opacity-90", e),
    ...t
}));
My.displayName = dy.displayName;
function gj() {
    const {toasts: e} = wN();
    return a.jsxs(hj, {
        children: [e.map(function({id: t, title: n, description: r, action: o, ...s}) {
            return a.jsxs(Ey, {
                ...s,
                children: [a.jsxs("div", {
                    className: "grid gap-1",
                    children: [n && a.jsx(Ty, {
                        children: n
                    }), r && a.jsx(My, {
                        children: r
                    })]
                }), o, a.jsx(Py, {})]
            }, t)
        }), a.jsx(ky, {})]
    })
}
var Ch = ["light", "dark"]
  , yj = "(prefers-color-scheme: dark)"
  , xj = m.createContext(void 0)
  , wj = {
    setTheme: e => {}
    ,
    themes: []
}
  , bj = () => {
    var e;
    return (e = m.useContext(xj)) != null ? e : wj
}
;
m.memo( ({forcedTheme: e, storageKey: t, attribute: n, enableSystem: r, enableColorScheme: o, defaultTheme: s, value: i, attrs: l, nonce: c}) => {
    let u = s === "system"
      , d = n === "class" ? `var d=document.documentElement,c=d.classList;${`c.remove(${l.map(b => `'${b}'`).join(",")})`};` : `var d=document.documentElement,n='${n}',s='setAttribute';`
      , f = o ? Ch.includes(s) && s ? `if(e==='light'||e==='dark'||!e)d.style.colorScheme=e||'${s}'` : "if(e==='light'||e==='dark')d.style.colorScheme=e" : ""
      , g = (b, v=!1, w=!0) => {
        let y = i ? i[b] : b
          , p = v ? b + "|| ''" : `'${y}'`
          , x = "";
        return o && w && !v && Ch.includes(b) && (x += `d.style.colorScheme = '${b}';`),
        n === "class" ? v || y ? x += `c.add(${p})` : x += "null" : y && (x += `d[s](n,${p})`),
        x
    }
      , h = e ? `!function(){${d}${g(e)}}()` : r ? `!function(){try{${d}var e=localStorage.getItem('${t}');if('system'===e||(!e&&${u})){var t='${yj}',m=window.matchMedia(t);if(m.media!==t||m.matches){${g("dark")}}else{${g("light")}}}else if(e){${i ? `var x=${JSON.stringify(i)};` : ""}${g(i ? "x[e]" : "e", !0)}}${u ? "" : "else{" + g(s, !1, !1) + "}"}${f}}catch(e){}}()` : `!function(){try{${d}var e=localStorage.getItem('${t}');if(e){${i ? `var x=${JSON.stringify(i)};` : ""}${g(i ? "x[e]" : "e", !0)}}else{${g(s, !1, !1)};}${f}}catch(t){}}();`;
    return m.createElement("script", {
        nonce: c,
        dangerouslySetInnerHTML: {
            __html: h
        }
    })
}
);
var Nj = e => {
    switch (e) {
    case "success":
        return Cj;
    case "info":
        return Ej;
    case "warning":
        return kj;
    case "error":
        return Pj;
    default:
        return null
    }
}
  , Sj = Array(12).fill(0)
  , jj = ({visible: e, className: t}) => I.createElement("div", {
    className: ["sonner-loading-wrapper", t].filter(Boolean).join(" "),
    "data-visible": e
}, I.createElement("div", {
    className: "sonner-spinner"
}, Sj.map( (n, r) => I.createElement("div", {
    className: "sonner-loading-bar",
    key: `spinner-bar-${r}`
}))))
  , Cj = I.createElement("svg", {
    xmlns: "http://www.w3.org/2000/svg",
    viewBox: "0 0 20 20",
    fill: "currentColor",
    height: "20",
    width: "20"
}, I.createElement("path", {
    fillRule: "evenodd",
    d: "M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z",
    clipRule: "evenodd"
}))
  , kj = I.createElement("svg", {
    xmlns: "http://www.w3.org/2000/svg",
    viewBox: "0 0 24 24",
    fill: "currentColor",
    height: "20",
    width: "20"
}, I.createElement("path", {
    fillRule: "evenodd",
    d: "M9.401 3.003c1.155-2 4.043-2 5.197 0l7.355 12.748c1.154 2-.29 4.5-2.599 4.5H4.645c-2.309 0-3.752-2.5-2.598-4.5L9.4 3.003zM12 8.25a.75.75 0 01.75.75v3.75a.75.75 0 01-1.5 0V9a.75.75 0 01.75-.75zm0 8.25a.75.75 0 100-1.5.75.75 0 000 1.5z",
    clipRule: "evenodd"
}))
  , Ej = I.createElement("svg", {
    xmlns: "http://www.w3.org/2000/svg",
    viewBox: "0 0 20 20",
    fill: "currentColor",
    height: "20",
    width: "20"
}, I.createElement("path", {
    fillRule: "evenodd",
    d: "M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a.75.75 0 000 1.5h.253a.25.25 0 01.244.304l-.459 2.066A1.75 1.75 0 0010.747 15H11a.75.75 0 000-1.5h-.253a.25.25 0 01-.244-.304l.459-2.066A1.75 1.75 0 009.253 9H9z",
    clipRule: "evenodd"
}))
  , Pj = I.createElement("svg", {
    xmlns: "http://www.w3.org/2000/svg",
    viewBox: "0 0 20 20",
    fill: "currentColor",
    height: "20",
    width: "20"
}, I.createElement("path", {
    fillRule: "evenodd",
    d: "M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-8-5a.75.75 0 01.75.75v4.5a.75.75 0 01-1.5 0v-4.5A.75.75 0 0110 5zm0 10a1 1 0 100-2 1 1 0 000 2z",
    clipRule: "evenodd"
}))
  , Tj = I.createElement("svg", {
    xmlns: "http://www.w3.org/2000/svg",
    width: "12",
    height: "12",
    viewBox: "0 0 24 24",
    fill: "none",
    stroke: "currentColor",
    strokeWidth: "1.5",
    strokeLinecap: "round",
    strokeLinejoin: "round"
}, I.createElement("line", {
    x1: "18",
    y1: "6",
    x2: "6",
    y2: "18"
}), I.createElement("line", {
    x1: "6",
    y1: "6",
    x2: "18",
    y2: "18"
}))
  , Mj = () => {
    let[e,t] = I.useState(document.hidden);
    return I.useEffect( () => {
        let n = () => {
            t(document.hidden)
        }
        ;
        return document.addEventListener("visibilitychange", n),
        () => window.removeEventListener("visibilitychange", n)
    }
    , []),
    e
}
  , Gu = 1
  , Rj = class {
    constructor() {
        this.subscribe = e => (this.subscribers.push(e),
        () => {
            let t = this.subscribers.indexOf(e);
            this.subscribers.splice(t, 1)
        }
        ),
        this.publish = e => {
            this.subscribers.forEach(t => t(e))
        }
        ,
        this.addToast = e => {
            this.publish(e),
            this.toasts = [...this.toasts, e]
        }
        ,
        this.create = e => {
            var t;
            let {message: n, ...r} = e
              , o = typeof (e == null ? void 0 : e.id) == "number" || ((t = e.id) == null ? void 0 : t.length) > 0 ? e.id : Gu++
              , s = this.toasts.find(l => l.id === o)
              , i = e.dismissible === void 0 ? !0 : e.dismissible;
            return this.dismissedToasts.has(o) && this.dismissedToasts.delete(o),
            s ? this.toasts = this.toasts.map(l => l.id === o ? (this.publish({
                ...l,
                ...e,
                id: o,
                title: n
            }),
            {
                ...l,
                ...e,
                id: o,
                dismissible: i,
                title: n
            }) : l) : this.addToast({
                title: n,
                ...r,
                dismissible: i,
                id: o
            }),
            o
        }
        ,
        this.dismiss = e => (this.dismissedToasts.add(e),
        e || this.toasts.forEach(t => {
            this.subscribers.forEach(n => n({
                id: t.id,
                dismiss: !0
            }))
        }
        ),
        this.subscribers.forEach(t => t({
            id: e,
            dismiss: !0
        })),
        e),
        this.message = (e, t) => this.create({
            ...t,
            message: e
        }),
        this.error = (e, t) => this.create({
            ...t,
            message: e,
            type: "error"
        }),
        this.success = (e, t) => this.create({
            ...t,
            type: "success",
            message: e
        }),
        this.info = (e, t) => this.create({
            ...t,
            type: "info",
            message: e
        }),
        this.warning = (e, t) => this.create({
            ...t,
            type: "warning",
            message: e
        }),
        this.loading = (e, t) => this.create({
            ...t,
            type: "loading",
            message: e
        }),
        this.promise = (e, t) => {
            if (!t)
                return;
            let n;
            t.loading !== void 0 && (n = this.create({
                ...t,
                promise: e,
                type: "loading",
                message: t.loading,
                description: typeof t.description != "function" ? t.description : void 0
            }));
            let r = e instanceof Promise ? e : e(), o = n !== void 0, s, i = r.then(async c => {
                if (s = ["resolve", c],
                I.isValidElement(c))
                    o = !1,
                    this.create({
                        id: n,
                        type: "default",
                        message: c
                    });
                else if (Dj(c) && !c.ok) {
                    o = !1;
                    let u = typeof t.error == "function" ? await t.error(`HTTP error! status: ${c.status}`) : t.error
                      , d = typeof t.description == "function" ? await t.description(`HTTP error! status: ${c.status}`) : t.description;
                    this.create({
                        id: n,
                        type: "error",
                        message: u,
                        description: d
                    })
                } else if (t.success !== void 0) {
                    o = !1;
                    let u = typeof t.success == "function" ? await t.success(c) : t.success
                      , d = typeof t.description == "function" ? await t.description(c) : t.description;
                    this.create({
                        id: n,
                        type: "success",
                        message: u,
                        description: d
                    })
                }
            }
            ).catch(async c => {
                if (s = ["reject", c],
                t.error !== void 0) {
                    o = !1;
                    let u = typeof t.error == "function" ? await t.error(c) : t.error
                      , d = typeof t.description == "function" ? await t.description(c) : t.description;
                    this.create({
                        id: n,
                        type: "error",
                        message: u,
                        description: d
                    })
                }
            }
            ).finally( () => {
                var c;
                o && (this.dismiss(n),
                n = void 0),
                (c = t.finally) == null || c.call(t)
            }
            ), l = () => new Promise( (c, u) => i.then( () => s[0] === "reject" ? u(s[1]) : c(s[1])).catch(u));
            return typeof n != "string" && typeof n != "number" ? {
                unwrap: l
            } : Object.assign(n, {
                unwrap: l
            })
        }
        ,
        this.custom = (e, t) => {
            let n = (t == null ? void 0 : t.id) || Gu++;
            return this.create({
                jsx: e(n),
                id: n,
                ...t
            }),
            n
        }
        ,
        this.getActiveToasts = () => this.toasts.filter(e => !this.dismissedToasts.has(e.id)),
        this.subscribers = [],
        this.toasts = [],
        this.dismissedToasts = new Set
    }
}
  , it = new Rj
  , _j = (e, t) => {
    let n = (t == null ? void 0 : t.id) || Gu++;
    return it.addToast({
        title: e,
        ...t,
        id: n
    }),
    n
}
  , Dj = e => e && typeof e == "object" && "ok"in e && typeof e.ok == "boolean" && "status"in e && typeof e.status == "number"
  , Oj = _j
  , Aj = () => it.toasts
  , Ij = () => it.getActiveToasts();
Object.assign(Oj, {
    success: it.success,
    info: it.info,
    warning: it.warning,
    error: it.error,
    custom: it.custom,
    message: it.message,
    promise: it.promise,
    dismiss: it.dismiss,
    loading: it.loading
}, {
    getHistory: Aj,
    getToasts: Ij
});
function Lj(e, {insertAt: t}={}) {
    if (typeof document > "u")
        return;
    let n = document.head || document.getElementsByTagName("head")[0]
      , r = document.createElement("style");
    r.type = "text/css",
    t === "top" && n.firstChild ? n.insertBefore(r, n.firstChild) : n.appendChild(r),
    r.styleSheet ? r.styleSheet.cssText = e : r.appendChild(document.createTextNode(e))
}
Lj(`:where(html[dir="ltr"]),:where([data-sonner-toaster][dir="ltr"]){--toast-icon-margin-start: -3px;--toast-icon-margin-end: 4px;--toast-svg-margin-start: -1px;--toast-svg-margin-end: 0px;--toast-button-margin-start: auto;--toast-button-margin-end: 0;--toast-close-button-start: 0;--toast-close-button-end: unset;--toast-close-button-transform: translate(-35%, -35%)}:where(html[dir="rtl"]),:where([data-sonner-toaster][dir="rtl"]){--toast-icon-margin-start: 4px;--toast-icon-margin-end: -3px;--toast-svg-margin-start: 0px;--toast-svg-margin-end: -1px;--toast-button-margin-start: 0;--toast-button-margin-end: auto;--toast-close-button-start: unset;--toast-close-button-end: 0;--toast-close-button-transform: translate(35%, -35%)}:where([data-sonner-toaster]){position:fixed;width:var(--width);font-family:ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,Noto Sans,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji;--gray1: hsl(0, 0%, 99%);--gray2: hsl(0, 0%, 97.3%);--gray3: hsl(0, 0%, 95.1%);--gray4: hsl(0, 0%, 93%);--gray5: hsl(0, 0%, 90.9%);--gray6: hsl(0, 0%, 88.7%);--gray7: hsl(0, 0%, 85.8%);--gray8: hsl(0, 0%, 78%);--gray9: hsl(0, 0%, 56.1%);--gray10: hsl(0, 0%, 52.3%);--gray11: hsl(0, 0%, 43.5%);--gray12: hsl(0, 0%, 9%);--border-radius: 8px;box-sizing:border-box;padding:0;margin:0;list-style:none;outline:none;z-index:999999999;transition:transform .4s ease}:where([data-sonner-toaster][data-lifted="true"]){transform:translateY(-10px)}@media (hover: none) and (pointer: coarse){:where([data-sonner-toaster][data-lifted="true"]){transform:none}}:where([data-sonner-toaster][data-x-position="right"]){right:var(--offset-right)}:where([data-sonner-toaster][data-x-position="left"]){left:var(--offset-left)}:where([data-sonner-toaster][data-x-position="center"]){left:50%;transform:translate(-50%)}:where([data-sonner-toaster][data-y-position="top"]){top:var(--offset-top)}:where([data-sonner-toaster][data-y-position="bottom"]){bottom:var(--offset-bottom)}:where([data-sonner-toast]){--y: translateY(100%);--lift-amount: calc(var(--lift) * var(--gap));z-index:var(--z-index);position:absolute;opacity:0;transform:var(--y);filter:blur(0);touch-action:none;transition:transform .4s,opacity .4s,height .4s,box-shadow .2s;box-sizing:border-box;outline:none;overflow-wrap:anywhere}:where([data-sonner-toast][data-styled="true"]){padding:16px;background:var(--normal-bg);border:1px solid var(--normal-border);color:var(--normal-text);border-radius:var(--border-radius);box-shadow:0 4px 12px #0000001a;width:var(--width);font-size:13px;display:flex;align-items:center;gap:6px}:where([data-sonner-toast]:focus-visible){box-shadow:0 4px 12px #0000001a,0 0 0 2px #0003}:where([data-sonner-toast][data-y-position="top"]){top:0;--y: translateY(-100%);--lift: 1;--lift-amount: calc(1 * var(--gap))}:where([data-sonner-toast][data-y-position="bottom"]){bottom:0;--y: translateY(100%);--lift: -1;--lift-amount: calc(var(--lift) * var(--gap))}:where([data-sonner-toast]) :where([data-description]){font-weight:400;line-height:1.4;color:inherit}:where([data-sonner-toast]) :where([data-title]){font-weight:500;line-height:1.5;color:inherit}:where([data-sonner-toast]) :where([data-icon]){display:flex;height:16px;width:16px;position:relative;justify-content:flex-start;align-items:center;flex-shrink:0;margin-left:var(--toast-icon-margin-start);margin-right:var(--toast-icon-margin-end)}:where([data-sonner-toast][data-promise="true"]) :where([data-icon])>svg{opacity:0;transform:scale(.8);transform-origin:center;animation:sonner-fade-in .3s ease forwards}:where([data-sonner-toast]) :where([data-icon])>*{flex-shrink:0}:where([data-sonner-toast]) :where([data-icon]) svg{margin-left:var(--toast-svg-margin-start);margin-right:var(--toast-svg-margin-end)}:where([data-sonner-toast]) :where([data-content]){display:flex;flex-direction:column;gap:2px}[data-sonner-toast][data-styled=true] [data-button]{border-radius:4px;padding-left:8px;padding-right:8px;height:24px;font-size:12px;color:var(--normal-bg);background:var(--normal-text);margin-left:var(--toast-button-margin-start);margin-right:var(--toast-button-margin-end);border:none;cursor:pointer;outline:none;display:flex;align-items:center;flex-shrink:0;transition:opacity .4s,box-shadow .2s}:where([data-sonner-toast]) :where([data-button]):focus-visible{box-shadow:0 0 0 2px #0006}:where([data-sonner-toast]) :where([data-button]):first-of-type{margin-left:var(--toast-button-margin-start);margin-right:var(--toast-button-margin-end)}:where([data-sonner-toast]) :where([data-cancel]){color:var(--normal-text);background:rgba(0,0,0,.08)}:where([data-sonner-toast][data-theme="dark"]) :where([data-cancel]){background:rgba(255,255,255,.3)}:where([data-sonner-toast]) :where([data-close-button]){position:absolute;left:var(--toast-close-button-start);right:var(--toast-close-button-end);top:0;height:20px;width:20px;display:flex;justify-content:center;align-items:center;padding:0;color:var(--gray12);border:1px solid var(--gray4);transform:var(--toast-close-button-transform);border-radius:50%;cursor:pointer;z-index:1;transition:opacity .1s,background .2s,border-color .2s}[data-sonner-toast] [data-close-button]{background:var(--gray1)}:where([data-sonner-toast]) :where([data-close-button]):focus-visible{box-shadow:0 4px 12px #0000001a,0 0 0 2px #0003}:where([data-sonner-toast]) :where([data-disabled="true"]){cursor:not-allowed}:where([data-sonner-toast]):hover :where([data-close-button]):hover{background:var(--gray2);border-color:var(--gray5)}:where([data-sonner-toast][data-swiping="true"]):before{content:"";position:absolute;left:-50%;right:-50%;height:100%;z-index:-1}:where([data-sonner-toast][data-y-position="top"][data-swiping="true"]):before{bottom:50%;transform:scaleY(3) translateY(50%)}:where([data-sonner-toast][data-y-position="bottom"][data-swiping="true"]):before{top:50%;transform:scaleY(3) translateY(-50%)}:where([data-sonner-toast][data-swiping="false"][data-removed="true"]):before{content:"";position:absolute;inset:0;transform:scaleY(2)}:where([data-sonner-toast]):after{content:"";position:absolute;left:0;height:calc(var(--gap) + 1px);bottom:100%;width:100%}:where([data-sonner-toast][data-mounted="true"]){--y: translateY(0);opacity:1}:where([data-sonner-toast][data-expanded="false"][data-front="false"]){--scale: var(--toasts-before) * .05 + 1;--y: translateY(calc(var(--lift-amount) * var(--toasts-before))) scale(calc(-1 * var(--scale)));height:var(--front-toast-height)}:where([data-sonner-toast])>*{transition:opacity .4s}:where([data-sonner-toast][data-expanded="false"][data-front="false"][data-styled="true"])>*{opacity:0}:where([data-sonner-toast][data-visible="false"]){opacity:0;pointer-events:none}:where([data-sonner-toast][data-mounted="true"][data-expanded="true"]){--y: translateY(calc(var(--lift) * var(--offset)));height:var(--initial-height)}:where([data-sonner-toast][data-removed="true"][data-front="true"][data-swipe-out="false"]){--y: translateY(calc(var(--lift) * -100%));opacity:0}:where([data-sonner-toast][data-removed="true"][data-front="false"][data-swipe-out="false"][data-expanded="true"]){--y: translateY(calc(var(--lift) * var(--offset) + var(--lift) * -100%));opacity:0}:where([data-sonner-toast][data-removed="true"][data-front="false"][data-swipe-out="false"][data-expanded="false"]){--y: translateY(40%);opacity:0;transition:transform .5s,opacity .2s}:where([data-sonner-toast][data-removed="true"][data-front="false"]):before{height:calc(var(--initial-height) + 20%)}[data-sonner-toast][data-swiping=true]{transform:var(--y) translateY(var(--swipe-amount-y, 0px)) translate(var(--swipe-amount-x, 0px));transition:none}[data-sonner-toast][data-swiped=true]{user-select:none}[data-sonner-toast][data-swipe-out=true][data-y-position=bottom],[data-sonner-toast][data-swipe-out=true][data-y-position=top]{animation-duration:.2s;animation-timing-function:ease-out;animation-fill-mode:forwards}[data-sonner-toast][data-swipe-out=true][data-swipe-direction=left]{animation-name:swipe-out-left}[data-sonner-toast][data-swipe-out=true][data-swipe-direction=right]{animation-name:swipe-out-right}[data-sonner-toast][data-swipe-out=true][data-swipe-direction=up]{animation-name:swipe-out-up}[data-sonner-toast][data-swipe-out=true][data-swipe-direction=down]{animation-name:swipe-out-down}@keyframes swipe-out-left{0%{transform:var(--y) translate(var(--swipe-amount-x));opacity:1}to{transform:var(--y) translate(calc(var(--swipe-amount-x) - 100%));opacity:0}}@keyframes swipe-out-right{0%{transform:var(--y) translate(var(--swipe-amount-x));opacity:1}to{transform:var(--y) translate(calc(var(--swipe-amount-x) + 100%));opacity:0}}@keyframes swipe-out-up{0%{transform:var(--y) translateY(var(--swipe-amount-y));opacity:1}to{transform:var(--y) translateY(calc(var(--swipe-amount-y) - 100%));opacity:0}}@keyframes swipe-out-down{0%{transform:var(--y) translateY(var(--swipe-amount-y));opacity:1}to{transform:var(--y) translateY(calc(var(--swipe-amount-y) + 100%));opacity:0}}@media (max-width: 600px){[data-sonner-toaster]{position:fixed;right:var(--mobile-offset-right);left:var(--mobile-offset-left);width:100%}[data-sonner-toaster][dir=rtl]{left:calc(var(--mobile-offset-left) * -1)}[data-sonner-toaster] [data-sonner-toast]{left:0;right:0;width:calc(100% - var(--mobile-offset-left) * 2)}[data-sonner-toaster][data-x-position=left]{left:var(--mobile-offset-left)}[data-sonner-toaster][data-y-position=bottom]{bottom:var(--mobile-offset-bottom)}[data-sonner-toaster][data-y-position=top]{top:var(--mobile-offset-top)}[data-sonner-toaster][data-x-position=center]{left:var(--mobile-offset-left);right:var(--mobile-offset-right);transform:none}}[data-sonner-toaster][data-theme=light]{--normal-bg: #fff;--normal-border: var(--gray4);--normal-text: var(--gray12);--success-bg: hsl(143, 85%, 96%);--success-border: hsl(145, 92%, 91%);--success-text: hsl(140, 100%, 27%);--info-bg: hsl(208, 100%, 97%);--info-border: hsl(221, 91%, 91%);--info-text: hsl(210, 92%, 45%);--warning-bg: hsl(49, 100%, 97%);--warning-border: hsl(49, 91%, 91%);--warning-text: hsl(31, 92%, 45%);--error-bg: hsl(359, 100%, 97%);--error-border: hsl(359, 100%, 94%);--error-text: hsl(360, 100%, 45%)}[data-sonner-toaster][data-theme=light] [data-sonner-toast][data-invert=true]{--normal-bg: #000;--normal-border: hsl(0, 0%, 20%);--normal-text: var(--gray1)}[data-sonner-toaster][data-theme=dark] [data-sonner-toast][data-invert=true]{--normal-bg: #fff;--normal-border: var(--gray3);--normal-text: var(--gray12)}[data-sonner-toaster][data-theme=dark]{--normal-bg: #000;--normal-bg-hover: hsl(0, 0%, 12%);--normal-border: hsl(0, 0%, 20%);--normal-border-hover: hsl(0, 0%, 25%);--normal-text: var(--gray1);--success-bg: hsl(150, 100%, 6%);--success-border: hsl(147, 100%, 12%);--success-text: hsl(150, 86%, 65%);--info-bg: hsl(215, 100%, 6%);--info-border: hsl(223, 100%, 12%);--info-text: hsl(216, 87%, 65%);--warning-bg: hsl(64, 100%, 6%);--warning-border: hsl(60, 100%, 12%);--warning-text: hsl(46, 87%, 65%);--error-bg: hsl(358, 76%, 10%);--error-border: hsl(357, 89%, 16%);--error-text: hsl(358, 100%, 81%)}[data-sonner-toaster][data-theme=dark] [data-sonner-toast] [data-close-button]{background:var(--normal-bg);border-color:var(--normal-border);color:var(--normal-text)}[data-sonner-toaster][data-theme=dark] [data-sonner-toast] [data-close-button]:hover{background:var(--normal-bg-hover);border-color:var(--normal-border-hover)}[data-rich-colors=true][data-sonner-toast][data-type=success],[data-rich-colors=true][data-sonner-toast][data-type=success] [data-close-button]{background:var(--success-bg);border-color:var(--success-border);color:var(--success-text)}[data-rich-colors=true][data-sonner-toast][data-type=info],[data-rich-colors=true][data-sonner-toast][data-type=info] [data-close-button]{background:var(--info-bg);border-color:var(--info-border);color:var(--info-text)}[data-rich-colors=true][data-sonner-toast][data-type=warning],[data-rich-colors=true][data-sonner-toast][data-type=warning] [data-close-button]{background:var(--warning-bg);border-color:var(--warning-border);color:var(--warning-text)}[data-rich-colors=true][data-sonner-toast][data-type=error],[data-rich-colors=true][data-sonner-toast][data-type=error] [data-close-button]{background:var(--error-bg);border-color:var(--error-border);color:var(--error-text)}.sonner-loading-wrapper{--size: 16px;height:var(--size);width:var(--size);position:absolute;inset:0;z-index:10}.sonner-loading-wrapper[data-visible=false]{transform-origin:center;animation:sonner-fade-out .2s ease forwards}.sonner-spinner{position:relative;top:50%;left:50%;height:var(--size);width:var(--size)}.sonner-loading-bar{animation:sonner-spin 1.2s linear infinite;background:var(--gray11);border-radius:6px;height:8%;left:-10%;position:absolute;top:-3.9%;width:24%}.sonner-loading-bar:nth-child(1){animation-delay:-1.2s;transform:rotate(.0001deg) translate(146%)}.sonner-loading-bar:nth-child(2){animation-delay:-1.1s;transform:rotate(30deg) translate(146%)}.sonner-loading-bar:nth-child(3){animation-delay:-1s;transform:rotate(60deg) translate(146%)}.sonner-loading-bar:nth-child(4){animation-delay:-.9s;transform:rotate(90deg) translate(146%)}.sonner-loading-bar:nth-child(5){animation-delay:-.8s;transform:rotate(120deg) translate(146%)}.sonner-loading-bar:nth-child(6){animation-delay:-.7s;transform:rotate(150deg) translate(146%)}.sonner-loading-bar:nth-child(7){animation-delay:-.6s;transform:rotate(180deg) translate(146%)}.sonner-loading-bar:nth-child(8){animation-delay:-.5s;transform:rotate(210deg) translate(146%)}.sonner-loading-bar:nth-child(9){animation-delay:-.4s;transform:rotate(240deg) translate(146%)}.sonner-loading-bar:nth-child(10){animation-delay:-.3s;transform:rotate(270deg) translate(146%)}.sonner-loading-bar:nth-child(11){animation-delay:-.2s;transform:rotate(300deg) translate(146%)}.sonner-loading-bar:nth-child(12){animation-delay:-.1s;transform:rotate(330deg) translate(146%)}@keyframes sonner-fade-in{0%{opacity:0;transform:scale(.8)}to{opacity:1;transform:scale(1)}}@keyframes sonner-fade-out{0%{opacity:1;transform:scale(1)}to{opacity:0;transform:scale(.8)}}@keyframes sonner-spin{0%{opacity:1}to{opacity:.15}}@media (prefers-reduced-motion){[data-sonner-toast],[data-sonner-toast]>*,.sonner-loading-bar{transition:none!important;animation:none!important}}.sonner-loader{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);transform-origin:center;transition:opacity .2s,transform .2s}.sonner-loader[data-visible=false]{opacity:0;transform:scale(.8) translate(-50%,-50%)}
`);
function ai(e) {
    return e.label !== void 0
}
var Fj = 3
  , zj = "32px"
  , $j = "16px"
  , kh = 4e3
  , Bj = 356
  , Wj = 14
  , Hj = 20
  , Vj = 200;
function zt(...e) {
    return e.filter(Boolean).join(" ")
}
function Uj(e) {
    let[t,n] = e.split("-")
      , r = [];
    return t && r.push(t),
    n && r.push(n),
    r
}
var Yj = e => {
    var t, n, r, o, s, i, l, c, u, d, f;
    let {invert: g, toast: h, unstyled: b, interacting: v, setHeights: w, visibleToasts: y, heights: p, index: x, toasts: N, expanded: S, removeToast: k, defaultRichColors: C, closeButton: T, style: D, cancelButtonStyle: R, actionButtonStyle: F, className: A="", descriptionClassName: W="", duration: O, position: V, gap: $, loadingIcon: M, expandByDefault: j, classNames: E, icons: L, closeButtonAriaLabel: U="Close toast", pauseWhenPageIsHidden: H} = e
      , [J,G] = I.useState(null)
      , [xe,Me] = I.useState(null)
      , [z,me] = I.useState(!1)
      , [Re,de] = I.useState(!1)
      , [oe,ce] = I.useState(!1)
      , [Ye,jt] = I.useState(!1)
      , [Tr,$n] = I.useState(!1)
      , [Mr,bs] = I.useState(0)
      , [uo,Zf] = I.useState(0)
      , Ns = I.useRef(h.duration || O || kh)
      , em = I.useRef(null)
      , Rr = I.useRef(null)
      , Ow = x === 0
      , Aw = x + 1 <= y
      , Ct = h.type
      , fo = h.dismissible !== !1
      , Iw = h.className || ""
      , Lw = h.descriptionClassName || ""
      , za = I.useMemo( () => p.findIndex(q => q.toastId === h.id) || 0, [p, h.id])
      , Fw = I.useMemo( () => {
        var q;
        return (q = h.closeButton) != null ? q : T
    }
    , [h.closeButton, T])
      , tm = I.useMemo( () => h.duration || O || kh, [h.duration, O])
      , Xl = I.useRef(0)
      , mo = I.useRef(0)
      , nm = I.useRef(0)
      , ho = I.useRef(null)
      , [zw,$w] = V.split("-")
      , rm = I.useMemo( () => p.reduce( (q, ve, Se) => Se >= za ? q : q + ve.height, 0), [p, za])
      , om = Mj()
      , Bw = h.invert || g
      , Jl = Ct === "loading";
    mo.current = I.useMemo( () => za * $ + rm, [za, rm]),
    I.useEffect( () => {
        Ns.current = tm
    }
    , [tm]),
    I.useEffect( () => {
        me(!0)
    }
    , []),
    I.useEffect( () => {
        let q = Rr.current;
        if (q) {
            let ve = q.getBoundingClientRect().height;
            return Zf(ve),
            w(Se => [{
                toastId: h.id,
                height: ve,
                position: h.position
            }, ...Se]),
            () => w(Se => Se.filter(At => At.toastId !== h.id))
        }
    }
    , [w, h.id]),
    I.useLayoutEffect( () => {
        if (!z)
            return;
        let q = Rr.current
          , ve = q.style.height;
        q.style.height = "auto";
        let Se = q.getBoundingClientRect().height;
        q.style.height = ve,
        Zf(Se),
        w(At => At.find(It => It.toastId === h.id) ? At.map(It => It.toastId === h.id ? {
            ...It,
            height: Se
        } : It) : [{
            toastId: h.id,
            height: Se,
            position: h.position
        }, ...At])
    }
    , [z, h.title, h.description, w, h.id]);
    let Bn = I.useCallback( () => {
        de(!0),
        bs(mo.current),
        w(q => q.filter(ve => ve.toastId !== h.id)),
        setTimeout( () => {
            k(h)
        }
        , Vj)
    }
    , [h, k, w, mo]);
    I.useEffect( () => {
        if (h.promise && Ct === "loading" || h.duration === 1 / 0 || h.type === "loading")
            return;
        let q;
        return S || v || H && om ? ( () => {
            if (nm.current < Xl.current) {
                let ve = new Date().getTime() - Xl.current;
                Ns.current = Ns.current - ve
            }
            nm.current = new Date().getTime()
        }
        )() : Ns.current !== 1 / 0 && (Xl.current = new Date().getTime(),
        q = setTimeout( () => {
            var ve;
            (ve = h.onAutoClose) == null || ve.call(h, h),
            Bn()
        }
        , Ns.current)),
        () => clearTimeout(q)
    }
    , [S, v, h, Ct, H, om, Bn]),
    I.useEffect( () => {
        h.delete && Bn()
    }
    , [Bn, h.delete]);
    function Ww() {
        var q, ve, Se;
        return L != null && L.loading ? I.createElement("div", {
            className: zt(E == null ? void 0 : E.loader, (q = h == null ? void 0 : h.classNames) == null ? void 0 : q.loader, "sonner-loader"),
            "data-visible": Ct === "loading"
        }, L.loading) : M ? I.createElement("div", {
            className: zt(E == null ? void 0 : E.loader, (ve = h == null ? void 0 : h.classNames) == null ? void 0 : ve.loader, "sonner-loader"),
            "data-visible": Ct === "loading"
        }, M) : I.createElement(jj, {
            className: zt(E == null ? void 0 : E.loader, (Se = h == null ? void 0 : h.classNames) == null ? void 0 : Se.loader),
            visible: Ct === "loading"
        })
    }
    return I.createElement("li", {
        tabIndex: 0,
        ref: Rr,
        className: zt(A, Iw, E == null ? void 0 : E.toast, (t = h == null ? void 0 : h.classNames) == null ? void 0 : t.toast, E == null ? void 0 : E.default, E == null ? void 0 : E[Ct], (n = h == null ? void 0 : h.classNames) == null ? void 0 : n[Ct]),
        "data-sonner-toast": "",
        "data-rich-colors": (r = h.richColors) != null ? r : C,
        "data-styled": !(h.jsx || h.unstyled || b),
        "data-mounted": z,
        "data-promise": !!h.promise,
        "data-swiped": Tr,
        "data-removed": Re,
        "data-visible": Aw,
        "data-y-position": zw,
        "data-x-position": $w,
        "data-index": x,
        "data-front": Ow,
        "data-swiping": oe,
        "data-dismissible": fo,
        "data-type": Ct,
        "data-invert": Bw,
        "data-swipe-out": Ye,
        "data-swipe-direction": xe,
        "data-expanded": !!(S || j && z),
        style: {
            "--index": x,
            "--toasts-before": x,
            "--z-index": N.length - x,
            "--offset": `${Re ? Mr : mo.current}px`,
            "--initial-height": j ? "auto" : `${uo}px`,
            ...D,
            ...h.style
        },
        onDragEnd: () => {
            ce(!1),
            G(null),
            ho.current = null
        }
        ,
        onPointerDown: q => {
            Jl || !fo || (em.current = new Date,
            bs(mo.current),
            q.target.setPointerCapture(q.pointerId),
            q.target.tagName !== "BUTTON" && (ce(!0),
            ho.current = {
                x: q.clientX,
                y: q.clientY
            }))
        }
        ,
        onPointerUp: () => {
            var q, ve, Se, At;
            if (Ye || !fo)
                return;
            ho.current = null;
            let It = Number(((q = Rr.current) == null ? void 0 : q.style.getPropertyValue("--swipe-amount-x").replace("px", "")) || 0)
              , Wn = Number(((ve = Rr.current) == null ? void 0 : ve.style.getPropertyValue("--swipe-amount-y").replace("px", "")) || 0)
              , _r = new Date().getTime() - ((Se = em.current) == null ? void 0 : Se.getTime())
              , Lt = J === "x" ? It : Wn
              , Hn = Math.abs(Lt) / _r;
            if (Math.abs(Lt) >= Hj || Hn > .11) {
                bs(mo.current),
                (At = h.onDismiss) == null || At.call(h, h),
                Me(J === "x" ? It > 0 ? "right" : "left" : Wn > 0 ? "down" : "up"),
                Bn(),
                jt(!0),
                $n(!1);
                return
            }
            ce(!1),
            G(null)
        }
        ,
        onPointerMove: q => {
            var ve, Se, At, It;
            if (!ho.current || !fo || ((ve = window.getSelection()) == null ? void 0 : ve.toString().length) > 0)
                return;
            let Wn = q.clientY - ho.current.y
              , _r = q.clientX - ho.current.x
              , Lt = (Se = e.swipeDirections) != null ? Se : Uj(V);
            !J && (Math.abs(_r) > 1 || Math.abs(Wn) > 1) && G(Math.abs(_r) > Math.abs(Wn) ? "x" : "y");
            let Hn = {
                x: 0,
                y: 0
            };
            J === "y" ? (Lt.includes("top") || Lt.includes("bottom")) && (Lt.includes("top") && Wn < 0 || Lt.includes("bottom") && Wn > 0) && (Hn.y = Wn) : J === "x" && (Lt.includes("left") || Lt.includes("right")) && (Lt.includes("left") && _r < 0 || Lt.includes("right") && _r > 0) && (Hn.x = _r),
            (Math.abs(Hn.x) > 0 || Math.abs(Hn.y) > 0) && $n(!0),
            (At = Rr.current) == null || At.style.setProperty("--swipe-amount-x", `${Hn.x}px`),
            (It = Rr.current) == null || It.style.setProperty("--swipe-amount-y", `${Hn.y}px`)
        }
    }, Fw && !h.jsx ? I.createElement("button", {
        "aria-label": U,
        "data-disabled": Jl,
        "data-close-button": !0,
        onClick: Jl || !fo ? () => {}
        : () => {
            var q;
            Bn(),
            (q = h.onDismiss) == null || q.call(h, h)
        }
        ,
        className: zt(E == null ? void 0 : E.closeButton, (o = h == null ? void 0 : h.classNames) == null ? void 0 : o.closeButton)
    }, (s = L == null ? void 0 : L.close) != null ? s : Tj) : null, h.jsx || m.isValidElement(h.title) ? h.jsx ? h.jsx : typeof h.title == "function" ? h.title() : h.title : I.createElement(I.Fragment, null, Ct || h.icon || h.promise ? I.createElement("div", {
        "data-icon": "",
        className: zt(E == null ? void 0 : E.icon, (i = h == null ? void 0 : h.classNames) == null ? void 0 : i.icon)
    }, h.promise || h.type === "loading" && !h.icon ? h.icon || Ww() : null, h.type !== "loading" ? h.icon || (L == null ? void 0 : L[Ct]) || Nj(Ct) : null) : null, I.createElement("div", {
        "data-content": "",
        className: zt(E == null ? void 0 : E.content, (l = h == null ? void 0 : h.classNames) == null ? void 0 : l.content)
    }, I.createElement("div", {
        "data-title": "",
        className: zt(E == null ? void 0 : E.title, (c = h == null ? void 0 : h.classNames) == null ? void 0 : c.title)
    }, typeof h.title == "function" ? h.title() : h.title), h.description ? I.createElement("div", {
        "data-description": "",
        className: zt(W, Lw, E == null ? void 0 : E.description, (u = h == null ? void 0 : h.classNames) == null ? void 0 : u.description)
    }, typeof h.description == "function" ? h.description() : h.description) : null), m.isValidElement(h.cancel) ? h.cancel : h.cancel && ai(h.cancel) ? I.createElement("button", {
        "data-button": !0,
        "data-cancel": !0,
        style: h.cancelButtonStyle || R,
        onClick: q => {
            var ve, Se;
            ai(h.cancel) && fo && ((Se = (ve = h.cancel).onClick) == null || Se.call(ve, q),
            Bn())
        }
        ,
        className: zt(E == null ? void 0 : E.cancelButton, (d = h == null ? void 0 : h.classNames) == null ? void 0 : d.cancelButton)
    }, h.cancel.label) : null, m.isValidElement(h.action) ? h.action : h.action && ai(h.action) ? I.createElement("button", {
        "data-button": !0,
        "data-action": !0,
        style: h.actionButtonStyle || F,
        onClick: q => {
            var ve, Se;
            ai(h.action) && ((Se = (ve = h.action).onClick) == null || Se.call(ve, q),
            !q.defaultPrevented && Bn())
        }
        ,
        className: zt(E == null ? void 0 : E.actionButton, (f = h == null ? void 0 : h.classNames) == null ? void 0 : f.actionButton)
    }, h.action.label) : null))
}
;
function Eh() {
    if (typeof window > "u" || typeof document > "u")
        return "ltr";
    let e = document.documentElement.getAttribute("dir");
    return e === "auto" || !e ? window.getComputedStyle(document.documentElement).direction : e
}
function Kj(e, t) {
    let n = {};
    return [e, t].forEach( (r, o) => {
        let s = o === 1
          , i = s ? "--mobile-offset" : "--offset"
          , l = s ? $j : zj;
        function c(u) {
            ["top", "right", "bottom", "left"].forEach(d => {
                n[`${i}-${d}`] = typeof u == "number" ? `${u}px` : u
            }
            )
        }
        typeof r == "number" || typeof r == "string" ? c(r) : typeof r == "object" ? ["top", "right", "bottom", "left"].forEach(u => {
            r[u] === void 0 ? n[`${i}-${u}`] = l : n[`${i}-${u}`] = typeof r[u] == "number" ? `${r[u]}px` : r[u]
        }
        ) : c(l)
    }
    ),
    n
}
var Qj = m.forwardRef(function(e, t) {
    let {invert: n, position: r="bottom-right", hotkey: o=["altKey", "KeyT"], expand: s, closeButton: i, className: l, offset: c, mobileOffset: u, theme: d="light", richColors: f, duration: g, style: h, visibleToasts: b=Fj, toastOptions: v, dir: w=Eh(), gap: y=Wj, loadingIcon: p, icons: x, containerAriaLabel: N="Notifications", pauseWhenPageIsHidden: S} = e
      , [k,C] = I.useState([])
      , T = I.useMemo( () => Array.from(new Set([r].concat(k.filter(H => H.position).map(H => H.position)))), [k, r])
      , [D,R] = I.useState([])
      , [F,A] = I.useState(!1)
      , [W,O] = I.useState(!1)
      , [V,$] = I.useState(d !== "system" ? d : typeof window < "u" && window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light")
      , M = I.useRef(null)
      , j = o.join("+").replace(/Key/g, "").replace(/Digit/g, "")
      , E = I.useRef(null)
      , L = I.useRef(!1)
      , U = I.useCallback(H => {
        C(J => {
            var G;
            return (G = J.find(xe => xe.id === H.id)) != null && G.delete || it.dismiss(H.id),
            J.filter( ({id: xe}) => xe !== H.id)
        }
        )
    }
    , []);
    return I.useEffect( () => it.subscribe(H => {
        if (H.dismiss) {
            C(J => J.map(G => G.id === H.id ? {
                ...G,
                delete: !0
            } : G));
            return
        }
        setTimeout( () => {
            $g.flushSync( () => {
                C(J => {
                    let G = J.findIndex(xe => xe.id === H.id);
                    return G !== -1 ? [...J.slice(0, G), {
                        ...J[G],
                        ...H
                    }, ...J.slice(G + 1)] : [H, ...J]
                }
                )
            }
            )
        }
        )
    }
    ), []),
    I.useEffect( () => {
        if (d !== "system") {
            $(d);
            return
        }
        if (d === "system" && (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? $("dark") : $("light")),
        typeof window > "u")
            return;
        let H = window.matchMedia("(prefers-color-scheme: dark)");
        try {
            H.addEventListener("change", ({matches: J}) => {
                $(J ? "dark" : "light")
            }
            )
        } catch {
            H.addListener( ({matches: G}) => {
                try {
                    $(G ? "dark" : "light")
                } catch (xe) {
                    console.error(xe)
                }
            }
            )
        }
    }
    , [d]),
    I.useEffect( () => {
        k.length <= 1 && A(!1)
    }
    , [k]),
    I.useEffect( () => {
        let H = J => {
            var G, xe;
            o.every(Me => J[Me] || J.code === Me) && (A(!0),
            (G = M.current) == null || G.focus()),
            J.code === "Escape" && (document.activeElement === M.current || (xe = M.current) != null && xe.contains(document.activeElement)) && A(!1)
        }
        ;
        return document.addEventListener("keydown", H),
        () => document.removeEventListener("keydown", H)
    }
    , [o]),
    I.useEffect( () => {
        if (M.current)
            return () => {
                E.current && (E.current.focus({
                    preventScroll: !0
                }),
                E.current = null,
                L.current = !1)
            }
    }
    , [M.current]),
    I.createElement("section", {
        ref: t,
        "aria-label": `${N} ${j}`,
        tabIndex: -1,
        "aria-live": "polite",
        "aria-relevant": "additions text",
        "aria-atomic": "false",
        suppressHydrationWarning: !0
    }, T.map( (H, J) => {
        var G;
        let[xe,Me] = H.split("-");
        return k.length ? I.createElement("ol", {
            key: H,
            dir: w === "auto" ? Eh() : w,
            tabIndex: -1,
            ref: M,
            className: l,
            "data-sonner-toaster": !0,
            "data-theme": V,
            "data-y-position": xe,
            "data-lifted": F && k.length > 1 && !s,
            "data-x-position": Me,
            style: {
                "--front-toast-height": `${((G = D[0]) == null ? void 0 : G.height) || 0}px`,
                "--width": `${Bj}px`,
                "--gap": `${y}px`,
                ...h,
                ...Kj(c, u)
            },
            onBlur: z => {
                L.current && !z.currentTarget.contains(z.relatedTarget) && (L.current = !1,
                E.current && (E.current.focus({
                    preventScroll: !0
                }),
                E.current = null))
            }
            ,
            onFocus: z => {
                z.target instanceof HTMLElement && z.target.dataset.dismissible === "false" || L.current || (L.current = !0,
                E.current = z.relatedTarget)
            }
            ,
            onMouseEnter: () => A(!0),
            onMouseMove: () => A(!0),
            onMouseLeave: () => {
                W || A(!1)
            }
            ,
            onDragEnd: () => A(!1),
            onPointerDown: z => {
                z.target instanceof HTMLElement && z.target.dataset.dismissible === "false" || O(!0)
            }
            ,
            onPointerUp: () => O(!1)
        }, k.filter(z => !z.position && J === 0 || z.position === H).map( (z, me) => {
            var Re, de;
            return I.createElement(Yj, {
                key: z.id,
                icons: x,
                index: me,
                toast: z,
                defaultRichColors: f,
                duration: (Re = v == null ? void 0 : v.duration) != null ? Re : g,
                className: v == null ? void 0 : v.className,
                descriptionClassName: v == null ? void 0 : v.descriptionClassName,
                invert: n,
                visibleToasts: b,
                closeButton: (de = v == null ? void 0 : v.closeButton) != null ? de : i,
                interacting: W,
                position: H,
                style: v == null ? void 0 : v.style,
                unstyled: v == null ? void 0 : v.unstyled,
                classNames: v == null ? void 0 : v.classNames,
                cancelButtonStyle: v == null ? void 0 : v.cancelButtonStyle,
                actionButtonStyle: v == null ? void 0 : v.actionButtonStyle,
                removeToast: U,
                toasts: k.filter(oe => oe.position == z.position),
                heights: D.filter(oe => oe.position == z.position),
                setHeights: R,
                expandByDefault: s,
                gap: y,
                loadingIcon: p,
                expanded: F,
                pauseWhenPageIsHidden: S,
                swipeDirections: e.swipeDirections
            })
        }
        )) : null
    }
    ))
});
const Gj = ({...e}) => {
    const {theme: t="system"} = bj();
    return a.jsx(Qj, {
        theme: t,
        className: "toaster group",
        toastOptions: {
            classNames: {
                toast: "group toast group-[.toaster]:bg-background group-[.toaster]:text-foreground group-[.toaster]:border-border group-[.toaster]:shadow-lg",
                description: "group-[.toast]:text-muted-foreground",
                actionButton: "group-[.toast]:bg-primary group-[.toast]:text-primary-foreground",
                cancelButton: "group-[.toast]:bg-muted group-[.toast]:text-muted-foreground"
            }
        },
        ...e
    })
}
;
var qj = bd[" useId ".trim().toString()] || ( () => {}
)
  , Xj = 0;
function zo(e) {
    const [t,n] = m.useState(qj());
    return Ue( () => {
        n(r => r ?? String(Xj++))
    }
    , [e]),
    t ? `radix-${t}` : ""
}
const Jj = ["top", "right", "bottom", "left"]
  , br = Math.min
  , vt = Math.max
  , rl = Math.round
  , ii = Math.floor
  , gn = e => ({
    x: e,
    y: e
})
  , Zj = {
    left: "right",
    right: "left",
    bottom: "top",
    top: "bottom"
}
  , e2 = {
    start: "end",
    end: "start"
};
function qu(e, t, n) {
    return vt(e, br(t, n))
}
function Ln(e, t) {
    return typeof e == "function" ? e(t) : e
}
function Fn(e) {
    return e.split("-")[0]
}
function ps(e) {
    return e.split("-")[1]
}
function wf(e) {
    return e === "x" ? "y" : "x"
}
function bf(e) {
    return e === "y" ? "height" : "width"
}
const t2 = new Set(["top", "bottom"]);
function mn(e) {
    return t2.has(Fn(e)) ? "y" : "x"
}
function Nf(e) {
    return wf(mn(e))
}
function n2(e, t, n) {
    n === void 0 && (n = !1);
    const r = ps(e)
      , o = Nf(e)
      , s = bf(o);
    let i = o === "x" ? r === (n ? "end" : "start") ? "right" : "left" : r === "start" ? "bottom" : "top";
    return t.reference[s] > t.floating[s] && (i = ol(i)),
    [i, ol(i)]
}
function r2(e) {
    const t = ol(e);
    return [Xu(e), t, Xu(t)]
}
function Xu(e) {
    return e.replace(/start|end/g, t => e2[t])
}
const Ph = ["left", "right"]
  , Th = ["right", "left"]
  , o2 = ["top", "bottom"]
  , s2 = ["bottom", "top"];
function a2(e, t, n) {
    switch (e) {
    case "top":
    case "bottom":
        return n ? t ? Th : Ph : t ? Ph : Th;
    case "left":
    case "right":
        return t ? o2 : s2;
    default:
        return []
    }
}
function i2(e, t, n, r) {
    const o = ps(e);
    let s = a2(Fn(e), n === "start", r);
    return o && (s = s.map(i => i + "-" + o),
    t && (s = s.concat(s.map(Xu)))),
    s
}
function ol(e) {
    return e.replace(/left|right|bottom|top/g, t => Zj[t])
}
function l2(e) {
    return {
        top: 0,
        right: 0,
        bottom: 0,
        left: 0,
        ...e
    }
}
function Ry(e) {
    return typeof e != "number" ? l2(e) : {
        top: e,
        right: e,
        bottom: e,
        left: e
    }
}
function sl(e) {
    const {x: t, y: n, width: r, height: o} = e;
    return {
        width: r,
        height: o,
        top: n,
        left: t,
        right: t + r,
        bottom: n + o,
        x: t,
        y: n
    }
}
function Mh(e, t, n) {
    let {reference: r, floating: o} = e;
    const s = mn(t)
      , i = Nf(t)
      , l = bf(i)
      , c = Fn(t)
      , u = s === "y"
      , d = r.x + r.width / 2 - o.width / 2
      , f = r.y + r.height / 2 - o.height / 2
      , g = r[l] / 2 - o[l] / 2;
    let h;
    switch (c) {
    case "top":
        h = {
            x: d,
            y: r.y - o.height
        };
        break;
    case "bottom":
        h = {
            x: d,
            y: r.y + r.height
        };
        break;
    case "right":
        h = {
            x: r.x + r.width,
            y: f
        };
        break;
    case "left":
        h = {
            x: r.x - o.width,
            y: f
        };
        break;
    default:
        h = {
            x: r.x,
            y: r.y
        }
    }
    switch (ps(t)) {
    case "start":
        h[i] -= g * (n && u ? -1 : 1);
        break;
    case "end":
        h[i] += g * (n && u ? -1 : 1);
        break
    }
    return h
}
const c2 = async (e, t, n) => {
    const {placement: r="bottom", strategy: o="absolute", middleware: s=[], platform: i} = n
      , l = s.filter(Boolean)
      , c = await (i.isRTL == null ? void 0 : i.isRTL(t));
    let u = await i.getElementRects({
        reference: e,
        floating: t,
        strategy: o
    })
      , {x: d, y: f} = Mh(u, r, c)
      , g = r
      , h = {}
      , b = 0;
    for (let v = 0; v < l.length; v++) {
        const {name: w, fn: y} = l[v]
          , {x: p, y: x, data: N, reset: S} = await y({
            x: d,
            y: f,
            initialPlacement: r,
            placement: g,
            strategy: o,
            middlewareData: h,
            rects: u,
            platform: i,
            elements: {
                reference: e,
                floating: t
            }
        });
        d = p ?? d,
        f = x ?? f,
        h = {
            ...h,
            [w]: {
                ...h[w],
                ...N
            }
        },
        S && b <= 50 && (b++,
        typeof S == "object" && (S.placement && (g = S.placement),
        S.rects && (u = S.rects === !0 ? await i.getElementRects({
            reference: e,
            floating: t,
            strategy: o
        }) : S.rects),
        {x: d, y: f} = Mh(u, g, c)),
        v = -1)
    }
    return {
        x: d,
        y: f,
        placement: g,
        strategy: o,
        middlewareData: h
    }
}
;
async function pa(e, t) {
    var n;
    t === void 0 && (t = {});
    const {x: r, y: o, platform: s, rects: i, elements: l, strategy: c} = e
      , {boundary: u="clippingAncestors", rootBoundary: d="viewport", elementContext: f="floating", altBoundary: g=!1, padding: h=0} = Ln(t, e)
      , b = Ry(h)
      , w = l[g ? f === "floating" ? "reference" : "floating" : f]
      , y = sl(await s.getClippingRect({
        element: (n = await (s.isElement == null ? void 0 : s.isElement(w))) == null || n ? w : w.contextElement || await (s.getDocumentElement == null ? void 0 : s.getDocumentElement(l.floating)),
        boundary: u,
        rootBoundary: d,
        strategy: c
    }))
      , p = f === "floating" ? {
        x: r,
        y: o,
        width: i.floating.width,
        height: i.floating.height
    } : i.reference
      , x = await (s.getOffsetParent == null ? void 0 : s.getOffsetParent(l.floating))
      , N = await (s.isElement == null ? void 0 : s.isElement(x)) ? await (s.getScale == null ? void 0 : s.getScale(x)) || {
        x: 1,
        y: 1
    } : {
        x: 1,
        y: 1
    }
      , S = sl(s.convertOffsetParentRelativeRectToViewportRelativeRect ? await s.convertOffsetParentRelativeRectToViewportRelativeRect({
        elements: l,
        rect: p,
        offsetParent: x,
        strategy: c
    }) : p);
    return {
        top: (y.top - S.top + b.top) / N.y,
        bottom: (S.bottom - y.bottom + b.bottom) / N.y,
        left: (y.left - S.left + b.left) / N.x,
        right: (S.right - y.right + b.right) / N.x
    }
}
const u2 = e => ({
    name: "arrow",
    options: e,
    async fn(t) {
        const {x: n, y: r, placement: o, rects: s, platform: i, elements: l, middlewareData: c} = t
          , {element: u, padding: d=0} = Ln(e, t) || {};
        if (u == null)
            return {};
        const f = Ry(d)
          , g = {
            x: n,
            y: r
        }
          , h = Nf(o)
          , b = bf(h)
          , v = await i.getDimensions(u)
          , w = h === "y"
          , y = w ? "top" : "left"
          , p = w ? "bottom" : "right"
          , x = w ? "clientHeight" : "clientWidth"
          , N = s.reference[b] + s.reference[h] - g[h] - s.floating[b]
          , S = g[h] - s.reference[h]
          , k = await (i.getOffsetParent == null ? void 0 : i.getOffsetParent(u));
        let C = k ? k[x] : 0;
        (!C || !await (i.isElement == null ? void 0 : i.isElement(k))) && (C = l.floating[x] || s.floating[b]);
        const T = N / 2 - S / 2
          , D = C / 2 - v[b] / 2 - 1
          , R = br(f[y], D)
          , F = br(f[p], D)
          , A = R
          , W = C - v[b] - F
          , O = C / 2 - v[b] / 2 + T
          , V = qu(A, O, W)
          , $ = !c.arrow && ps(o) != null && O !== V && s.reference[b] / 2 - (O < A ? R : F) - v[b] / 2 < 0
          , M = $ ? O < A ? O - A : O - W : 0;
        return {
            [h]: g[h] + M,
            data: {
                [h]: V,
                centerOffset: O - V - M,
                ...$ && {
                    alignmentOffset: M
                }
            },
            reset: $
        }
    }
})
  , d2 = function(e) {
    return e === void 0 && (e = {}),
    {
        name: "flip",
        options: e,
        async fn(t) {
            var n, r;
            const {placement: o, middlewareData: s, rects: i, initialPlacement: l, platform: c, elements: u} = t
              , {mainAxis: d=!0, crossAxis: f=!0, fallbackPlacements: g, fallbackStrategy: h="bestFit", fallbackAxisSideDirection: b="none", flipAlignment: v=!0, ...w} = Ln(e, t);
            if ((n = s.arrow) != null && n.alignmentOffset)
                return {};
            const y = Fn(o)
              , p = mn(l)
              , x = Fn(l) === l
              , N = await (c.isRTL == null ? void 0 : c.isRTL(u.floating))
              , S = g || (x || !v ? [ol(l)] : r2(l))
              , k = b !== "none";
            !g && k && S.push(...i2(l, v, b, N));
            const C = [l, ...S]
              , T = await pa(t, w)
              , D = [];
            let R = ((r = s.flip) == null ? void 0 : r.overflows) || [];
            if (d && D.push(T[y]),
            f) {
                const O = n2(o, i, N);
                D.push(T[O[0]], T[O[1]])
            }
            if (R = [...R, {
                placement: o,
                overflows: D
            }],
            !D.every(O => O <= 0)) {
                var F, A;
                const O = (((F = s.flip) == null ? void 0 : F.index) || 0) + 1
                  , V = C[O];
                if (V && (!(f === "alignment" ? p !== mn(V) : !1) || R.every(j => j.overflows[0] > 0 && mn(j.placement) === p)))
                    return {
                        data: {
                            index: O,
                            overflows: R
                        },
                        reset: {
                            placement: V
                        }
                    };
                let $ = (A = R.filter(M => M.overflows[0] <= 0).sort( (M, j) => M.overflows[1] - j.overflows[1])[0]) == null ? void 0 : A.placement;
                if (!$)
                    switch (h) {
                    case "bestFit":
                        {
                            var W;
                            const M = (W = R.filter(j => {
                                if (k) {
                                    const E = mn(j.placement);
                                    return E === p || E === "y"
                                }
                                return !0
                            }
                            ).map(j => [j.placement, j.overflows.filter(E => E > 0).reduce( (E, L) => E + L, 0)]).sort( (j, E) => j[1] - E[1])[0]) == null ? void 0 : W[0];
                            M && ($ = M);
                            break
                        }
                    case "initialPlacement":
                        $ = l;
                        break
                    }
                if (o !== $)
                    return {
                        reset: {
                            placement: $
                        }
                    }
            }
            return {}
        }
    }
};
function Rh(e, t) {
    return {
        top: e.top - t.height,
        right: e.right - t.width,
        bottom: e.bottom - t.height,
        left: e.left - t.width
    }
}
function _h(e) {
    return Jj.some(t => e[t] >= 0)
}
const f2 = function(e) {
    return e === void 0 && (e = {}),
    {
        name: "hide",
        options: e,
        async fn(t) {
            const {rects: n} = t
              , {strategy: r="referenceHidden", ...o} = Ln(e, t);
            switch (r) {
            case "referenceHidden":
                {
                    const s = await pa(t, {
                        ...o,
                        elementContext: "reference"
                    })
                      , i = Rh(s, n.reference);
                    return {
                        data: {
                            referenceHiddenOffsets: i,
                            referenceHidden: _h(i)
                        }
                    }
                }
            case "escaped":
                {
                    const s = await pa(t, {
                        ...o,
                        altBoundary: !0
                    })
                      , i = Rh(s, n.floating);
                    return {
                        data: {
                            escapedOffsets: i,
                            escaped: _h(i)
                        }
                    }
                }
            default:
                return {}
            }
        }
    }
}
  , _y = new Set(["left", "top"]);
async function m2(e, t) {
    const {placement: n, platform: r, elements: o} = e
      , s = await (r.isRTL == null ? void 0 : r.isRTL(o.floating))
      , i = Fn(n)
      , l = ps(n)
      , c = mn(n) === "y"
      , u = _y.has(i) ? -1 : 1
      , d = s && c ? -1 : 1
      , f = Ln(t, e);
    let {mainAxis: g, crossAxis: h, alignmentAxis: b} = typeof f == "number" ? {
        mainAxis: f,
        crossAxis: 0,
        alignmentAxis: null
    } : {
        mainAxis: f.mainAxis || 0,
        crossAxis: f.crossAxis || 0,
        alignmentAxis: f.alignmentAxis
    };
    return l && typeof b == "number" && (h = l === "end" ? b * -1 : b),
    c ? {
        x: h * d,
        y: g * u
    } : {
        x: g * u,
        y: h * d
    }
}
const h2 = function(e) {
    return e === void 0 && (e = 0),
    {
        name: "offset",
        options: e,
        async fn(t) {
            var n, r;
            const {x: o, y: s, placement: i, middlewareData: l} = t
              , c = await m2(t, e);
            return i === ((n = l.offset) == null ? void 0 : n.placement) && (r = l.arrow) != null && r.alignmentOffset ? {} : {
                x: o + c.x,
                y: s + c.y,
                data: {
                    ...c,
                    placement: i
                }
            }
        }
    }
}
  , p2 = function(e) {
    return e === void 0 && (e = {}),
    {
        name: "shift",
        options: e,
        async fn(t) {
            const {x: n, y: r, placement: o} = t
              , {mainAxis: s=!0, crossAxis: i=!1, limiter: l={
                fn: w => {
                    let {x: y, y: p} = w;
                    return {
                        x: y,
                        y: p
                    }
                }
            }, ...c} = Ln(e, t)
              , u = {
                x: n,
                y: r
            }
              , d = await pa(t, c)
              , f = mn(Fn(o))
              , g = wf(f);
            let h = u[g]
              , b = u[f];
            if (s) {
                const w = g === "y" ? "top" : "left"
                  , y = g === "y" ? "bottom" : "right"
                  , p = h + d[w]
                  , x = h - d[y];
                h = qu(p, h, x)
            }
            if (i) {
                const w = f === "y" ? "top" : "left"
                  , y = f === "y" ? "bottom" : "right"
                  , p = b + d[w]
                  , x = b - d[y];
                b = qu(p, b, x)
            }
            const v = l.fn({
                ...t,
                [g]: h,
                [f]: b
            });
            return {
                ...v,
                data: {
                    x: v.x - n,
                    y: v.y - r,
                    enabled: {
                        [g]: s,
                        [f]: i
                    }
                }
            }
        }
    }
}
  , v2 = function(e) {
    return e === void 0 && (e = {}),
    {
        options: e,
        fn(t) {
            const {x: n, y: r, placement: o, rects: s, middlewareData: i} = t
              , {offset: l=0, mainAxis: c=!0, crossAxis: u=!0} = Ln(e, t)
              , d = {
                x: n,
                y: r
            }
              , f = mn(o)
              , g = wf(f);
            let h = d[g]
              , b = d[f];
            const v = Ln(l, t)
              , w = typeof v == "number" ? {
                mainAxis: v,
                crossAxis: 0
            } : {
                mainAxis: 0,
                crossAxis: 0,
                ...v
            };
            if (c) {
                const x = g === "y" ? "height" : "width"
                  , N = s.reference[g] - s.floating[x] + w.mainAxis
                  , S = s.reference[g] + s.reference[x] - w.mainAxis;
                h < N ? h = N : h > S && (h = S)
            }
            if (u) {
                var y, p;
                const x = g === "y" ? "width" : "height"
                  , N = _y.has(Fn(o))
                  , S = s.reference[f] - s.floating[x] + (N && ((y = i.offset) == null ? void 0 : y[f]) || 0) + (N ? 0 : w.crossAxis)
                  , k = s.reference[f] + s.reference[x] + (N ? 0 : ((p = i.offset) == null ? void 0 : p[f]) || 0) - (N ? w.crossAxis : 0);
                b < S ? b = S : b > k && (b = k)
            }
            return {
                [g]: h,
                [f]: b
            }
        }
    }
}
  , g2 = function(e) {
    return e === void 0 && (e = {}),
    {
        name: "size",
        options: e,
        async fn(t) {
            var n, r;
            const {placement: o, rects: s, platform: i, elements: l} = t
              , {apply: c= () => {}
            , ...u} = Ln(e, t)
              , d = await pa(t, u)
              , f = Fn(o)
              , g = ps(o)
              , h = mn(o) === "y"
              , {width: b, height: v} = s.floating;
            let w, y;
            f === "top" || f === "bottom" ? (w = f,
            y = g === (await (i.isRTL == null ? void 0 : i.isRTL(l.floating)) ? "start" : "end") ? "left" : "right") : (y = f,
            w = g === "end" ? "top" : "bottom");
            const p = v - d.top - d.bottom
              , x = b - d.left - d.right
              , N = br(v - d[w], p)
              , S = br(b - d[y], x)
              , k = !t.middlewareData.shift;
            let C = N
              , T = S;
            if ((n = t.middlewareData.shift) != null && n.enabled.x && (T = x),
            (r = t.middlewareData.shift) != null && r.enabled.y && (C = p),
            k && !g) {
                const R = vt(d.left, 0)
                  , F = vt(d.right, 0)
                  , A = vt(d.top, 0)
                  , W = vt(d.bottom, 0);
                h ? T = b - 2 * (R !== 0 || F !== 0 ? R + F : vt(d.left, d.right)) : C = v - 2 * (A !== 0 || W !== 0 ? A + W : vt(d.top, d.bottom))
            }
            await c({
                ...t,
                availableWidth: T,
                availableHeight: C
            });
            const D = await i.getDimensions(l.floating);
            return b !== D.width || v !== D.height ? {
                reset: {
                    rects: !0
                }
            } : {}
        }
    }
};
function Al() {
    return typeof window < "u"
}
function vs(e) {
    return Dy(e) ? (e.nodeName || "").toLowerCase() : "#document"
}
function xt(e) {
    var t;
    return (e == null || (t = e.ownerDocument) == null ? void 0 : t.defaultView) || window
}
function bn(e) {
    var t;
    return (t = (Dy(e) ? e.ownerDocument : e.document) || window.document) == null ? void 0 : t.documentElement
}
function Dy(e) {
    return Al() ? e instanceof Node || e instanceof xt(e).Node : !1
}
function en(e) {
    return Al() ? e instanceof Element || e instanceof xt(e).Element : !1
}
function xn(e) {
    return Al() ? e instanceof HTMLElement || e instanceof xt(e).HTMLElement : !1
}
function Dh(e) {
    return !Al() || typeof ShadowRoot > "u" ? !1 : e instanceof ShadowRoot || e instanceof xt(e).ShadowRoot
}
const y2 = new Set(["inline", "contents"]);
function _a(e) {
    const {overflow: t, overflowX: n, overflowY: r, display: o} = tn(e);
    return /auto|scroll|overlay|hidden|clip/.test(t + r + n) && !y2.has(o)
}
const x2 = new Set(["table", "td", "th"]);
function w2(e) {
    return x2.has(vs(e))
}
const b2 = [":popover-open", ":modal"];
function Il(e) {
    return b2.some(t => {
        try {
            return e.matches(t)
        } catch {
            return !1
        }
    }
    )
}
const N2 = ["transform", "translate", "scale", "rotate", "perspective"]
  , S2 = ["transform", "translate", "scale", "rotate", "perspective", "filter"]
  , j2 = ["paint", "layout", "strict", "content"];
function Sf(e) {
    const t = jf()
      , n = en(e) ? tn(e) : e;
    return N2.some(r => n[r] ? n[r] !== "none" : !1) || (n.containerType ? n.containerType !== "normal" : !1) || !t && (n.backdropFilter ? n.backdropFilter !== "none" : !1) || !t && (n.filter ? n.filter !== "none" : !1) || S2.some(r => (n.willChange || "").includes(r)) || j2.some(r => (n.contain || "").includes(r))
}
function C2(e) {
    let t = Nr(e);
    for (; xn(t) && !is(t); ) {
        if (Sf(t))
            return t;
        if (Il(t))
            return null;
        t = Nr(t)
    }
    return null
}
function jf() {
    return typeof CSS > "u" || !CSS.supports ? !1 : CSS.supports("-webkit-backdrop-filter", "none")
}
const k2 = new Set(["html", "body", "#document"]);
function is(e) {
    return k2.has(vs(e))
}
function tn(e) {
    return xt(e).getComputedStyle(e)
}
function Ll(e) {
    return en(e) ? {
        scrollLeft: e.scrollLeft,
        scrollTop: e.scrollTop
    } : {
        scrollLeft: e.scrollX,
        scrollTop: e.scrollY
    }
}
function Nr(e) {
    if (vs(e) === "html")
        return e;
    const t = e.assignedSlot || e.parentNode || Dh(e) && e.host || bn(e);
    return Dh(t) ? t.host : t
}
function Oy(e) {
    const t = Nr(e);
    return is(t) ? e.ownerDocument ? e.ownerDocument.body : e.body : xn(t) && _a(t) ? t : Oy(t)
}
function va(e, t, n) {
    var r;
    t === void 0 && (t = []),
    n === void 0 && (n = !0);
    const o = Oy(e)
      , s = o === ((r = e.ownerDocument) == null ? void 0 : r.body)
      , i = xt(o);
    if (s) {
        const l = Ju(i);
        return t.concat(i, i.visualViewport || [], _a(o) ? o : [], l && n ? va(l) : [])
    }
    return t.concat(o, va(o, [], n))
}
function Ju(e) {
    return e.parent && Object.getPrototypeOf(e.parent) ? e.frameElement : null
}
function Ay(e) {
    const t = tn(e);
    let n = parseFloat(t.width) || 0
      , r = parseFloat(t.height) || 0;
    const o = xn(e)
      , s = o ? e.offsetWidth : n
      , i = o ? e.offsetHeight : r
      , l = rl(n) !== s || rl(r) !== i;
    return l && (n = s,
    r = i),
    {
        width: n,
        height: r,
        $: l
    }
}
function Cf(e) {
    return en(e) ? e : e.contextElement
}
function $o(e) {
    const t = Cf(e);
    if (!xn(t))
        return gn(1);
    const n = t.getBoundingClientRect()
      , {width: r, height: o, $: s} = Ay(t);
    let i = (s ? rl(n.width) : n.width) / r
      , l = (s ? rl(n.height) : n.height) / o;
    return (!i || !Number.isFinite(i)) && (i = 1),
    (!l || !Number.isFinite(l)) && (l = 1),
    {
        x: i,
        y: l
    }
}
const E2 = gn(0);
function Iy(e) {
    const t = xt(e);
    return !jf() || !t.visualViewport ? E2 : {
        x: t.visualViewport.offsetLeft,
        y: t.visualViewport.offsetTop
    }
}
function P2(e, t, n) {
    return t === void 0 && (t = !1),
    !n || t && n !== xt(e) ? !1 : t
}
function Zr(e, t, n, r) {
    t === void 0 && (t = !1),
    n === void 0 && (n = !1);
    const o = e.getBoundingClientRect()
      , s = Cf(e);
    let i = gn(1);
    t && (r ? en(r) && (i = $o(r)) : i = $o(e));
    const l = P2(s, n, r) ? Iy(s) : gn(0);
    let c = (o.left + l.x) / i.x
      , u = (o.top + l.y) / i.y
      , d = o.width / i.x
      , f = o.height / i.y;
    if (s) {
        const g = xt(s)
          , h = r && en(r) ? xt(r) : r;
        let b = g
          , v = Ju(b);
        for (; v && r && h !== b; ) {
            const w = $o(v)
              , y = v.getBoundingClientRect()
              , p = tn(v)
              , x = y.left + (v.clientLeft + parseFloat(p.paddingLeft)) * w.x
              , N = y.top + (v.clientTop + parseFloat(p.paddingTop)) * w.y;
            c *= w.x,
            u *= w.y,
            d *= w.x,
            f *= w.y,
            c += x,
            u += N,
            b = xt(v),
            v = Ju(b)
        }
    }
    return sl({
        width: d,
        height: f,
        x: c,
        y: u
    })
}
function kf(e, t) {
    const n = Ll(e).scrollLeft;
    return t ? t.left + n : Zr(bn(e)).left + n
}
function Ly(e, t, n) {
    n === void 0 && (n = !1);
    const r = e.getBoundingClientRect()
      , o = r.left + t.scrollLeft - (n ? 0 : kf(e, r))
      , s = r.top + t.scrollTop;
    return {
        x: o,
        y: s
    }
}
function T2(e) {
    let {elements: t, rect: n, offsetParent: r, strategy: o} = e;
    const s = o === "fixed"
      , i = bn(r)
      , l = t ? Il(t.floating) : !1;
    if (r === i || l && s)
        return n;
    let c = {
        scrollLeft: 0,
        scrollTop: 0
    }
      , u = gn(1);
    const d = gn(0)
      , f = xn(r);
    if ((f || !f && !s) && ((vs(r) !== "body" || _a(i)) && (c = Ll(r)),
    xn(r))) {
        const h = Zr(r);
        u = $o(r),
        d.x = h.x + r.clientLeft,
        d.y = h.y + r.clientTop
    }
    const g = i && !f && !s ? Ly(i, c, !0) : gn(0);
    return {
        width: n.width * u.x,
        height: n.height * u.y,
        x: n.x * u.x - c.scrollLeft * u.x + d.x + g.x,
        y: n.y * u.y - c.scrollTop * u.y + d.y + g.y
    }
}
function M2(e) {
    return Array.from(e.getClientRects())
}
function R2(e) {
    const t = bn(e)
      , n = Ll(e)
      , r = e.ownerDocument.body
      , o = vt(t.scrollWidth, t.clientWidth, r.scrollWidth, r.clientWidth)
      , s = vt(t.scrollHeight, t.clientHeight, r.scrollHeight, r.clientHeight);
    let i = -n.scrollLeft + kf(e);
    const l = -n.scrollTop;
    return tn(r).direction === "rtl" && (i += vt(t.clientWidth, r.clientWidth) - o),
    {
        width: o,
        height: s,
        x: i,
        y: l
    }
}
function _2(e, t) {
    const n = xt(e)
      , r = bn(e)
      , o = n.visualViewport;
    let s = r.clientWidth
      , i = r.clientHeight
      , l = 0
      , c = 0;
    if (o) {
        s = o.width,
        i = o.height;
        const u = jf();
        (!u || u && t === "fixed") && (l = o.offsetLeft,
        c = o.offsetTop)
    }
    return {
        width: s,
        height: i,
        x: l,
        y: c
    }
}
const D2 = new Set(["absolute", "fixed"]);
function O2(e, t) {
    const n = Zr(e, !0, t === "fixed")
      , r = n.top + e.clientTop
      , o = n.left + e.clientLeft
      , s = xn(e) ? $o(e) : gn(1)
      , i = e.clientWidth * s.x
      , l = e.clientHeight * s.y
      , c = o * s.x
      , u = r * s.y;
    return {
        width: i,
        height: l,
        x: c,
        y: u
    }
}
function Oh(e, t, n) {
    let r;
    if (t === "viewport")
        r = _2(e, n);
    else if (t === "document")
        r = R2(bn(e));
    else if (en(t))
        r = O2(t, n);
    else {
        const o = Iy(e);
        r = {
            x: t.x - o.x,
            y: t.y - o.y,
            width: t.width,
            height: t.height
        }
    }
    return sl(r)
}
function Fy(e, t) {
    const n = Nr(e);
    return n === t || !en(n) || is(n) ? !1 : tn(n).position === "fixed" || Fy(n, t)
}
function A2(e, t) {
    const n = t.get(e);
    if (n)
        return n;
    let r = va(e, [], !1).filter(l => en(l) && vs(l) !== "body")
      , o = null;
    const s = tn(e).position === "fixed";
    let i = s ? Nr(e) : e;
    for (; en(i) && !is(i); ) {
        const l = tn(i)
          , c = Sf(i);
        !c && l.position === "fixed" && (o = null),
        (s ? !c && !o : !c && l.position === "static" && !!o && D2.has(o.position) || _a(i) && !c && Fy(e, i)) ? r = r.filter(d => d !== i) : o = l,
        i = Nr(i)
    }
    return t.set(e, r),
    r
}
function I2(e) {
    let {element: t, boundary: n, rootBoundary: r, strategy: o} = e;
    const i = [...n === "clippingAncestors" ? Il(t) ? [] : A2(t, this._c) : [].concat(n), r]
      , l = i[0]
      , c = i.reduce( (u, d) => {
        const f = Oh(t, d, o);
        return u.top = vt(f.top, u.top),
        u.right = br(f.right, u.right),
        u.bottom = br(f.bottom, u.bottom),
        u.left = vt(f.left, u.left),
        u
    }
    , Oh(t, l, o));
    return {
        width: c.right - c.left,
        height: c.bottom - c.top,
        x: c.left,
        y: c.top
    }
}
function L2(e) {
    const {width: t, height: n} = Ay(e);
    return {
        width: t,
        height: n
    }
}
function F2(e, t, n) {
    const r = xn(t)
      , o = bn(t)
      , s = n === "fixed"
      , i = Zr(e, !0, s, t);
    let l = {
        scrollLeft: 0,
        scrollTop: 0
    };
    const c = gn(0);
    function u() {
        c.x = kf(o)
    }
    if (r || !r && !s)
        if ((vs(t) !== "body" || _a(o)) && (l = Ll(t)),
        r) {
            const h = Zr(t, !0, s, t);
            c.x = h.x + t.clientLeft,
            c.y = h.y + t.clientTop
        } else
            o && u();
    s && !r && o && u();
    const d = o && !r && !s ? Ly(o, l) : gn(0)
      , f = i.left + l.scrollLeft - c.x - d.x
      , g = i.top + l.scrollTop - c.y - d.y;
    return {
        x: f,
        y: g,
        width: i.width,
        height: i.height
    }
}
function Mc(e) {
    return tn(e).position === "static"
}
function Ah(e, t) {
    if (!xn(e) || tn(e).position === "fixed")
        return null;
    if (t)
        return t(e);
    let n = e.offsetParent;
    return bn(e) === n && (n = n.ownerDocument.body),
    n
}
function zy(e, t) {
    const n = xt(e);
    if (Il(e))
        return n;
    if (!xn(e)) {
        let o = Nr(e);
        for (; o && !is(o); ) {
            if (en(o) && !Mc(o))
                return o;
            o = Nr(o)
        }
        return n
    }
    let r = Ah(e, t);
    for (; r && w2(r) && Mc(r); )
        r = Ah(r, t);
    return r && is(r) && Mc(r) && !Sf(r) ? n : r || C2(e) || n
}
const z2 = async function(e) {
    const t = this.getOffsetParent || zy
      , n = this.getDimensions
      , r = await n(e.floating);
    return {
        reference: F2(e.reference, await t(e.floating), e.strategy),
        floating: {
            x: 0,
            y: 0,
            width: r.width,
            height: r.height
        }
    }
};
function $2(e) {
    return tn(e).direction === "rtl"
}
const B2 = {
    convertOffsetParentRelativeRectToViewportRelativeRect: T2,
    getDocumentElement: bn,
    getClippingRect: I2,
    getOffsetParent: zy,
    getElementRects: z2,
    getClientRects: M2,
    getDimensions: L2,
    getScale: $o,
    isElement: en,
    isRTL: $2
};
function $y(e, t) {
    return e.x === t.x && e.y === t.y && e.width === t.width && e.height === t.height
}
function W2(e, t) {
    let n = null, r;
    const o = bn(e);
    function s() {
        var l;
        clearTimeout(r),
        (l = n) == null || l.disconnect(),
        n = null
    }
    function i(l, c) {
        l === void 0 && (l = !1),
        c === void 0 && (c = 1),
        s();
        const u = e.getBoundingClientRect()
          , {left: d, top: f, width: g, height: h} = u;
        if (l || t(),
        !g || !h)
            return;
        const b = ii(f)
          , v = ii(o.clientWidth - (d + g))
          , w = ii(o.clientHeight - (f + h))
          , y = ii(d)
          , x = {
            rootMargin: -b + "px " + -v + "px " + -w + "px " + -y + "px",
            threshold: vt(0, br(1, c)) || 1
        };
        let N = !0;
        function S(k) {
            const C = k[0].intersectionRatio;
            if (C !== c) {
                if (!N)
                    return i();
                C ? i(!1, C) : r = setTimeout( () => {
                    i(!1, 1e-7)
                }
                , 1e3)
            }
            C === 1 && !$y(u, e.getBoundingClientRect()) && i(),
            N = !1
        }
        try {
            n = new IntersectionObserver(S,{
                ...x,
                root: o.ownerDocument
            })
        } catch {
            n = new IntersectionObserver(S,x)
        }
        n.observe(e)
    }
    return i(!0),
    s
}
function H2(e, t, n, r) {
    r === void 0 && (r = {});
    const {ancestorScroll: o=!0, ancestorResize: s=!0, elementResize: i=typeof ResizeObserver == "function", layoutShift: l=typeof IntersectionObserver == "function", animationFrame: c=!1} = r
      , u = Cf(e)
      , d = o || s ? [...u ? va(u) : [], ...va(t)] : [];
    d.forEach(y => {
        o && y.addEventListener("scroll", n, {
            passive: !0
        }),
        s && y.addEventListener("resize", n)
    }
    );
    const f = u && l ? W2(u, n) : null;
    let g = -1
      , h = null;
    i && (h = new ResizeObserver(y => {
        let[p] = y;
        p && p.target === u && h && (h.unobserve(t),
        cancelAnimationFrame(g),
        g = requestAnimationFrame( () => {
            var x;
            (x = h) == null || x.observe(t)
        }
        )),
        n()
    }
    ),
    u && !c && h.observe(u),
    h.observe(t));
    let b, v = c ? Zr(e) : null;
    c && w();
    function w() {
        const y = Zr(e);
        v && !$y(v, y) && n(),
        v = y,
        b = requestAnimationFrame(w)
    }
    return n(),
    () => {
        var y;
        d.forEach(p => {
            o && p.removeEventListener("scroll", n),
            s && p.removeEventListener("resize", n)
        }
        ),
        f == null || f(),
        (y = h) == null || y.disconnect(),
        h = null,
        c && cancelAnimationFrame(b)
    }
}
const V2 = h2
  , U2 = p2
  , Y2 = d2
  , K2 = g2
  , Q2 = f2
  , Ih = u2
  , G2 = v2
  , q2 = (e, t, n) => {
    const r = new Map
      , o = {
        platform: B2,
        ...n
    }
      , s = {
        ...o.platform,
        _c: r
    };
    return c2(e, t, {
        ...o,
        platform: s
    })
}
;
var X2 = typeof document < "u"
  , J2 = function() {}
  , Ei = X2 ? m.useLayoutEffect : J2;
function al(e, t) {
    if (e === t)
        return !0;
    if (typeof e != typeof t)
        return !1;
    if (typeof e == "function" && e.toString() === t.toString())
        return !0;
    let n, r, o;
    if (e && t && typeof e == "object") {
        if (Array.isArray(e)) {
            if (n = e.length,
            n !== t.length)
                return !1;
            for (r = n; r-- !== 0; )
                if (!al(e[r], t[r]))
                    return !1;
            return !0
        }
        if (o = Object.keys(e),
        n = o.length,
        n !== Object.keys(t).length)
            return !1;
        for (r = n; r-- !== 0; )
            if (!{}.hasOwnProperty.call(t, o[r]))
                return !1;
        for (r = n; r-- !== 0; ) {
            const s = o[r];
            if (!(s === "_owner" && e.$$typeof) && !al(e[s], t[s]))
                return !1
        }
        return !0
    }
    return e !== e && t !== t
}
function By(e) {
    return typeof window > "u" ? 1 : (e.ownerDocument.defaultView || window).devicePixelRatio || 1
}
function Lh(e, t) {
    const n = By(e);
    return Math.round(t * n) / n
}
function Rc(e) {
    const t = m.useRef(e);
    return Ei( () => {
        t.current = e
    }
    ),
    t
}
function Z2(e) {
    e === void 0 && (e = {});
    const {placement: t="bottom", strategy: n="absolute", middleware: r=[], platform: o, elements: {reference: s, floating: i}={}, transform: l=!0, whileElementsMounted: c, open: u} = e
      , [d,f] = m.useState({
        x: 0,
        y: 0,
        strategy: n,
        placement: t,
        middlewareData: {},
        isPositioned: !1
    })
      , [g,h] = m.useState(r);
    al(g, r) || h(r);
    const [b,v] = m.useState(null)
      , [w,y] = m.useState(null)
      , p = m.useCallback(j => {
        j !== k.current && (k.current = j,
        v(j))
    }
    , [])
      , x = m.useCallback(j => {
        j !== C.current && (C.current = j,
        y(j))
    }
    , [])
      , N = s || b
      , S = i || w
      , k = m.useRef(null)
      , C = m.useRef(null)
      , T = m.useRef(d)
      , D = c != null
      , R = Rc(c)
      , F = Rc(o)
      , A = Rc(u)
      , W = m.useCallback( () => {
        if (!k.current || !C.current)
            return;
        const j = {
            placement: t,
            strategy: n,
            middleware: g
        };
        F.current && (j.platform = F.current),
        q2(k.current, C.current, j).then(E => {
            const L = {
                ...E,
                isPositioned: A.current !== !1
            };
            O.current && !al(T.current, L) && (T.current = L,
            ao.flushSync( () => {
                f(L)
            }
            ))
        }
        )
    }
    , [g, t, n, F, A]);
    Ei( () => {
        u === !1 && T.current.isPositioned && (T.current.isPositioned = !1,
        f(j => ({
            ...j,
            isPositioned: !1
        })))
    }
    , [u]);
    const O = m.useRef(!1);
    Ei( () => (O.current = !0,
    () => {
        O.current = !1
    }
    ), []),
    Ei( () => {
        if (N && (k.current = N),
        S && (C.current = S),
        N && S) {
            if (R.current)
                return R.current(N, S, W);
            W()
        }
    }
    , [N, S, W, R, D]);
    const V = m.useMemo( () => ({
        reference: k,
        floating: C,
        setReference: p,
        setFloating: x
    }), [p, x])
      , $ = m.useMemo( () => ({
        reference: N,
        floating: S
    }), [N, S])
      , M = m.useMemo( () => {
        const j = {
            position: n,
            left: 0,
            top: 0
        };
        if (!$.floating)
            return j;
        const E = Lh($.floating, d.x)
          , L = Lh($.floating, d.y);
        return l ? {
            ...j,
            transform: "translate(" + E + "px, " + L + "px)",
            ...By($.floating) >= 1.5 && {
                willChange: "transform"
            }
        } : {
            position: n,
            left: E,
            top: L
        }
    }
    , [n, l, $.floating, d.x, d.y]);
    return m.useMemo( () => ({
        ...d,
        update: W,
        refs: V,
        elements: $,
        floatingStyles: M
    }), [d, W, V, $, M])
}
const eC = e => {
    function t(n) {
        return {}.hasOwnProperty.call(n, "current")
    }
    return {
        name: "arrow",
        options: e,
        fn(n) {
            const {element: r, padding: o} = typeof e == "function" ? e(n) : e;
            return r && t(r) ? r.current != null ? Ih({
                element: r.current,
                padding: o
            }).fn(n) : {} : r ? Ih({
                element: r,
                padding: o
            }).fn(n) : {}
        }
    }
}
  , tC = (e, t) => ({
    ...V2(e),
    options: [e, t]
})
  , nC = (e, t) => ({
    ...U2(e),
    options: [e, t]
})
  , rC = (e, t) => ({
    ...G2(e),
    options: [e, t]
})
  , oC = (e, t) => ({
    ...Y2(e),
    options: [e, t]
})
  , sC = (e, t) => ({
    ...K2(e),
    options: [e, t]
})
  , aC = (e, t) => ({
    ...Q2(e),
    options: [e, t]
})
  , iC = (e, t) => ({
    ...eC(e),
    options: [e, t]
});
var lC = "Arrow"
  , Wy = m.forwardRef( (e, t) => {
    const {children: n, width: r=10, height: o=5, ...s} = e;
    return a.jsx(te.svg, {
        ...s,
        ref: t,
        width: r,
        height: o,
        viewBox: "0 0 30 10",
        preserveAspectRatio: "none",
        children: e.asChild ? n : a.jsx("polygon", {
            points: "0,0 30,0 15,10"
        })
    })
}
);
Wy.displayName = lC;
var cC = Wy;
function Hy(e) {
    const [t,n] = m.useState(void 0);
    return Ue( () => {
        if (e) {
            n({
                width: e.offsetWidth,
                height: e.offsetHeight
            });
            const r = new ResizeObserver(o => {
                if (!Array.isArray(o) || !o.length)
                    return;
                const s = o[0];
                let i, l;
                if ("borderBoxSize"in s) {
                    const c = s.borderBoxSize
                      , u = Array.isArray(c) ? c[0] : c;
                    i = u.inlineSize,
                    l = u.blockSize
                } else
                    i = e.offsetWidth,
                    l = e.offsetHeight;
                n({
                    width: i,
                    height: l
                })
            }
            );
            return r.observe(e, {
                box: "border-box"
            }),
            () => r.unobserve(e)
        } else
            n(void 0)
    }
    , [e]),
    t
}
var Ef = "Popper"
  , [Vy,Fl] = io(Ef)
  , [uC,Uy] = Vy(Ef)
  , Yy = e => {
    const {__scopePopper: t, children: n} = e
      , [r,o] = m.useState(null);
    return a.jsx(uC, {
        scope: t,
        anchor: r,
        onAnchorChange: o,
        children: n
    })
}
;
Yy.displayName = Ef;
var Ky = "PopperAnchor"
  , Qy = m.forwardRef( (e, t) => {
    const {__scopePopper: n, virtualRef: r, ...o} = e
      , s = Uy(Ky, n)
      , i = m.useRef(null)
      , l = fe(t, i);
    return m.useEffect( () => {
        s.onAnchorChange((r == null ? void 0 : r.current) || i.current)
    }
    ),
    r ? null : a.jsx(te.div, {
        ...o,
        ref: l
    })
}
);
Qy.displayName = Ky;
var Pf = "PopperContent"
  , [dC,fC] = Vy(Pf)
  , Gy = m.forwardRef( (e, t) => {
    var z, me, Re, de, oe, ce;
    const {__scopePopper: n, side: r="bottom", sideOffset: o=0, align: s="center", alignOffset: i=0, arrowPadding: l=0, avoidCollisions: c=!0, collisionBoundary: u=[], collisionPadding: d=0, sticky: f="partial", hideWhenDetached: g=!1, updatePositionStrategy: h="optimized", onPlaced: b, ...v} = e
      , w = Uy(Pf, n)
      , [y,p] = m.useState(null)
      , x = fe(t, Ye => p(Ye))
      , [N,S] = m.useState(null)
      , k = Hy(N)
      , C = (k == null ? void 0 : k.width) ?? 0
      , T = (k == null ? void 0 : k.height) ?? 0
      , D = r + (s !== "center" ? "-" + s : "")
      , R = typeof d == "number" ? d : {
        top: 0,
        right: 0,
        bottom: 0,
        left: 0,
        ...d
    }
      , F = Array.isArray(u) ? u : [u]
      , A = F.length > 0
      , W = {
        padding: R,
        boundary: F.filter(hC),
        altBoundary: A
    }
      , {refs: O, floatingStyles: V, placement: $, isPositioned: M, middlewareData: j} = Z2({
        strategy: "fixed",
        placement: D,
        whileElementsMounted: (...Ye) => H2(...Ye, {
            animationFrame: h === "always"
        }),
        elements: {
            reference: w.anchor
        },
        middleware: [tC({
            mainAxis: o + T,
            alignmentAxis: i
        }), c && nC({
            mainAxis: !0,
            crossAxis: !1,
            limiter: f === "partial" ? rC() : void 0,
            ...W
        }), c && oC({
            ...W
        }), sC({
            ...W,
            apply: ({elements: Ye, rects: jt, availableWidth: Tr, availableHeight: $n}) => {
                const {width: Mr, height: bs} = jt.reference
                  , uo = Ye.floating.style;
                uo.setProperty("--radix-popper-available-width", `${Tr}px`),
                uo.setProperty("--radix-popper-available-height", `${$n}px`),
                uo.setProperty("--radix-popper-anchor-width", `${Mr}px`),
                uo.setProperty("--radix-popper-anchor-height", `${bs}px`)
            }
        }), N && iC({
            element: N,
            padding: l
        }), pC({
            arrowWidth: C,
            arrowHeight: T
        }), g && aC({
            strategy: "referenceHidden",
            ...W
        })]
    })
      , [E,L] = Jy($)
      , U = Zt(b);
    Ue( () => {
        M && (U == null || U())
    }
    , [M, U]);
    const H = (z = j.arrow) == null ? void 0 : z.x
      , J = (me = j.arrow) == null ? void 0 : me.y
      , G = ((Re = j.arrow) == null ? void 0 : Re.centerOffset) !== 0
      , [xe,Me] = m.useState();
    return Ue( () => {
        y && Me(window.getComputedStyle(y).zIndex)
    }
    , [y]),
    a.jsx("div", {
        ref: O.setFloating,
        "data-radix-popper-content-wrapper": "",
        style: {
            ...V,
            transform: M ? V.transform : "translate(0, -200%)",
            minWidth: "max-content",
            zIndex: xe,
            "--radix-popper-transform-origin": [(de = j.transformOrigin) == null ? void 0 : de.x, (oe = j.transformOrigin) == null ? void 0 : oe.y].join(" "),
            ...((ce = j.hide) == null ? void 0 : ce.referenceHidden) && {
                visibility: "hidden",
                pointerEvents: "none"
            }
        },
        dir: e.dir,
        children: a.jsx(dC, {
            scope: n,
            placedSide: E,
            onArrowChange: S,
            arrowX: H,
            arrowY: J,
            shouldHideArrow: G,
            children: a.jsx(te.div, {
                "data-side": E,
                "data-align": L,
                ...v,
                ref: x,
                style: {
                    ...v.style,
                    animation: M ? void 0 : "none"
                }
            })
        })
    })
}
);
Gy.displayName = Pf;
var qy = "PopperArrow"
  , mC = {
    top: "bottom",
    right: "left",
    bottom: "top",
    left: "right"
}
  , Xy = m.forwardRef(function(t, n) {
    const {__scopePopper: r, ...o} = t
      , s = fC(qy, r)
      , i = mC[s.placedSide];
    return a.jsx("span", {
        ref: s.onArrowChange,
        style: {
            position: "absolute",
            left: s.arrowX,
            top: s.arrowY,
            [i]: 0,
            transformOrigin: {
                top: "",
                right: "0 0",
                bottom: "center 0",
                left: "100% 0"
            }[s.placedSide],
            transform: {
                top: "translateY(100%)",
                right: "translateY(50%) rotate(90deg) translateX(-50%)",
                bottom: "rotate(180deg)",
                left: "translateY(50%) rotate(-90deg) translateX(50%)"
            }[s.placedSide],
            visibility: s.shouldHideArrow ? "hidden" : void 0
        },
        children: a.jsx(cC, {
            ...o,
            ref: n,
            style: {
                ...o.style,
                display: "block"
            }
        })
    })
});
Xy.displayName = qy;
function hC(e) {
    return e !== null
}
var pC = e => ({
    name: "transformOrigin",
    options: e,
    fn(t) {
        var w, y, p;
        const {placement: n, rects: r, middlewareData: o} = t
          , i = ((w = o.arrow) == null ? void 0 : w.centerOffset) !== 0
          , l = i ? 0 : e.arrowWidth
          , c = i ? 0 : e.arrowHeight
          , [u,d] = Jy(n)
          , f = {
            start: "0%",
            center: "50%",
            end: "100%"
        }[d]
          , g = (((y = o.arrow) == null ? void 0 : y.x) ?? 0) + l / 2
          , h = (((p = o.arrow) == null ? void 0 : p.y) ?? 0) + c / 2;
        let b = ""
          , v = "";
        return u === "bottom" ? (b = i ? f : `${g}px`,
        v = `${-c}px`) : u === "top" ? (b = i ? f : `${g}px`,
        v = `${r.floating.height + c}px`) : u === "right" ? (b = `${-c}px`,
        v = i ? f : `${h}px`) : u === "left" && (b = `${r.floating.width + c}px`,
        v = i ? f : `${h}px`),
        {
            data: {
                x: b,
                y: v
            }
        }
    }
});
function Jy(e) {
    const [t,n="center"] = e.split("-");
    return [t, n]
}
var vC = Yy
  , Zy = Qy
  , ex = Gy
  , tx = Xy
  , [zl,SR] = io("Tooltip", [Fl])
  , Tf = Fl()
  , nx = "TooltipProvider"
  , gC = 700
  , Fh = "tooltip.open"
  , [yC,rx] = zl(nx)
  , ox = e => {
    const {__scopeTooltip: t, delayDuration: n=gC, skipDelayDuration: r=300, disableHoverableContent: o=!1, children: s} = e
      , i = m.useRef(!0)
      , l = m.useRef(!1)
      , c = m.useRef(0);
    return m.useEffect( () => {
        const u = c.current;
        return () => window.clearTimeout(u)
    }
    , []),
    a.jsx(yC, {
        scope: t,
        isOpenDelayedRef: i,
        delayDuration: n,
        onOpen: m.useCallback( () => {
            window.clearTimeout(c.current),
            i.current = !1
        }
        , []),
        onClose: m.useCallback( () => {
            window.clearTimeout(c.current),
            c.current = window.setTimeout( () => i.current = !0, r)
        }
        , [r]),
        isPointerInTransitRef: l,
        onPointerInTransitChange: m.useCallback(u => {
            l.current = u
        }
        , []),
        disableHoverableContent: o,
        children: s
    })
}
;
ox.displayName = nx;
var sx = "Tooltip"
  , [jR,$l] = zl(sx)
  , Zu = "TooltipTrigger"
  , xC = m.forwardRef( (e, t) => {
    const {__scopeTooltip: n, ...r} = e
      , o = $l(Zu, n)
      , s = rx(Zu, n)
      , i = Tf(n)
      , l = m.useRef(null)
      , c = fe(t, l, o.onTriggerChange)
      , u = m.useRef(!1)
      , d = m.useRef(!1)
      , f = m.useCallback( () => u.current = !1, []);
    return m.useEffect( () => () => document.removeEventListener("pointerup", f), [f]),
    a.jsx(Zy, {
        asChild: !0,
        ...i,
        children: a.jsx(te.button, {
            "aria-describedby": o.open ? o.contentId : void 0,
            "data-state": o.stateAttribute,
            ...r,
            ref: c,
            onPointerMove: Q(e.onPointerMove, g => {
                g.pointerType !== "touch" && !d.current && !s.isPointerInTransitRef.current && (o.onTriggerEnter(),
                d.current = !0)
            }
            ),
            onPointerLeave: Q(e.onPointerLeave, () => {
                o.onTriggerLeave(),
                d.current = !1
            }
            ),
            onPointerDown: Q(e.onPointerDown, () => {
                o.open && o.onClose(),
                u.current = !0,
                document.addEventListener("pointerup", f, {
                    once: !0
                })
            }
            ),
            onFocus: Q(e.onFocus, () => {
                u.current || o.onOpen()
            }
            ),
            onBlur: Q(e.onBlur, o.onClose),
            onClick: Q(e.onClick, o.onClose)
        })
    })
}
);
xC.displayName = Zu;
var wC = "TooltipPortal"
  , [CR,bC] = zl(wC, {
    forceMount: void 0
})
  , ls = "TooltipContent"
  , ax = m.forwardRef( (e, t) => {
    const n = bC(ls, e.__scopeTooltip)
      , {forceMount: r=n.forceMount, side: o="top", ...s} = e
      , i = $l(ls, e.__scopeTooltip);
    return a.jsx(ms, {
        present: r || i.open,
        children: i.disableHoverableContent ? a.jsx(ix, {
            side: o,
            ...s,
            ref: t
        }) : a.jsx(NC, {
            side: o,
            ...s,
            ref: t
        })
    })
}
)
  , NC = m.forwardRef( (e, t) => {
    const n = $l(ls, e.__scopeTooltip)
      , r = rx(ls, e.__scopeTooltip)
      , o = m.useRef(null)
      , s = fe(t, o)
      , [i,l] = m.useState(null)
      , {trigger: c, onClose: u} = n
      , d = o.current
      , {onPointerInTransitChange: f} = r
      , g = m.useCallback( () => {
        l(null),
        f(!1)
    }
    , [f])
      , h = m.useCallback( (b, v) => {
        const w = b.currentTarget
          , y = {
            x: b.clientX,
            y: b.clientY
        }
          , p = EC(y, w.getBoundingClientRect())
          , x = PC(y, p)
          , N = TC(v.getBoundingClientRect())
          , S = RC([...x, ...N]);
        l(S),
        f(!0)
    }
    , [f]);
    return m.useEffect( () => () => g(), [g]),
    m.useEffect( () => {
        if (c && d) {
            const b = w => h(w, d)
              , v = w => h(w, c);
            return c.addEventListener("pointerleave", b),
            d.addEventListener("pointerleave", v),
            () => {
                c.removeEventListener("pointerleave", b),
                d.removeEventListener("pointerleave", v)
            }
        }
    }
    , [c, d, h, g]),
    m.useEffect( () => {
        if (i) {
            const b = v => {
                const w = v.target
                  , y = {
                    x: v.clientX,
                    y: v.clientY
                }
                  , p = (c == null ? void 0 : c.contains(w)) || (d == null ? void 0 : d.contains(w))
                  , x = !MC(y, i);
                p ? g() : x && (g(),
                u())
            }
            ;
            return document.addEventListener("pointermove", b),
            () => document.removeEventListener("pointermove", b)
        }
    }
    , [c, d, i, u, g]),
    a.jsx(ix, {
        ...e,
        ref: s
    })
}
)
  , [SC,jC] = zl(sx, {
    isInside: !1
})
  , CC = CN("TooltipContent")
  , ix = m.forwardRef( (e, t) => {
    const {__scopeTooltip: n, children: r, "aria-label": o, onEscapeKeyDown: s, onPointerDownOutside: i, ...l} = e
      , c = $l(ls, n)
      , u = Tf(n)
      , {onClose: d} = c;
    return m.useEffect( () => (document.addEventListener(Fh, d),
    () => document.removeEventListener(Fh, d)), [d]),
    m.useEffect( () => {
        if (c.trigger) {
            const f = g => {
                const h = g.target;
                h != null && h.contains(c.trigger) && d()
            }
            ;
            return window.addEventListener("scroll", f, {
                capture: !0
            }),
            () => window.removeEventListener("scroll", f, {
                capture: !0
            })
        }
    }
    , [c.trigger, d]),
    a.jsx(Ta, {
        asChild: !0,
        disableOutsidePointerEvents: !1,
        onEscapeKeyDown: s,
        onPointerDownOutside: i,
        onFocusOutside: f => f.preventDefault(),
        onDismiss: d,
        children: a.jsxs(ex, {
            "data-state": c.stateAttribute,
            ...u,
            ...l,
            ref: t,
            style: {
                ...l.style,
                "--radix-tooltip-content-transform-origin": "var(--radix-popper-transform-origin)",
                "--radix-tooltip-content-available-width": "var(--radix-popper-available-width)",
                "--radix-tooltip-content-available-height": "var(--radix-popper-available-height)",
                "--radix-tooltip-trigger-width": "var(--radix-popper-anchor-width)",
                "--radix-tooltip-trigger-height": "var(--radix-popper-anchor-height)"
            },
            children: [a.jsx(CC, {
                children: r
            }), a.jsx(SC, {
                scope: n,
                isInside: !0,
                children: a.jsx(KN, {
                    id: c.contentId,
                    role: "tooltip",
                    children: o || r
                })
            })]
        })
    })
}
);
ax.displayName = ls;
var lx = "TooltipArrow"
  , kC = m.forwardRef( (e, t) => {
    const {__scopeTooltip: n, ...r} = e
      , o = Tf(n);
    return jC(lx, n).isInside ? null : a.jsx(tx, {
        ...o,
        ...r,
        ref: t
    })
}
);
kC.displayName = lx;
function EC(e, t) {
    const n = Math.abs(t.top - e.y)
      , r = Math.abs(t.bottom - e.y)
      , o = Math.abs(t.right - e.x)
      , s = Math.abs(t.left - e.x);
    switch (Math.min(n, r, o, s)) {
    case s:
        return "left";
    case o:
        return "right";
    case n:
        return "top";
    case r:
        return "bottom";
    default:
        throw new Error("unreachable")
    }
}
function PC(e, t, n=5) {
    const r = [];
    switch (t) {
    case "top":
        r.push({
            x: e.x - n,
            y: e.y + n
        }, {
            x: e.x + n,
            y: e.y + n
        });
        break;
    case "bottom":
        r.push({
            x: e.x - n,
            y: e.y - n
        }, {
            x: e.x + n,
            y: e.y - n
        });
        break;
    case "left":
        r.push({
            x: e.x + n,
            y: e.y - n
        }, {
            x: e.x + n,
            y: e.y + n
        });
        break;
    case "right":
        r.push({
            x: e.x - n,
            y: e.y - n
        }, {
            x: e.x - n,
            y: e.y + n
        });
        break
    }
    return r
}
function TC(e) {
    const {top: t, right: n, bottom: r, left: o} = e;
    return [{
        x: o,
        y: t
    }, {
        x: n,
        y: t
    }, {
        x: n,
        y: r
    }, {
        x: o,
        y: r
    }]
}
function MC(e, t) {
    const {x: n, y: r} = e;
    let o = !1;
    for (let s = 0, i = t.length - 1; s < t.length; i = s++) {
        const l = t[s]
          , c = t[i]
          , u = l.x
          , d = l.y
          , f = c.x
          , g = c.y;
        d > r != g > r && n < (f - u) * (r - d) / (g - d) + u && (o = !o)
    }
    return o
}
function RC(e) {
    const t = e.slice();
    return t.sort( (n, r) => n.x < r.x ? -1 : n.x > r.x ? 1 : n.y < r.y ? -1 : n.y > r.y ? 1 : 0),
    _C(t)
}
function _C(e) {
    if (e.length <= 1)
        return e.slice();
    const t = [];
    for (let r = 0; r < e.length; r++) {
        const o = e[r];
        for (; t.length >= 2; ) {
            const s = t[t.length - 1]
              , i = t[t.length - 2];
            if ((s.x - i.x) * (o.y - i.y) >= (s.y - i.y) * (o.x - i.x))
                t.pop();
            else
                break
        }
        t.push(o)
    }
    t.pop();
    const n = [];
    for (let r = e.length - 1; r >= 0; r--) {
        const o = e[r];
        for (; n.length >= 2; ) {
            const s = n[n.length - 1]
              , i = n[n.length - 2];
            if ((s.x - i.x) * (o.y - i.y) >= (s.y - i.y) * (o.x - i.x))
                n.pop();
            else
                break
        }
        n.push(o)
    }
    return n.pop(),
    t.length === 1 && n.length === 1 && t[0].x === n[0].x && t[0].y === n[0].y ? t : t.concat(n)
}
var DC = ox
  , cx = ax;
const OC = DC
  , AC = m.forwardRef( ({className: e, sideOffset: t=4, ...n}, r) => a.jsx(cx, {
    ref: r,
    sideOffset: t,
    className: re("z-50 overflow-hidden rounded-md border bg-popover px-3 py-1.5 text-sm text-popover-foreground shadow-md animate-in fade-in-0 zoom-in-95 data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=closed]:zoom-out-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2", e),
    ...n
}));
AC.displayName = cx.displayName;
var Bl = class {
    constructor() {
        this.listeners = new Set,
        this.subscribe = this.subscribe.bind(this)
    }
    subscribe(e) {
        return this.listeners.add(e),
        this.onSubscribe(),
        () => {
            this.listeners.delete(e),
            this.onUnsubscribe()
        }
    }
    hasListeners() {
        return this.listeners.size > 0
    }
    onSubscribe() {}
    onUnsubscribe() {}
}
  , Wl = typeof window > "u" || "Deno"in globalThis;
function Wt() {}
function IC(e, t) {
    return typeof e == "function" ? e(t) : e
}
function LC(e) {
    return typeof e == "number" && e >= 0 && e !== 1 / 0
}
function FC(e, t) {
    return Math.max(e + (t || 0) - Date.now(), 0)
}
function ed(e, t) {
    return typeof e == "function" ? e(t) : e
}
function zC(e, t) {
    return typeof e == "function" ? e(t) : e
}
function zh(e, t) {
    const {type: n="all", exact: r, fetchStatus: o, predicate: s, queryKey: i, stale: l} = e;
    if (i) {
        if (r) {
            if (t.queryHash !== Mf(i, t.options))
                return !1
        } else if (!ya(t.queryKey, i))
            return !1
    }
    if (n !== "all") {
        const c = t.isActive();
        if (n === "active" && !c || n === "inactive" && c)
            return !1
    }
    return !(typeof l == "boolean" && t.isStale() !== l || o && o !== t.state.fetchStatus || s && !s(t))
}
function $h(e, t) {
    const {exact: n, status: r, predicate: o, mutationKey: s} = e;
    if (s) {
        if (!t.options.mutationKey)
            return !1;
        if (n) {
            if (ga(t.options.mutationKey) !== ga(s))
                return !1
        } else if (!ya(t.options.mutationKey, s))
            return !1
    }
    return !(r && t.state.status !== r || o && !o(t))
}
function Mf(e, t) {
    return ((t == null ? void 0 : t.queryKeyHashFn) || ga)(e)
}
function ga(e) {
    return JSON.stringify(e, (t, n) => td(n) ? Object.keys(n).sort().reduce( (r, o) => (r[o] = n[o],
    r), {}) : n)
}
function ya(e, t) {
    return e === t ? !0 : typeof e != typeof t ? !1 : e && t && typeof e == "object" && typeof t == "object" ? Object.keys(t).every(n => ya(e[n], t[n])) : !1
}
function ux(e, t) {
    if (e === t)
        return e;
    const n = Bh(e) && Bh(t);
    if (n || td(e) && td(t)) {
        const r = n ? e : Object.keys(e)
          , o = r.length
          , s = n ? t : Object.keys(t)
          , i = s.length
          , l = n ? [] : {}
          , c = new Set(r);
        let u = 0;
        for (let d = 0; d < i; d++) {
            const f = n ? d : s[d];
            (!n && c.has(f) || n) && e[f] === void 0 && t[f] === void 0 ? (l[f] = void 0,
            u++) : (l[f] = ux(e[f], t[f]),
            l[f] === e[f] && e[f] !== void 0 && u++)
        }
        return o === i && u === o ? e : l
    }
    return t
}
function Bh(e) {
    return Array.isArray(e) && e.length === Object.keys(e).length
}
function td(e) {
    if (!Wh(e))
        return !1;
    const t = e.constructor;
    if (t === void 0)
        return !0;
    const n = t.prototype;
    return !(!Wh(n) || !n.hasOwnProperty("isPrototypeOf") || Object.getPrototypeOf(e) !== Object.prototype)
}
function Wh(e) {
    return Object.prototype.toString.call(e) === "[object Object]"
}
function $C(e) {
    return new Promise(t => {
        setTimeout(t, e)
    }
    )
}
function BC(e, t, n) {
    return typeof n.structuralSharing == "function" ? n.structuralSharing(e, t) : n.structuralSharing !== !1 ? ux(e, t) : t
}
function WC(e, t, n=0) {
    const r = [...e, t];
    return n && r.length > n ? r.slice(1) : r
}
function HC(e, t, n=0) {
    const r = [t, ...e];
    return n && r.length > n ? r.slice(0, -1) : r
}
var Rf = Symbol();
function dx(e, t) {
    return !e.queryFn && (t != null && t.initialPromise) ? () => t.initialPromise : !e.queryFn || e.queryFn === Rf ? () => Promise.reject(new Error(`Missing queryFn: '${e.queryHash}'`)) : e.queryFn
}
var zr, er, Wo, xp, VC = (xp = class extends Bl {
    constructor() {
        super();
        ue(this, zr);
        ue(this, er);
        ue(this, Wo);
        X(this, Wo, t => {
            if (!Wl && window.addEventListener) {
                const n = () => t();
                return window.addEventListener("visibilitychange", n, !1),
                () => {
                    window.removeEventListener("visibilitychange", n)
                }
            }
        }
        )
    }
    onSubscribe() {
        P(this, er) || this.setEventListener(P(this, Wo))
    }
    onUnsubscribe() {
        var t;
        this.hasListeners() || ((t = P(this, er)) == null || t.call(this),
        X(this, er, void 0))
    }
    setEventListener(t) {
        var n;
        X(this, Wo, t),
        (n = P(this, er)) == null || n.call(this),
        X(this, er, t(r => {
            typeof r == "boolean" ? this.setFocused(r) : this.onFocus()
        }
        ))
    }
    setFocused(t) {
        P(this, zr) !== t && (X(this, zr, t),
        this.onFocus())
    }
    onFocus() {
        const t = this.isFocused();
        this.listeners.forEach(n => {
            n(t)
        }
        )
    }
    isFocused() {
        var t;
        return typeof P(this, zr) == "boolean" ? P(this, zr) : ((t = globalThis.document) == null ? void 0 : t.visibilityState) !== "hidden"
    }
}
,
zr = new WeakMap,
er = new WeakMap,
Wo = new WeakMap,
xp), fx = new VC, Ho, tr, Vo, wp, UC = (wp = class extends Bl {
    constructor() {
        super();
        ue(this, Ho, !0);
        ue(this, tr);
        ue(this, Vo);
        X(this, Vo, t => {
            if (!Wl && window.addEventListener) {
                const n = () => t(!0)
                  , r = () => t(!1);
                return window.addEventListener("online", n, !1),
                window.addEventListener("offline", r, !1),
                () => {
                    window.removeEventListener("online", n),
                    window.removeEventListener("offline", r)
                }
            }
        }
        )
    }
    onSubscribe() {
        P(this, tr) || this.setEventListener(P(this, Vo))
    }
    onUnsubscribe() {
        var t;
        this.hasListeners() || ((t = P(this, tr)) == null || t.call(this),
        X(this, tr, void 0))
    }
    setEventListener(t) {
        var n;
        X(this, Vo, t),
        (n = P(this, tr)) == null || n.call(this),
        X(this, tr, t(this.setOnline.bind(this)))
    }
    setOnline(t) {
        P(this, Ho) !== t && (X(this, Ho, t),
        this.listeners.forEach(r => {
            r(t)
        }
        ))
    }
    isOnline() {
        return P(this, Ho)
    }
}
,
Ho = new WeakMap,
tr = new WeakMap,
Vo = new WeakMap,
wp), il = new UC;
function YC() {
    let e, t;
    const n = new Promise( (o, s) => {
        e = o,
        t = s
    }
    );
    n.status = "pending",
    n.catch( () => {}
    );
    function r(o) {
        Object.assign(n, o),
        delete n.resolve,
        delete n.reject
    }
    return n.resolve = o => {
        r({
            status: "fulfilled",
            value: o
        }),
        e(o)
    }
    ,
    n.reject = o => {
        r({
            status: "rejected",
            reason: o
        }),
        t(o)
    }
    ,
    n
}
function KC(e) {
    return Math.min(1e3 * 2 ** e, 3e4)
}
function mx(e) {
    return (e ?? "online") === "online" ? il.isOnline() : !0
}
var hx = class extends Error {
    constructor(e) {
        super("CancelledError"),
        this.revert = e == null ? void 0 : e.revert,
        this.silent = e == null ? void 0 : e.silent
    }
}
;
function _c(e) {
    return e instanceof hx
}
function px(e) {
    let t = !1, n = 0, r = !1, o;
    const s = YC()
      , i = v => {
        var w;
        r || (g(new hx(v)),
        (w = e.abort) == null || w.call(e))
    }
      , l = () => {
        t = !0
    }
      , c = () => {
        t = !1
    }
      , u = () => fx.isFocused() && (e.networkMode === "always" || il.isOnline()) && e.canRun()
      , d = () => mx(e.networkMode) && e.canRun()
      , f = v => {
        var w;
        r || (r = !0,
        (w = e.onSuccess) == null || w.call(e, v),
        o == null || o(),
        s.resolve(v))
    }
      , g = v => {
        var w;
        r || (r = !0,
        (w = e.onError) == null || w.call(e, v),
        o == null || o(),
        s.reject(v))
    }
      , h = () => new Promise(v => {
        var w;
        o = y => {
            (r || u()) && v(y)
        }
        ,
        (w = e.onPause) == null || w.call(e)
    }
    ).then( () => {
        var v;
        o = void 0,
        r || (v = e.onContinue) == null || v.call(e)
    }
    )
      , b = () => {
        if (r)
            return;
        let v;
        const w = n === 0 ? e.initialPromise : void 0;
        try {
            v = w ?? e.fn()
        } catch (y) {
            v = Promise.reject(y)
        }
        Promise.resolve(v).then(f).catch(y => {
            var k;
            if (r)
                return;
            const p = e.retry ?? (Wl ? 0 : 3)
              , x = e.retryDelay ?? KC
              , N = typeof x == "function" ? x(n, y) : x
              , S = p === !0 || typeof p == "number" && n < p || typeof p == "function" && p(n, y);
            if (t || !S) {
                g(y);
                return
            }
            n++,
            (k = e.onFail) == null || k.call(e, n, y),
            $C(N).then( () => u() ? void 0 : h()).then( () => {
                t ? g(y) : b()
            }
            )
        }
        )
    }
    ;
    return {
        promise: s,
        cancel: i,
        continue: () => (o == null || o(),
        s),
        cancelRetry: l,
        continueRetry: c,
        canStart: d,
        start: () => (d() ? b() : h().then(b),
        s)
    }
}
var QC = e => setTimeout(e, 0);
function GC() {
    let e = []
      , t = 0
      , n = l => {
        l()
    }
      , r = l => {
        l()
    }
      , o = QC;
    const s = l => {
        t ? e.push(l) : o( () => {
            n(l)
        }
        )
    }
      , i = () => {
        const l = e;
        e = [],
        l.length && o( () => {
            r( () => {
                l.forEach(c => {
                    n(c)
                }
                )
            }
            )
        }
        )
    }
    ;
    return {
        batch: l => {
            let c;
            t++;
            try {
                c = l()
            } finally {
                t--,
                t || i()
            }
            return c
        }
        ,
        batchCalls: l => (...c) => {
            s( () => {
                l(...c)
            }
            )
        }
        ,
        schedule: s,
        setNotifyFunction: l => {
            n = l
        }
        ,
        setBatchNotifyFunction: l => {
            r = l
        }
        ,
        setScheduler: l => {
            o = l
        }
    }
}
var nt = GC(), $r, bp, vx = (bp = class {
    constructor() {
        ue(this, $r)
    }
    destroy() {
        this.clearGcTimeout()
    }
    scheduleGc() {
        this.clearGcTimeout(),
        LC(this.gcTime) && X(this, $r, setTimeout( () => {
            this.optionalRemove()
        }
        , this.gcTime))
    }
    updateGcTime(e) {
        this.gcTime = Math.max(this.gcTime || 0, e ?? (Wl ? 1 / 0 : 5 * 60 * 1e3))
    }
    clearGcTimeout() {
        P(this, $r) && (clearTimeout(P(this, $r)),
        X(this, $r, void 0))
    }
}
,
$r = new WeakMap,
bp), Uo, Br, kt, Wr, qe, Na, Hr, Ht, jn, Np, qC = (Np = class extends vx {
    constructor(t) {
        super();
        ue(this, Ht);
        ue(this, Uo);
        ue(this, Br);
        ue(this, kt);
        ue(this, Wr);
        ue(this, qe);
        ue(this, Na);
        ue(this, Hr);
        X(this, Hr, !1),
        X(this, Na, t.defaultOptions),
        this.setOptions(t.options),
        this.observers = [],
        X(this, Wr, t.client),
        X(this, kt, P(this, Wr).getQueryCache()),
        this.queryKey = t.queryKey,
        this.queryHash = t.queryHash,
        X(this, Uo, JC(this.options)),
        this.state = t.state ?? P(this, Uo),
        this.scheduleGc()
    }
    get meta() {
        return this.options.meta
    }
    get promise() {
        var t;
        return (t = P(this, qe)) == null ? void 0 : t.promise
    }
    setOptions(t) {
        this.options = {
            ...P(this, Na),
            ...t
        },
        this.updateGcTime(this.options.gcTime)
    }
    optionalRemove() {
        !this.observers.length && this.state.fetchStatus === "idle" && P(this, kt).remove(this)
    }
    setData(t, n) {
        const r = BC(this.state.data, t, this.options);
        return Ke(this, Ht, jn).call(this, {
            data: r,
            type: "success",
            dataUpdatedAt: n == null ? void 0 : n.updatedAt,
            manual: n == null ? void 0 : n.manual
        }),
        r
    }
    setState(t, n) {
        Ke(this, Ht, jn).call(this, {
            type: "setState",
            state: t,
            setStateOptions: n
        })
    }
    cancel(t) {
        var r, o;
        const n = (r = P(this, qe)) == null ? void 0 : r.promise;
        return (o = P(this, qe)) == null || o.cancel(t),
        n ? n.then(Wt).catch(Wt) : Promise.resolve()
    }
    destroy() {
        super.destroy(),
        this.cancel({
            silent: !0
        })
    }
    reset() {
        this.destroy(),
        this.setState(P(this, Uo))
    }
    isActive() {
        return this.observers.some(t => zC(t.options.enabled, this) !== !1)
    }
    isDisabled() {
        return this.getObserversCount() > 0 ? !this.isActive() : this.options.queryFn === Rf || this.state.dataUpdateCount + this.state.errorUpdateCount === 0
    }
    isStatic() {
        return this.getObserversCount() > 0 ? this.observers.some(t => ed(t.options.staleTime, this) === "static") : !1
    }
    isStale() {
        return this.getObserversCount() > 0 ? this.observers.some(t => t.getCurrentResult().isStale) : this.state.data === void 0 || this.state.isInvalidated
    }
    isStaleByTime(t=0) {
        return this.state.data === void 0 ? !0 : t === "static" ? !1 : this.state.isInvalidated ? !0 : !FC(this.state.dataUpdatedAt, t)
    }
    onFocus() {
        var n;
        const t = this.observers.find(r => r.shouldFetchOnWindowFocus());
        t == null || t.refetch({
            cancelRefetch: !1
        }),
        (n = P(this, qe)) == null || n.continue()
    }
    onOnline() {
        var n;
        const t = this.observers.find(r => r.shouldFetchOnReconnect());
        t == null || t.refetch({
            cancelRefetch: !1
        }),
        (n = P(this, qe)) == null || n.continue()
    }
    addObserver(t) {
        this.observers.includes(t) || (this.observers.push(t),
        this.clearGcTimeout(),
        P(this, kt).notify({
            type: "observerAdded",
            query: this,
            observer: t
        }))
    }
    removeObserver(t) {
        this.observers.includes(t) && (this.observers = this.observers.filter(n => n !== t),
        this.observers.length || (P(this, qe) && (P(this, Hr) ? P(this, qe).cancel({
            revert: !0
        }) : P(this, qe).cancelRetry()),
        this.scheduleGc()),
        P(this, kt).notify({
            type: "observerRemoved",
            query: this,
            observer: t
        }))
    }
    getObserversCount() {
        return this.observers.length
    }
    invalidate() {
        this.state.isInvalidated || Ke(this, Ht, jn).call(this, {
            type: "invalidate"
        })
    }
    fetch(t, n) {
        var u, d, f;
        if (this.state.fetchStatus !== "idle") {
            if (this.state.data !== void 0 && (n != null && n.cancelRefetch))
                this.cancel({
                    silent: !0
                });
            else if (P(this, qe))
                return P(this, qe).continueRetry(),
                P(this, qe).promise
        }
        if (t && this.setOptions(t),
        !this.options.queryFn) {
            const g = this.observers.find(h => h.options.queryFn);
            g && this.setOptions(g.options)
        }
        const r = new AbortController
          , o = g => {
            Object.defineProperty(g, "signal", {
                enumerable: !0,
                get: () => (X(this, Hr, !0),
                r.signal)
            })
        }
          , s = () => {
            const g = dx(this.options, n)
              , b = ( () => {
                const v = {
                    client: P(this, Wr),
                    queryKey: this.queryKey,
                    meta: this.meta
                };
                return o(v),
                v
            }
            )();
            return X(this, Hr, !1),
            this.options.persister ? this.options.persister(g, b, this) : g(b)
        }
          , l = ( () => {
            const g = {
                fetchOptions: n,
                options: this.options,
                queryKey: this.queryKey,
                client: P(this, Wr),
                state: this.state,
                fetchFn: s
            };
            return o(g),
            g
        }
        )();
        (u = this.options.behavior) == null || u.onFetch(l, this),
        X(this, Br, this.state),
        (this.state.fetchStatus === "idle" || this.state.fetchMeta !== ((d = l.fetchOptions) == null ? void 0 : d.meta)) && Ke(this, Ht, jn).call(this, {
            type: "fetch",
            meta: (f = l.fetchOptions) == null ? void 0 : f.meta
        });
        const c = g => {
            var h, b, v, w;
            _c(g) && g.silent || Ke(this, Ht, jn).call(this, {
                type: "error",
                error: g
            }),
            _c(g) || ((b = (h = P(this, kt).config).onError) == null || b.call(h, g, this),
            (w = (v = P(this, kt).config).onSettled) == null || w.call(v, this.state.data, g, this)),
            this.scheduleGc()
        }
        ;
        return X(this, qe, px({
            initialPromise: n == null ? void 0 : n.initialPromise,
            fn: l.fetchFn,
            abort: r.abort.bind(r),
            onSuccess: g => {
                var h, b, v, w;
                if (g === void 0) {
                    c(new Error(`${this.queryHash} data is undefined`));
                    return
                }
                try {
                    this.setData(g)
                } catch (y) {
                    c(y);
                    return
                }
                (b = (h = P(this, kt).config).onSuccess) == null || b.call(h, g, this),
                (w = (v = P(this, kt).config).onSettled) == null || w.call(v, g, this.state.error, this),
                this.scheduleGc()
            }
            ,
            onError: c,
            onFail: (g, h) => {
                Ke(this, Ht, jn).call(this, {
                    type: "failed",
                    failureCount: g,
                    error: h
                })
            }
            ,
            onPause: () => {
                Ke(this, Ht, jn).call(this, {
                    type: "pause"
                })
            }
            ,
            onContinue: () => {
                Ke(this, Ht, jn).call(this, {
                    type: "continue"
                })
            }
            ,
            retry: l.options.retry,
            retryDelay: l.options.retryDelay,
            networkMode: l.options.networkMode,
            canRun: () => !0
        })),
        P(this, qe).start()
    }
}
,
Uo = new WeakMap,
Br = new WeakMap,
kt = new WeakMap,
Wr = new WeakMap,
qe = new WeakMap,
Na = new WeakMap,
Hr = new WeakMap,
Ht = new WeakSet,
jn = function(t) {
    const n = r => {
        switch (t.type) {
        case "failed":
            return {
                ...r,
                fetchFailureCount: t.failureCount,
                fetchFailureReason: t.error
            };
        case "pause":
            return {
                ...r,
                fetchStatus: "paused"
            };
        case "continue":
            return {
                ...r,
                fetchStatus: "fetching"
            };
        case "fetch":
            return {
                ...r,
                ...XC(r.data, this.options),
                fetchMeta: t.meta ?? null
            };
        case "success":
            return X(this, Br, void 0),
            {
                ...r,
                data: t.data,
                dataUpdateCount: r.dataUpdateCount + 1,
                dataUpdatedAt: t.dataUpdatedAt ?? Date.now(),
                error: null,
                isInvalidated: !1,
                status: "success",
                ...!t.manual && {
                    fetchStatus: "idle",
                    fetchFailureCount: 0,
                    fetchFailureReason: null
                }
            };
        case "error":
            const o = t.error;
            return _c(o) && o.revert && P(this, Br) ? {
                ...P(this, Br),
                fetchStatus: "idle"
            } : {
                ...r,
                error: o,
                errorUpdateCount: r.errorUpdateCount + 1,
                errorUpdatedAt: Date.now(),
                fetchFailureCount: r.fetchFailureCount + 1,
                fetchFailureReason: o,
                fetchStatus: "idle",
                status: "error"
            };
        case "invalidate":
            return {
                ...r,
                isInvalidated: !0
            };
        case "setState":
            return {
                ...r,
                ...t.state
            }
        }
    }
    ;
    this.state = n(this.state),
    nt.batch( () => {
        this.observers.forEach(r => {
            r.onQueryUpdate()
        }
        ),
        P(this, kt).notify({
            query: this,
            type: "updated",
            action: t
        })
    }
    )
}
,
Np);
function XC(e, t) {
    return {
        fetchFailureCount: 0,
        fetchFailureReason: null,
        fetchStatus: mx(t.networkMode) ? "fetching" : "paused",
        ...e === void 0 && {
            error: null,
            status: "pending"
        }
    }
}
function JC(e) {
    const t = typeof e.initialData == "function" ? e.initialData() : e.initialData
      , n = t !== void 0
      , r = n ? typeof e.initialDataUpdatedAt == "function" ? e.initialDataUpdatedAt() : e.initialDataUpdatedAt : 0;
    return {
        data: t,
        dataUpdateCount: 0,
        dataUpdatedAt: n ? r ?? Date.now() : 0,
        error: null,
        errorUpdateCount: 0,
        errorUpdatedAt: 0,
        fetchFailureCount: 0,
        fetchFailureReason: null,
        fetchMeta: null,
        isInvalidated: !1,
        status: n ? "success" : "pending",
        fetchStatus: "idle"
    }
}
var ln, Sp, ZC = (Sp = class extends Bl {
    constructor(t={}) {
        super();
        ue(this, ln);
        this.config = t,
        X(this, ln, new Map)
    }
    build(t, n, r) {
        const o = n.queryKey
          , s = n.queryHash ?? Mf(o, n);
        let i = this.get(s);
        return i || (i = new qC({
            client: t,
            queryKey: o,
            queryHash: s,
            options: t.defaultQueryOptions(n),
            state: r,
            defaultOptions: t.getQueryDefaults(o)
        }),
        this.add(i)),
        i
    }
    add(t) {
        P(this, ln).has(t.queryHash) || (P(this, ln).set(t.queryHash, t),
        this.notify({
            type: "added",
            query: t
        }))
    }
    remove(t) {
        const n = P(this, ln).get(t.queryHash);
        n && (t.destroy(),
        n === t && P(this, ln).delete(t.queryHash),
        this.notify({
            type: "removed",
            query: t
        }))
    }
    clear() {
        nt.batch( () => {
            this.getAll().forEach(t => {
                this.remove(t)
            }
            )
        }
        )
    }
    get(t) {
        return P(this, ln).get(t)
    }
    getAll() {
        return [...P(this, ln).values()]
    }
    find(t) {
        const n = {
            exact: !0,
            ...t
        };
        return this.getAll().find(r => zh(n, r))
    }
    findAll(t={}) {
        const n = this.getAll();
        return Object.keys(t).length > 0 ? n.filter(r => zh(t, r)) : n
    }
    notify(t) {
        nt.batch( () => {
            this.listeners.forEach(n => {
                n(t)
            }
            )
        }
        )
    }
    onFocus() {
        nt.batch( () => {
            this.getAll().forEach(t => {
                t.onFocus()
            }
            )
        }
        )
    }
    onOnline() {
        nt.batch( () => {
            this.getAll().forEach(t => {
                t.onOnline()
            }
            )
        }
        )
    }
}
,
ln = new WeakMap,
Sp), cn, Ze, Vr, un, Qn, jp, ek = (jp = class extends vx {
    constructor(t) {
        super();
        ue(this, un);
        ue(this, cn);
        ue(this, Ze);
        ue(this, Vr);
        this.mutationId = t.mutationId,
        X(this, Ze, t.mutationCache),
        X(this, cn, []),
        this.state = t.state || tk(),
        this.setOptions(t.options),
        this.scheduleGc()
    }
    setOptions(t) {
        this.options = t,
        this.updateGcTime(this.options.gcTime)
    }
    get meta() {
        return this.options.meta
    }
    addObserver(t) {
        P(this, cn).includes(t) || (P(this, cn).push(t),
        this.clearGcTimeout(),
        P(this, Ze).notify({
            type: "observerAdded",
            mutation: this,
            observer: t
        }))
    }
    removeObserver(t) {
        X(this, cn, P(this, cn).filter(n => n !== t)),
        this.scheduleGc(),
        P(this, Ze).notify({
            type: "observerRemoved",
            mutation: this,
            observer: t
        })
    }
    optionalRemove() {
        P(this, cn).length || (this.state.status === "pending" ? this.scheduleGc() : P(this, Ze).remove(this))
    }
    continue() {
        var t;
        return ((t = P(this, Vr)) == null ? void 0 : t.continue()) ?? this.execute(this.state.variables)
    }
    async execute(t) {
        var s, i, l, c, u, d, f, g, h, b, v, w, y, p, x, N, S, k, C, T;
        const n = () => {
            Ke(this, un, Qn).call(this, {
                type: "continue"
            })
        }
        ;
        X(this, Vr, px({
            fn: () => this.options.mutationFn ? this.options.mutationFn(t) : Promise.reject(new Error("No mutationFn found")),
            onFail: (D, R) => {
                Ke(this, un, Qn).call(this, {
                    type: "failed",
                    failureCount: D,
                    error: R
                })
            }
            ,
            onPause: () => {
                Ke(this, un, Qn).call(this, {
                    type: "pause"
                })
            }
            ,
            onContinue: n,
            retry: this.options.retry ?? 0,
            retryDelay: this.options.retryDelay,
            networkMode: this.options.networkMode,
            canRun: () => P(this, Ze).canRun(this)
        }));
        const r = this.state.status === "pending"
          , o = !P(this, Vr).canStart();
        try {
            if (r)
                n();
            else {
                Ke(this, un, Qn).call(this, {
                    type: "pending",
                    variables: t,
                    isPaused: o
                }),
                await ((i = (s = P(this, Ze).config).onMutate) == null ? void 0 : i.call(s, t, this));
                const R = await ((c = (l = this.options).onMutate) == null ? void 0 : c.call(l, t));
                R !== this.state.context && Ke(this, un, Qn).call(this, {
                    type: "pending",
                    context: R,
                    variables: t,
                    isPaused: o
                })
            }
            const D = await P(this, Vr).start();
            return await ((d = (u = P(this, Ze).config).onSuccess) == null ? void 0 : d.call(u, D, t, this.state.context, this)),
            await ((g = (f = this.options).onSuccess) == null ? void 0 : g.call(f, D, t, this.state.context)),
            await ((b = (h = P(this, Ze).config).onSettled) == null ? void 0 : b.call(h, D, null, this.state.variables, this.state.context, this)),
            await ((w = (v = this.options).onSettled) == null ? void 0 : w.call(v, D, null, t, this.state.context)),
            Ke(this, un, Qn).call(this, {
                type: "success",
                data: D
            }),
            D
        } catch (D) {
            try {
                throw await ((p = (y = P(this, Ze).config).onError) == null ? void 0 : p.call(y, D, t, this.state.context, this)),
                await ((N = (x = this.options).onError) == null ? void 0 : N.call(x, D, t, this.state.context)),
                await ((k = (S = P(this, Ze).config).onSettled) == null ? void 0 : k.call(S, void 0, D, this.state.variables, this.state.context, this)),
                await ((T = (C = this.options).onSettled) == null ? void 0 : T.call(C, void 0, D, t, this.state.context)),
                D
            } finally {
                Ke(this, un, Qn).call(this, {
                    type: "error",
                    error: D
                })
            }
        } finally {
            P(this, Ze).runNext(this)
        }
    }
}
,
cn = new WeakMap,
Ze = new WeakMap,
Vr = new WeakMap,
un = new WeakSet,
Qn = function(t) {
    const n = r => {
        switch (t.type) {
        case "failed":
            return {
                ...r,
                failureCount: t.failureCount,
                failureReason: t.error
            };
        case "pause":
            return {
                ...r,
                isPaused: !0
            };
        case "continue":
            return {
                ...r,
                isPaused: !1
            };
        case "pending":
            return {
                ...r,
                context: t.context,
                data: void 0,
                failureCount: 0,
                failureReason: null,
                error: null,
                isPaused: t.isPaused,
                status: "pending",
                variables: t.variables,
                submittedAt: Date.now()
            };
        case "success":
            return {
                ...r,
                data: t.data,
                failureCount: 0,
                failureReason: null,
                error: null,
                status: "success",
                isPaused: !1
            };
        case "error":
            return {
                ...r,
                data: void 0,
                error: t.error,
                failureCount: r.failureCount + 1,
                failureReason: t.error,
                isPaused: !1,
                status: "error"
            }
        }
    }
    ;
    this.state = n(this.state),
    nt.batch( () => {
        P(this, cn).forEach(r => {
            r.onMutationUpdate(t)
        }
        ),
        P(this, Ze).notify({
            mutation: this,
            type: "updated",
            action: t
        })
    }
    )
}
,
jp);
function tk() {
    return {
        context: void 0,
        data: void 0,
        error: null,
        failureCount: 0,
        failureReason: null,
        isPaused: !1,
        status: "idle",
        variables: void 0,
        submittedAt: 0
    }
}
var Pn, Vt, Sa, Cp, nk = (Cp = class extends Bl {
    constructor(t={}) {
        super();
        ue(this, Pn);
        ue(this, Vt);
        ue(this, Sa);
        this.config = t,
        X(this, Pn, new Set),
        X(this, Vt, new Map),
        X(this, Sa, 0)
    }
    build(t, n, r) {
        const o = new ek({
            mutationCache: this,
            mutationId: ++$a(this, Sa)._,
            options: t.defaultMutationOptions(n),
            state: r
        });
        return this.add(o),
        o
    }
    add(t) {
        P(this, Pn).add(t);
        const n = li(t);
        if (typeof n == "string") {
            const r = P(this, Vt).get(n);
            r ? r.push(t) : P(this, Vt).set(n, [t])
        }
        this.notify({
            type: "added",
            mutation: t
        })
    }
    remove(t) {
        if (P(this, Pn).delete(t)) {
            const n = li(t);
            if (typeof n == "string") {
                const r = P(this, Vt).get(n);
                if (r)
                    if (r.length > 1) {
                        const o = r.indexOf(t);
                        o !== -1 && r.splice(o, 1)
                    } else
                        r[0] === t && P(this, Vt).delete(n)
            }
        }
        this.notify({
            type: "removed",
            mutation: t
        })
    }
    canRun(t) {
        const n = li(t);
        if (typeof n == "string") {
            const r = P(this, Vt).get(n)
              , o = r == null ? void 0 : r.find(s => s.state.status === "pending");
            return !o || o === t
        } else
            return !0
    }
    runNext(t) {
        var r;
        const n = li(t);
        if (typeof n == "string") {
            const o = (r = P(this, Vt).get(n)) == null ? void 0 : r.find(s => s !== t && s.state.isPaused);
            return (o == null ? void 0 : o.continue()) ?? Promise.resolve()
        } else
            return Promise.resolve()
    }
    clear() {
        nt.batch( () => {
            P(this, Pn).forEach(t => {
                this.notify({
                    type: "removed",
                    mutation: t
                })
            }
            ),
            P(this, Pn).clear(),
            P(this, Vt).clear()
        }
        )
    }
    getAll() {
        return Array.from(P(this, Pn))
    }
    find(t) {
        const n = {
            exact: !0,
            ...t
        };
        return this.getAll().find(r => $h(n, r))
    }
    findAll(t={}) {
        return this.getAll().filter(n => $h(t, n))
    }
    notify(t) {
        nt.batch( () => {
            this.listeners.forEach(n => {
                n(t)
            }
            )
        }
        )
    }
    resumePausedMutations() {
        const t = this.getAll().filter(n => n.state.isPaused);
        return nt.batch( () => Promise.all(t.map(n => n.continue().catch(Wt))))
    }
}
,
Pn = new WeakMap,
Vt = new WeakMap,
Sa = new WeakMap,
Cp);
function li(e) {
    var t;
    return (t = e.options.scope) == null ? void 0 : t.id
}
function Hh(e) {
    return {
        onFetch: (t, n) => {
            var d, f, g, h, b;
            const r = t.options
              , o = (g = (f = (d = t.fetchOptions) == null ? void 0 : d.meta) == null ? void 0 : f.fetchMore) == null ? void 0 : g.direction
              , s = ((h = t.state.data) == null ? void 0 : h.pages) || []
              , i = ((b = t.state.data) == null ? void 0 : b.pageParams) || [];
            let l = {
                pages: [],
                pageParams: []
            }
              , c = 0;
            const u = async () => {
                let v = !1;
                const w = x => {
                    Object.defineProperty(x, "signal", {
                        enumerable: !0,
                        get: () => (t.signal.aborted ? v = !0 : t.signal.addEventListener("abort", () => {
                            v = !0
                        }
                        ),
                        t.signal)
                    })
                }
                  , y = dx(t.options, t.fetchOptions)
                  , p = async (x, N, S) => {
                    if (v)
                        return Promise.reject();
                    if (N == null && x.pages.length)
                        return Promise.resolve(x);
                    const C = ( () => {
                        const F = {
                            client: t.client,
                            queryKey: t.queryKey,
                            pageParam: N,
                            direction: S ? "backward" : "forward",
                            meta: t.options.meta
                        };
                        return w(F),
                        F
                    }
                    )()
                      , T = await y(C)
                      , {maxPages: D} = t.options
                      , R = S ? HC : WC;
                    return {
                        pages: R(x.pages, T, D),
                        pageParams: R(x.pageParams, N, D)
                    }
                }
                ;
                if (o && s.length) {
                    const x = o === "backward"
                      , N = x ? rk : Vh
                      , S = {
                        pages: s,
                        pageParams: i
                    }
                      , k = N(r, S);
                    l = await p(S, k, x)
                } else {
                    const x = e ?? s.length;
                    do {
                        const N = c === 0 ? i[0] ?? r.initialPageParam : Vh(r, l);
                        if (c > 0 && N == null)
                            break;
                        l = await p(l, N),
                        c++
                    } while (c < x)
                }
                return l
            }
            ;
            t.options.persister ? t.fetchFn = () => {
                var v, w;
                return (w = (v = t.options).persister) == null ? void 0 : w.call(v, u, {
                    client: t.client,
                    queryKey: t.queryKey,
                    meta: t.options.meta,
                    signal: t.signal
                }, n)
            }
            : t.fetchFn = u
        }
    }
}
function Vh(e, {pages: t, pageParams: n}) {
    const r = t.length - 1;
    return t.length > 0 ? e.getNextPageParam(t[r], t, n[r], n) : void 0
}
function rk(e, {pages: t, pageParams: n}) {
    var r;
    return t.length > 0 ? (r = e.getPreviousPageParam) == null ? void 0 : r.call(e, t[0], t, n[0], n) : void 0
}
var _e, nr, rr, Yo, Ko, or, Qo, Go, kp, ok = (kp = class {
    constructor(e={}) {
        ue(this, _e);
        ue(this, nr);
        ue(this, rr);
        ue(this, Yo);
        ue(this, Ko);
        ue(this, or);
        ue(this, Qo);
        ue(this, Go);
        X(this, _e, e.queryCache || new ZC),
        X(this, nr, e.mutationCache || new nk),
        X(this, rr, e.defaultOptions || {}),
        X(this, Yo, new Map),
        X(this, Ko, new Map),
        X(this, or, 0)
    }
    mount() {
        $a(this, or)._++,
        P(this, or) === 1 && (X(this, Qo, fx.subscribe(async e => {
            e && (await this.resumePausedMutations(),
            P(this, _e).onFocus())
        }
        )),
        X(this, Go, il.subscribe(async e => {
            e && (await this.resumePausedMutations(),
            P(this, _e).onOnline())
        }
        )))
    }
    unmount() {
        var e, t;
        $a(this, or)._--,
        P(this, or) === 0 && ((e = P(this, Qo)) == null || e.call(this),
        X(this, Qo, void 0),
        (t = P(this, Go)) == null || t.call(this),
        X(this, Go, void 0))
    }
    isFetching(e) {
        return P(this, _e).findAll({
            ...e,
            fetchStatus: "fetching"
        }).length
    }
    isMutating(e) {
        return P(this, nr).findAll({
            ...e,
            status: "pending"
        }).length
    }
    getQueryData(e) {
        var n;
        const t = this.defaultQueryOptions({
            queryKey: e
        });
        return (n = P(this, _e).get(t.queryHash)) == null ? void 0 : n.state.data
    }
    ensureQueryData(e) {
        const t = this.defaultQueryOptions(e)
          , n = P(this, _e).build(this, t)
          , r = n.state.data;
        return r === void 0 ? this.fetchQuery(e) : (e.revalidateIfStale && n.isStaleByTime(ed(t.staleTime, n)) && this.prefetchQuery(t),
        Promise.resolve(r))
    }
    getQueriesData(e) {
        return P(this, _e).findAll(e).map( ({queryKey: t, state: n}) => {
            const r = n.data;
            return [t, r]
        }
        )
    }
    setQueryData(e, t, n) {
        const r = this.defaultQueryOptions({
            queryKey: e
        })
          , o = P(this, _e).get(r.queryHash)
          , s = o == null ? void 0 : o.state.data
          , i = IC(t, s);
        if (i !== void 0)
            return P(this, _e).build(this, r).setData(i, {
                ...n,
                manual: !0
            })
    }
    setQueriesData(e, t, n) {
        return nt.batch( () => P(this, _e).findAll(e).map( ({queryKey: r}) => [r, this.setQueryData(r, t, n)]))
    }
    getQueryState(e) {
        var n;
        const t = this.defaultQueryOptions({
            queryKey: e
        });
        return (n = P(this, _e).get(t.queryHash)) == null ? void 0 : n.state
    }
    removeQueries(e) {
        const t = P(this, _e);
        nt.batch( () => {
            t.findAll(e).forEach(n => {
                t.remove(n)
            }
            )
        }
        )
    }
    resetQueries(e, t) {
        const n = P(this, _e);
        return nt.batch( () => (n.findAll(e).forEach(r => {
            r.reset()
        }
        ),
        this.refetchQueries({
            type: "active",
            ...e
        }, t)))
    }
    cancelQueries(e, t={}) {
        const n = {
            revert: !0,
            ...t
        }
          , r = nt.batch( () => P(this, _e).findAll(e).map(o => o.cancel(n)));
        return Promise.all(r).then(Wt).catch(Wt)
    }
    invalidateQueries(e, t={}) {
        return nt.batch( () => (P(this, _e).findAll(e).forEach(n => {
            n.invalidate()
        }
        ),
        (e == null ? void 0 : e.refetchType) === "none" ? Promise.resolve() : this.refetchQueries({
            ...e,
            type: (e == null ? void 0 : e.refetchType) ?? (e == null ? void 0 : e.type) ?? "active"
        }, t)))
    }
    refetchQueries(e, t={}) {
        const n = {
            ...t,
            cancelRefetch: t.cancelRefetch ?? !0
        }
          , r = nt.batch( () => P(this, _e).findAll(e).filter(o => !o.isDisabled() && !o.isStatic()).map(o => {
            let s = o.fetch(void 0, n);
            return n.throwOnError || (s = s.catch(Wt)),
            o.state.fetchStatus === "paused" ? Promise.resolve() : s
        }
        ));
        return Promise.all(r).then(Wt)
    }
    fetchQuery(e) {
        const t = this.defaultQueryOptions(e);
        t.retry === void 0 && (t.retry = !1);
        const n = P(this, _e).build(this, t);
        return n.isStaleByTime(ed(t.staleTime, n)) ? n.fetch(t) : Promise.resolve(n.state.data)
    }
    prefetchQuery(e) {
        return this.fetchQuery(e).then(Wt).catch(Wt)
    }
    fetchInfiniteQuery(e) {
        return e.behavior = Hh(e.pages),
        this.fetchQuery(e)
    }
    prefetchInfiniteQuery(e) {
        return this.fetchInfiniteQuery(e).then(Wt).catch(Wt)
    }
    ensureInfiniteQueryData(e) {
        return e.behavior = Hh(e.pages),
        this.ensureQueryData(e)
    }
    resumePausedMutations() {
        return il.isOnline() ? P(this, nr).resumePausedMutations() : Promise.resolve()
    }
    getQueryCache() {
        return P(this, _e)
    }
    getMutationCache() {
        return P(this, nr)
    }
    getDefaultOptions() {
        return P(this, rr)
    }
    setDefaultOptions(e) {
        X(this, rr, e)
    }
    setQueryDefaults(e, t) {
        P(this, Yo).set(ga(e), {
            queryKey: e,
            defaultOptions: t
        })
    }
    getQueryDefaults(e) {
        const t = [...P(this, Yo).values()]
          , n = {};
        return t.forEach(r => {
            ya(e, r.queryKey) && Object.assign(n, r.defaultOptions)
        }
        ),
        n
    }
    setMutationDefaults(e, t) {
        P(this, Ko).set(ga(e), {
            mutationKey: e,
            defaultOptions: t
        })
    }
    getMutationDefaults(e) {
        const t = [...P(this, Ko).values()]
          , n = {};
        return t.forEach(r => {
            ya(e, r.mutationKey) && Object.assign(n, r.defaultOptions)
        }
        ),
        n
    }
    defaultQueryOptions(e) {
        if (e._defaulted)
            return e;
        const t = {
            ...P(this, rr).queries,
            ...this.getQueryDefaults(e.queryKey),
            ...e,
            _defaulted: !0
        };
        return t.queryHash || (t.queryHash = Mf(t.queryKey, t)),
        t.refetchOnReconnect === void 0 && (t.refetchOnReconnect = t.networkMode !== "always"),
        t.throwOnError === void 0 && (t.throwOnError = !!t.suspense),
        !t.networkMode && t.persister && (t.networkMode = "offlineFirst"),
        t.queryFn === Rf && (t.enabled = !1),
        t
    }
    defaultMutationOptions(e) {
        return e != null && e._defaulted ? e : {
            ...P(this, rr).mutations,
            ...(e == null ? void 0 : e.mutationKey) && this.getMutationDefaults(e.mutationKey),
            ...e,
            _defaulted: !0
        }
    }
    clear() {
        P(this, _e).clear(),
        P(this, nr).clear()
    }
}
,
_e = new WeakMap,
nr = new WeakMap,
rr = new WeakMap,
Yo = new WeakMap,
Ko = new WeakMap,
or = new WeakMap,
Qo = new WeakMap,
Go = new WeakMap,
kp), sk = m.createContext(void 0), ak = ({client: e, children: t}) => (m.useEffect( () => (e.mount(),
() => {
    e.unmount()
}
), [e]),
a.jsx(sk.Provider, {
    value: e,
    children: t
}));
/**
 * @remix-run/router v1.23.0
 *
 * Copyright (c) Remix Software Inc.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE.md file in the root directory of this source tree.
 *
 * @license MIT
 */
function xa() {
    return xa = Object.assign ? Object.assign.bind() : function(e) {
        for (var t = 1; t < arguments.length; t++) {
            var n = arguments[t];
            for (var r in n)
                Object.prototype.hasOwnProperty.call(n, r) && (e[r] = n[r])
        }
        return e
    }
    ,
    xa.apply(this, arguments)
}
var lr;
(function(e) {
    e.Pop = "POP",
    e.Push = "PUSH",
    e.Replace = "REPLACE"
}
)(lr || (lr = {}));
const Uh = "popstate";
function ik(e) {
    e === void 0 && (e = {});
    function t(r, o) {
        let {pathname: s, search: i, hash: l} = r.location;
        return nd("", {
            pathname: s,
            search: i,
            hash: l
        }, o.state && o.state.usr || null, o.state && o.state.key || "default")
    }
    function n(r, o) {
        return typeof o == "string" ? o : ll(o)
    }
    return ck(t, n, null, e)
}
function Ie(e, t) {
    if (e === !1 || e === null || typeof e > "u")
        throw new Error(t)
}
function gx(e, t) {
    if (!e) {
        typeof console < "u" && console.warn(t);
        try {
            throw new Error(t)
        } catch {}
    }
}
function lk() {
    return Math.random().toString(36).substr(2, 8)
}
function Yh(e, t) {
    return {
        usr: e.state,
        key: e.key,
        idx: t
    }
}
function nd(e, t, n, r) {
    return n === void 0 && (n = null),
    xa({
        pathname: typeof e == "string" ? e : e.pathname,
        search: "",
        hash: ""
    }, typeof t == "string" ? gs(t) : t, {
        state: n,
        key: t && t.key || r || lk()
    })
}
function ll(e) {
    let {pathname: t="/", search: n="", hash: r=""} = e;
    return n && n !== "?" && (t += n.charAt(0) === "?" ? n : "?" + n),
    r && r !== "#" && (t += r.charAt(0) === "#" ? r : "#" + r),
    t
}
function gs(e) {
    let t = {};
    if (e) {
        let n = e.indexOf("#");
        n >= 0 && (t.hash = e.substr(n),
        e = e.substr(0, n));
        let r = e.indexOf("?");
        r >= 0 && (t.search = e.substr(r),
        e = e.substr(0, r)),
        e && (t.pathname = e)
    }
    return t
}
function ck(e, t, n, r) {
    r === void 0 && (r = {});
    let {window: o=document.defaultView, v5Compat: s=!1} = r
      , i = o.history
      , l = lr.Pop
      , c = null
      , u = d();
    u == null && (u = 0,
    i.replaceState(xa({}, i.state, {
        idx: u
    }), ""));
    function d() {
        return (i.state || {
            idx: null
        }).idx
    }
    function f() {
        l = lr.Pop;
        let w = d()
          , y = w == null ? null : w - u;
        u = w,
        c && c({
            action: l,
            location: v.location,
            delta: y
        })
    }
    function g(w, y) {
        l = lr.Push;
        let p = nd(v.location, w, y);
        u = d() + 1;
        let x = Yh(p, u)
          , N = v.createHref(p);
        try {
            i.pushState(x, "", N)
        } catch (S) {
            if (S instanceof DOMException && S.name === "DataCloneError")
                throw S;
            o.location.assign(N)
        }
        s && c && c({
            action: l,
            location: v.location,
            delta: 1
        })
    }
    function h(w, y) {
        l = lr.Replace;
        let p = nd(v.location, w, y);
        u = d();
        let x = Yh(p, u)
          , N = v.createHref(p);
        i.replaceState(x, "", N),
        s && c && c({
            action: l,
            location: v.location,
            delta: 0
        })
    }
    function b(w) {
        let y = o.location.origin !== "null" ? o.location.origin : o.location.href
          , p = typeof w == "string" ? w : ll(w);
        return p = p.replace(/ $/, "%20"),
        Ie(y, "No window.location.(origin|href) available to create URL for href: " + p),
        new URL(p,y)
    }
    let v = {
        get action() {
            return l
        },
        get location() {
            return e(o, i)
        },
        listen(w) {
            if (c)
                throw new Error("A history only accepts one active listener");
            return o.addEventListener(Uh, f),
            c = w,
            () => {
                o.removeEventListener(Uh, f),
                c = null
            }
        },
        createHref(w) {
            return t(o, w)
        },
        createURL: b,
        encodeLocation(w) {
            let y = b(w);
            return {
                pathname: y.pathname,
                search: y.search,
                hash: y.hash
            }
        },
        push: g,
        replace: h,
        go(w) {
            return i.go(w)
        }
    };
    return v
}
var Kh;
(function(e) {
    e.data = "data",
    e.deferred = "deferred",
    e.redirect = "redirect",
    e.error = "error"
}
)(Kh || (Kh = {}));
function uk(e, t, n) {
    return n === void 0 && (n = "/"),
    dk(e, t, n, !1)
}
function dk(e, t, n, r) {
    let o = typeof t == "string" ? gs(t) : t
      , s = _f(o.pathname || "/", n);
    if (s == null)
        return null;
    let i = yx(e);
    fk(i);
    let l = null;
    for (let c = 0; l == null && c < i.length; ++c) {
        let u = Sk(s);
        l = bk(i[c], u, r)
    }
    return l
}
function yx(e, t, n, r) {
    t === void 0 && (t = []),
    n === void 0 && (n = []),
    r === void 0 && (r = "");
    let o = (s, i, l) => {
        let c = {
            relativePath: l === void 0 ? s.path || "" : l,
            caseSensitive: s.caseSensitive === !0,
            childrenIndex: i,
            route: s
        };
        c.relativePath.startsWith("/") && (Ie(c.relativePath.startsWith(r), 'Absolute route path "' + c.relativePath + '" nested under path ' + ('"' + r + '" is not valid. An absolute child route path ') + "must start with the combined path of all its parent routes."),
        c.relativePath = c.relativePath.slice(r.length));
        let u = gr([r, c.relativePath])
          , d = n.concat(c);
        s.children && s.children.length > 0 && (Ie(s.index !== !0, "Index routes must not have child routes. Please remove " + ('all child routes from route path "' + u + '".')),
        yx(s.children, t, d, u)),
        !(s.path == null && !s.index) && t.push({
            path: u,
            score: xk(u, s.index),
            routesMeta: d
        })
    }
    ;
    return e.forEach( (s, i) => {
        var l;
        if (s.path === "" || !((l = s.path) != null && l.includes("?")))
            o(s, i);
        else
            for (let c of xx(s.path))
                o(s, i, c)
    }
    ),
    t
}
function xx(e) {
    let t = e.split("/");
    if (t.length === 0)
        return [];
    let[n,...r] = t
      , o = n.endsWith("?")
      , s = n.replace(/\?$/, "");
    if (r.length === 0)
        return o ? [s, ""] : [s];
    let i = xx(r.join("/"))
      , l = [];
    return l.push(...i.map(c => c === "" ? s : [s, c].join("/"))),
    o && l.push(...i),
    l.map(c => e.startsWith("/") && c === "" ? "/" : c)
}
function fk(e) {
    e.sort( (t, n) => t.score !== n.score ? n.score - t.score : wk(t.routesMeta.map(r => r.childrenIndex), n.routesMeta.map(r => r.childrenIndex)))
}
const mk = /^:[\w-]+$/
  , hk = 3
  , pk = 2
  , vk = 1
  , gk = 10
  , yk = -2
  , Qh = e => e === "*";
function xk(e, t) {
    let n = e.split("/")
      , r = n.length;
    return n.some(Qh) && (r += yk),
    t && (r += pk),
    n.filter(o => !Qh(o)).reduce( (o, s) => o + (mk.test(s) ? hk : s === "" ? vk : gk), r)
}
function wk(e, t) {
    return e.length === t.length && e.slice(0, -1).every( (r, o) => r === t[o]) ? e[e.length - 1] - t[t.length - 1] : 0
}
function bk(e, t, n) {
    let {routesMeta: r} = e
      , o = {}
      , s = "/"
      , i = [];
    for (let l = 0; l < r.length; ++l) {
        let c = r[l]
          , u = l === r.length - 1
          , d = s === "/" ? t : t.slice(s.length) || "/"
          , f = Gh({
            path: c.relativePath,
            caseSensitive: c.caseSensitive,
            end: u
        }, d)
          , g = c.route;
        if (!f && u && n && !r[r.length - 1].route.index && (f = Gh({
            path: c.relativePath,
            caseSensitive: c.caseSensitive,
            end: !1
        }, d)),
        !f)
            return null;
        Object.assign(o, f.params),
        i.push({
            params: o,
            pathname: gr([s, f.pathname]),
            pathnameBase: Ek(gr([s, f.pathnameBase])),
            route: g
        }),
        f.pathnameBase !== "/" && (s = gr([s, f.pathnameBase]))
    }
    return i
}
function Gh(e, t) {
    typeof e == "string" && (e = {
        path: e,
        caseSensitive: !1,
        end: !0
    });
    let[n,r] = Nk(e.path, e.caseSensitive, e.end)
      , o = t.match(n);
    if (!o)
        return null;
    let s = o[0]
      , i = s.replace(/(.)\/+$/, "$1")
      , l = o.slice(1);
    return {
        params: r.reduce( (u, d, f) => {
            let {paramName: g, isOptional: h} = d;
            if (g === "*") {
                let v = l[f] || "";
                i = s.slice(0, s.length - v.length).replace(/(.)\/+$/, "$1")
            }
            const b = l[f];
            return h && !b ? u[g] = void 0 : u[g] = (b || "").replace(/%2F/g, "/"),
            u
        }
        , {}),
        pathname: s,
        pathnameBase: i,
        pattern: e
    }
}
function Nk(e, t, n) {
    t === void 0 && (t = !1),
    n === void 0 && (n = !0),
    gx(e === "*" || !e.endsWith("*") || e.endsWith("/*"), 'Route path "' + e + '" will be treated as if it were ' + ('"' + e.replace(/\*$/, "/*") + '" because the `*` character must ') + "always follow a `/` in the pattern. To get rid of this warning, " + ('please change the route path to "' + e.replace(/\*$/, "/*") + '".'));
    let r = []
      , o = "^" + e.replace(/\/*\*?$/, "").replace(/^\/*/, "/").replace(/[\\.*+^${}|()[\]]/g, "\\$&").replace(/\/:([\w-]+)(\?)?/g, (i, l, c) => (r.push({
        paramName: l,
        isOptional: c != null
    }),
    c ? "/?([^\\/]+)?" : "/([^\\/]+)"));
    return e.endsWith("*") ? (r.push({
        paramName: "*"
    }),
    o += e === "*" || e === "/*" ? "(.*)$" : "(?:\\/(.+)|\\/*)$") : n ? o += "\\/*$" : e !== "" && e !== "/" && (o += "(?:(?=\\/|$))"),
    [new RegExp(o,t ? void 0 : "i"), r]
}
function Sk(e) {
    try {
        return e.split("/").map(t => decodeURIComponent(t).replace(/\//g, "%2F")).join("/")
    } catch (t) {
        return gx(!1, 'The URL path "' + e + '" could not be decoded because it is is a malformed URL segment. This is probably due to a bad percent ' + ("encoding (" + t + ").")),
        e
    }
}
function _f(e, t) {
    if (t === "/")
        return e;
    if (!e.toLowerCase().startsWith(t.toLowerCase()))
        return null;
    let n = t.endsWith("/") ? t.length - 1 : t.length
      , r = e.charAt(n);
    return r && r !== "/" ? null : e.slice(n) || "/"
}
function jk(e, t) {
    t === void 0 && (t = "/");
    let {pathname: n, search: r="", hash: o=""} = typeof e == "string" ? gs(e) : e;
    return {
        pathname: n ? n.startsWith("/") ? n : Ck(n, t) : t,
        search: Pk(r),
        hash: Tk(o)
    }
}
function Ck(e, t) {
    let n = t.replace(/\/+$/, "").split("/");
    return e.split("/").forEach(o => {
        o === ".." ? n.length > 1 && n.pop() : o !== "." && n.push(o)
    }
    ),
    n.length > 1 ? n.join("/") : "/"
}
function Dc(e, t, n, r) {
    return "Cannot include a '" + e + "' character in a manually specified " + ("`to." + t + "` field [" + JSON.stringify(r) + "].  Please separate it out to the ") + ("`to." + n + "` field. Alternatively you may provide the full path as ") + 'a string in <Link to="..."> and the router will parse it for you.'
}
function kk(e) {
    return e.filter( (t, n) => n === 0 || t.route.path && t.route.path.length > 0)
}
function wx(e, t) {
    let n = kk(e);
    return t ? n.map( (r, o) => o === n.length - 1 ? r.pathname : r.pathnameBase) : n.map(r => r.pathnameBase)
}
function bx(e, t, n, r) {
    r === void 0 && (r = !1);
    let o;
    typeof e == "string" ? o = gs(e) : (o = xa({}, e),
    Ie(!o.pathname || !o.pathname.includes("?"), Dc("?", "pathname", "search", o)),
    Ie(!o.pathname || !o.pathname.includes("#"), Dc("#", "pathname", "hash", o)),
    Ie(!o.search || !o.search.includes("#"), Dc("#", "search", "hash", o)));
    let s = e === "" || o.pathname === "", i = s ? "/" : o.pathname, l;
    if (i == null)
        l = n;
    else {
        let f = t.length - 1;
        if (!r && i.startsWith("..")) {
            let g = i.split("/");
            for (; g[0] === ".."; )
                g.shift(),
                f -= 1;
            o.pathname = g.join("/")
        }
        l = f >= 0 ? t[f] : "/"
    }
    let c = jk(o, l)
      , u = i && i !== "/" && i.endsWith("/")
      , d = (s || i === ".") && n.endsWith("/");
    return !c.pathname.endsWith("/") && (u || d) && (c.pathname += "/"),
    c
}
const gr = e => e.join("/").replace(/\/\/+/g, "/")
  , Ek = e => e.replace(/\/+$/, "").replace(/^\/*/, "/")
  , Pk = e => !e || e === "?" ? "" : e.startsWith("?") ? e : "?" + e
  , Tk = e => !e || e === "#" ? "" : e.startsWith("#") ? e : "#" + e;
function Mk(e) {
    return e != null && typeof e.status == "number" && typeof e.statusText == "string" && typeof e.internal == "boolean" && "data"in e
}
const Nx = ["post", "put", "patch", "delete"];
new Set(Nx);
const Rk = ["get", ...Nx];
new Set(Rk);
/**
 * React Router v6.30.1
 *
 * Copyright (c) Remix Software Inc.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE.md file in the root directory of this source tree.
 *
 * @license MIT
 */
function wa() {
    return wa = Object.assign ? Object.assign.bind() : function(e) {
        for (var t = 1; t < arguments.length; t++) {
            var n = arguments[t];
            for (var r in n)
                Object.prototype.hasOwnProperty.call(n, r) && (e[r] = n[r])
        }
        return e
    }
    ,
    wa.apply(this, arguments)
}
const Df = m.createContext(null)
  , _k = m.createContext(null)
  , lo = m.createContext(null)
  , Hl = m.createContext(null)
  , kr = m.createContext({
    outlet: null,
    matches: [],
    isDataRoute: !1
})
  , Sx = m.createContext(null);
function Dk(e, t) {
    let {relative: n} = t === void 0 ? {} : t;
    Da() || Ie(!1);
    let {basename: r, navigator: o} = m.useContext(lo)
      , {hash: s, pathname: i, search: l} = Cx(e, {
        relative: n
    })
      , c = i;
    return r !== "/" && (c = i === "/" ? r : gr([r, i])),
    o.createHref({
        pathname: c,
        search: l,
        hash: s
    })
}
function Da() {
    return m.useContext(Hl) != null
}
function ys() {
    return Da() || Ie(!1),
    m.useContext(Hl).location
}
function jx(e) {
    m.useContext(lo).static || m.useLayoutEffect(e)
}
function Ok() {
    let {isDataRoute: e} = m.useContext(kr);
    return e ? Qk() : Ak()
}
function Ak() {
    Da() || Ie(!1);
    let e = m.useContext(Df)
      , {basename: t, future: n, navigator: r} = m.useContext(lo)
      , {matches: o} = m.useContext(kr)
      , {pathname: s} = ys()
      , i = JSON.stringify(wx(o, n.v7_relativeSplatPath))
      , l = m.useRef(!1);
    return jx( () => {
        l.current = !0
    }
    ),
    m.useCallback(function(u, d) {
        if (d === void 0 && (d = {}),
        !l.current)
            return;
        if (typeof u == "number") {
            r.go(u);
            return
        }
        let f = bx(u, JSON.parse(i), s, d.relative === "path");
        e == null && t !== "/" && (f.pathname = f.pathname === "/" ? t : gr([t, f.pathname])),
        (d.replace ? r.replace : r.push)(f, d.state, d)
    }, [t, r, i, s, e])
}
function Ik() {
    let {matches: e} = m.useContext(kr)
      , t = e[e.length - 1];
    return t ? t.params : {}
}
function Cx(e, t) {
    let {relative: n} = t === void 0 ? {} : t
      , {future: r} = m.useContext(lo)
      , {matches: o} = m.useContext(kr)
      , {pathname: s} = ys()
      , i = JSON.stringify(wx(o, r.v7_relativeSplatPath));
    return m.useMemo( () => bx(e, JSON.parse(i), s, n === "path"), [e, i, s, n])
}
function Lk(e, t) {
    return Fk(e, t)
}
function Fk(e, t, n, r) {
    Da() || Ie(!1);
    let {navigator: o} = m.useContext(lo)
      , {matches: s} = m.useContext(kr)
      , i = s[s.length - 1]
      , l = i ? i.params : {};
    i && i.pathname;
    let c = i ? i.pathnameBase : "/";
    i && i.route;
    let u = ys(), d;
    if (t) {
        var f;
        let w = typeof t == "string" ? gs(t) : t;
        c === "/" || (f = w.pathname) != null && f.startsWith(c) || Ie(!1),
        d = w
    } else
        d = u;
    let g = d.pathname || "/"
      , h = g;
    if (c !== "/") {
        let w = c.replace(/^\//, "").split("/");
        h = "/" + g.replace(/^\//, "").split("/").slice(w.length).join("/")
    }
    let b = uk(e, {
        pathname: h
    })
      , v = Hk(b && b.map(w => Object.assign({}, w, {
        params: Object.assign({}, l, w.params),
        pathname: gr([c, o.encodeLocation ? o.encodeLocation(w.pathname).pathname : w.pathname]),
        pathnameBase: w.pathnameBase === "/" ? c : gr([c, o.encodeLocation ? o.encodeLocation(w.pathnameBase).pathname : w.pathnameBase])
    })), s, n, r);
    return t && v ? m.createElement(Hl.Provider, {
        value: {
            location: wa({
                pathname: "/",
                search: "",
                hash: "",
                state: null,
                key: "default"
            }, d),
            navigationType: lr.Pop
        }
    }, v) : v
}
function zk() {
    let e = Kk()
      , t = Mk(e) ? e.status + " " + e.statusText : e instanceof Error ? e.message : JSON.stringify(e)
      , n = e instanceof Error ? e.stack : null
      , o = {
        padding: "0.5rem",
        backgroundColor: "rgba(200,200,200, 0.5)"
    };
    return m.createElement(m.Fragment, null, m.createElement("h2", null, "Unexpected Application Error!"), m.createElement("h3", {
        style: {
            fontStyle: "italic"
        }
    }, t), n ? m.createElement("pre", {
        style: o
    }, n) : null, null)
}
const $k = m.createElement(zk, null);
class Bk extends m.Component {
    constructor(t) {
        super(t),
        this.state = {
            location: t.location,
            revalidation: t.revalidation,
            error: t.error
        }
    }
    static getDerivedStateFromError(t) {
        return {
            error: t
        }
    }
    static getDerivedStateFromProps(t, n) {
        return n.location !== t.location || n.revalidation !== "idle" && t.revalidation === "idle" ? {
            error: t.error,
            location: t.location,
            revalidation: t.revalidation
        } : {
            error: t.error !== void 0 ? t.error : n.error,
            location: n.location,
            revalidation: t.revalidation || n.revalidation
        }
    }
    componentDidCatch(t, n) {
        console.error("React Router caught the following error during render", t, n)
    }
    render() {
        return this.state.error !== void 0 ? m.createElement(kr.Provider, {
            value: this.props.routeContext
        }, m.createElement(Sx.Provider, {
            value: this.state.error,
            children: this.props.component
        })) : this.props.children
    }
}
function Wk(e) {
    let {routeContext: t, match: n, children: r} = e
      , o = m.useContext(Df);
    return o && o.static && o.staticContext && (n.route.errorElement || n.route.ErrorBoundary) && (o.staticContext._deepestRenderedBoundaryId = n.route.id),
    m.createElement(kr.Provider, {
        value: t
    }, r)
}
function Hk(e, t, n, r) {
    var o;
    if (t === void 0 && (t = []),
    n === void 0 && (n = null),
    r === void 0 && (r = null),
    e == null) {
        var s;
        if (!n)
            return null;
        if (n.errors)
            e = n.matches;
        else if ((s = r) != null && s.v7_partialHydration && t.length === 0 && !n.initialized && n.matches.length > 0)
            e = n.matches;
        else
            return null
    }
    let i = e
      , l = (o = n) == null ? void 0 : o.errors;
    if (l != null) {
        let d = i.findIndex(f => f.route.id && (l == null ? void 0 : l[f.route.id]) !== void 0);
        d >= 0 || Ie(!1),
        i = i.slice(0, Math.min(i.length, d + 1))
    }
    let c = !1
      , u = -1;
    if (n && r && r.v7_partialHydration)
        for (let d = 0; d < i.length; d++) {
            let f = i[d];
            if ((f.route.HydrateFallback || f.route.hydrateFallbackElement) && (u = d),
            f.route.id) {
                let {loaderData: g, errors: h} = n
                  , b = f.route.loader && g[f.route.id] === void 0 && (!h || h[f.route.id] === void 0);
                if (f.route.lazy || b) {
                    c = !0,
                    u >= 0 ? i = i.slice(0, u + 1) : i = [i[0]];
                    break
                }
            }
        }
    return i.reduceRight( (d, f, g) => {
        let h, b = !1, v = null, w = null;
        n && (h = l && f.route.id ? l[f.route.id] : void 0,
        v = f.route.errorElement || $k,
        c && (u < 0 && g === 0 ? (b = !0,
        w = null) : u === g && (b = !0,
        w = f.route.hydrateFallbackElement || null)));
        let y = t.concat(i.slice(0, g + 1))
          , p = () => {
            let x;
            return h ? x = v : b ? x = w : f.route.Component ? x = m.createElement(f.route.Component, null) : f.route.element ? x = f.route.element : x = d,
            m.createElement(Wk, {
                match: f,
                routeContext: {
                    outlet: d,
                    matches: y,
                    isDataRoute: n != null
                },
                children: x
            })
        }
        ;
        return n && (f.route.ErrorBoundary || f.route.errorElement || g === 0) ? m.createElement(Bk, {
            location: n.location,
            revalidation: n.revalidation,
            component: v,
            error: h,
            children: p(),
            routeContext: {
                outlet: null,
                matches: y,
                isDataRoute: !0
            }
        }) : p()
    }
    , null)
}
var kx = function(e) {
    return e.UseBlocker = "useBlocker",
    e.UseRevalidator = "useRevalidator",
    e.UseNavigateStable = "useNavigate",
    e
}(kx || {})
  , cl = function(e) {
    return e.UseBlocker = "useBlocker",
    e.UseLoaderData = "useLoaderData",
    e.UseActionData = "useActionData",
    e.UseRouteError = "useRouteError",
    e.UseNavigation = "useNavigation",
    e.UseRouteLoaderData = "useRouteLoaderData",
    e.UseMatches = "useMatches",
    e.UseRevalidator = "useRevalidator",
    e.UseNavigateStable = "useNavigate",
    e.UseRouteId = "useRouteId",
    e
}(cl || {});
function Vk(e) {
    let t = m.useContext(Df);
    return t || Ie(!1),
    t
}
function Uk(e) {
    let t = m.useContext(_k);
    return t || Ie(!1),
    t
}
function Yk(e) {
    let t = m.useContext(kr);
    return t || Ie(!1),
    t
}
function Ex(e) {
    let t = Yk()
      , n = t.matches[t.matches.length - 1];
    return n.route.id || Ie(!1),
    n.route.id
}
function Kk() {
    var e;
    let t = m.useContext(Sx)
      , n = Uk(cl.UseRouteError)
      , r = Ex(cl.UseRouteError);
    return t !== void 0 ? t : (e = n.errors) == null ? void 0 : e[r]
}
function Qk() {
    let {router: e} = Vk(kx.UseNavigateStable)
      , t = Ex(cl.UseNavigateStable)
      , n = m.useRef(!1);
    return jx( () => {
        n.current = !0
    }
    ),
    m.useCallback(function(o, s) {
        s === void 0 && (s = {}),
        n.current && (typeof o == "number" ? e.navigate(o) : e.navigate(o, wa({
            fromRouteId: t
        }, s)))
    }, [e, t])
}
function Gk(e, t) {
    e == null || e.v7_startTransition,
    e == null || e.v7_relativeSplatPath
}
function Cn(e) {
    Ie(!1)
}
function qk(e) {
    let {basename: t="/", children: n=null, location: r, navigationType: o=lr.Pop, navigator: s, static: i=!1, future: l} = e;
    Da() && Ie(!1);
    let c = t.replace(/^\/*/, "/")
      , u = m.useMemo( () => ({
        basename: c,
        navigator: s,
        static: i,
        future: wa({
            v7_relativeSplatPath: !1
        }, l)
    }), [c, l, s, i]);
    typeof r == "string" && (r = gs(r));
    let {pathname: d="/", search: f="", hash: g="", state: h=null, key: b="default"} = r
      , v = m.useMemo( () => {
        let w = _f(d, c);
        return w == null ? null : {
            location: {
                pathname: w,
                search: f,
                hash: g,
                state: h,
                key: b
            },
            navigationType: o
        }
    }
    , [c, d, f, g, h, b, o]);
    return v == null ? null : m.createElement(lo.Provider, {
        value: u
    }, m.createElement(Hl.Provider, {
        children: n,
        value: v
    }))
}
function Xk(e) {
    let {children: t, location: n} = e;
    return Lk(rd(t), n)
}
new Promise( () => {}
);
function rd(e, t) {
    t === void 0 && (t = []);
    let n = [];
    return m.Children.forEach(e, (r, o) => {
        if (!m.isValidElement(r))
            return;
        let s = [...t, o];
        if (r.type === m.Fragment) {
            n.push.apply(n, rd(r.props.children, s));
            return
        }
        r.type !== Cn && Ie(!1),
        !r.props.index || !r.props.children || Ie(!1);
        let i = {
            id: r.props.id || s.join("-"),
            caseSensitive: r.props.caseSensitive,
            element: r.props.element,
            Component: r.props.Component,
            index: r.props.index,
            path: r.props.path,
            loader: r.props.loader,
            action: r.props.action,
            errorElement: r.props.errorElement,
            ErrorBoundary: r.props.ErrorBoundary,
            hasErrorBoundary: r.props.ErrorBoundary != null || r.props.errorElement != null,
            shouldRevalidate: r.props.shouldRevalidate,
            handle: r.props.handle,
            lazy: r.props.lazy
        };
        r.props.children && (i.children = rd(r.props.children, s)),
        n.push(i)
    }
    ),
    n
}
/**
 * React Router DOM v6.30.1
 *
 * Copyright (c) Remix Software Inc.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE.md file in the root directory of this source tree.
 *
 * @license MIT
 */
function od() {
    return od = Object.assign ? Object.assign.bind() : function(e) {
        for (var t = 1; t < arguments.length; t++) {
            var n = arguments[t];
            for (var r in n)
                Object.prototype.hasOwnProperty.call(n, r) && (e[r] = n[r])
        }
        return e
    }
    ,
    od.apply(this, arguments)
}
function Jk(e, t) {
    if (e == null)
        return {};
    var n = {}, r = Object.keys(e), o, s;
    for (s = 0; s < r.length; s++)
        o = r[s],
        !(t.indexOf(o) >= 0) && (n[o] = e[o]);
    return n
}
function Zk(e) {
    return !!(e.metaKey || e.altKey || e.ctrlKey || e.shiftKey)
}
function eE(e, t) {
    return e.button === 0 && (!t || t === "_self") && !Zk(e)
}
const tE = ["onClick", "relative", "reloadDocument", "replace", "state", "target", "to", "preventScrollReset", "viewTransition"]
  , nE = "6";
try {
    window.__reactRouterVersion = nE
} catch {}
const rE = "startTransition"
  , qh = bd[rE];
function oE(e) {
    let {basename: t, children: n, future: r, window: o} = e
      , s = m.useRef();
    s.current == null && (s.current = ik({
        window: o,
        v5Compat: !0
    }));
    let i = s.current
      , [l,c] = m.useState({
        action: i.action,
        location: i.location
    })
      , {v7_startTransition: u} = r || {}
      , d = m.useCallback(f => {
        u && qh ? qh( () => c(f)) : c(f)
    }
    , [c, u]);
    return m.useLayoutEffect( () => i.listen(d), [i, d]),
    m.useEffect( () => Gk(r), [r]),
    m.createElement(qk, {
        basename: t,
        children: n,
        location: l.location,
        navigationType: l.action,
        navigator: i,
        future: r
    })
}
const sE = typeof window < "u" && typeof window.document < "u" && typeof window.document.createElement < "u"
  , aE = /^(?:[a-z][a-z0-9+.-]*:|\/\/)/i
  , Fe = m.forwardRef(function(t, n) {
    let {onClick: r, relative: o, reloadDocument: s, replace: i, state: l, target: c, to: u, preventScrollReset: d, viewTransition: f} = t, g = Jk(t, tE), {basename: h} = m.useContext(lo), b, v = !1;
    if (typeof u == "string" && aE.test(u) && (b = u,
    sE))
        try {
            let x = new URL(window.location.href)
              , N = u.startsWith("//") ? new URL(x.protocol + u) : new URL(u)
              , S = _f(N.pathname, h);
            N.origin === x.origin && S != null ? u = S + N.search + N.hash : v = !0
        } catch {}
    let w = Dk(u, {
        relative: o
    })
      , y = iE(u, {
        replace: i,
        state: l,
        target: c,
        preventScrollReset: d,
        relative: o,
        viewTransition: f
    });
    function p(x) {
        r && r(x),
        x.defaultPrevented || y(x)
    }
    return m.createElement("a", od({}, g, {
        href: b || w,
        onClick: v || s ? r : p,
        ref: n,
        target: c
    }))
});
var Xh;
(function(e) {
    e.UseScrollRestoration = "useScrollRestoration",
    e.UseSubmit = "useSubmit",
    e.UseSubmitFetcher = "useSubmitFetcher",
    e.UseFetcher = "useFetcher",
    e.useViewTransitionState = "useViewTransitionState"
}
)(Xh || (Xh = {}));
var Jh;
(function(e) {
    e.UseFetcher = "useFetcher",
    e.UseFetchers = "useFetchers",
    e.UseScrollRestoration = "useScrollRestoration"
}
)(Jh || (Jh = {}));
function iE(e, t) {
    let {target: n, replace: r, state: o, preventScrollReset: s, relative: i, viewTransition: l} = t === void 0 ? {} : t
      , c = Ok()
      , u = ys()
      , d = Cx(e, {
        relative: i
    });
    return m.useCallback(f => {
        if (eE(f, n)) {
            f.preventDefault();
            let g = r !== void 0 ? r : ll(u) === ll(d);
            c(e, {
                replace: g,
                state: o,
                preventScrollReset: s,
                relative: i,
                viewTransition: l
            })
        }
    }
    , [u, c, d, r, o, n, e, s, i, l])
}
const sd = Ol("inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0", {
    variants: {
        variant: {
            default: "bg-primary text-primary-foreground hover:bg-primary/90",
            destructive: "bg-destructive text-destructive-foreground hover:bg-destructive/90",
            outline: "border border-input bg-background hover:bg-accent hover:text-accent-foreground",
            secondary: "bg-secondary text-secondary-foreground hover:bg-secondary/80",
            ghost: "hover:bg-accent hover:text-accent-foreground",
            link: "text-primary underline-offset-4 hover:underline"
        },
        size: {
            default: "h-10 px-4 py-2",
            sm: "h-9 rounded-md px-3",
            lg: "h-11 rounded-md px-8",
            icon: "h-10 w-10"
        }
    },
    defaultVariants: {
        variant: "default",
        size: "default"
    }
})
  , ae = m.forwardRef( ({className: e, variant: t, size: n, asChild: r=!1, ...o}, s) => {
    const i = r ? SN : "button";
    return a.jsx(i, {
        className: re(sd({
            variant: t,
            size: n,
            className: e
        })),
        ref: s,
        ...o
    })
}
);
ae.displayName = "Button";
const lE = () => {
    const [e,t] = m.useState(!1)
      , n = ys()
      , r = [{
        name: "Home",
        path: "/",
        icon: gf
    }, {
        name: "Buy / Lease",
        path: "/buy-lease",
        icon: Vu
    }, {
        name: "Sell & Evaluate",
        path: "/sell-evaluate",
        icon: xy
    }, {
        name: "Blog",
        path: "/blog",
        icon: yS
    }, {
        name: "Open House",
        path: "/open-house",
        icon: Jr
    }, {
        name: "Mortgage Calculator",
        path: "/mortgage-calculator",
        icon: Uu
    }]
      , o = s => n.pathname === s;
    return a.jsx("nav", {
        className: "bg-background/95 backdrop-blur-sm border-b shadow-soft sticky top-0 z-50",
        children: a.jsxs("div", {
            className: "max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
            children: [a.jsxs("div", {
                className: "flex justify-between items-center h-16",
                children: [a.jsxs(Fe, {
                    to: "/",
                    className: "flex items-center space-x-2",
                    children: [a.jsx("div", {
                        className: "w-8 h-8 bg-accent-gradient rounded-lg flex items-center justify-center",
                        children: a.jsx(Vu, {
                            className: "h-5 w-5 text-primary"
                        })
                    }), a.jsx("span", {
                        className: "text-xl font-bold text-primary",
                        children: "RealtyPro"
                    })]
                }), a.jsx("div", {
                    className: "hidden md:flex items-center space-x-1",
                    children: r.map(s => {
                        const i = s.icon;
                        return a.jsxs(Fe, {
                            to: s.path,
                            className: `px-4 py-2 rounded-lg text-sm font-medium transition-all duration-200 flex items-center space-x-2 ${o(s.path) ? "bg-primary text-primary-foreground shadow-medium" : "text-muted-foreground hover:text-primary hover:bg-secondary"}`,
                            children: [a.jsx(i, {
                                className: "h-4 w-4"
                            }), a.jsx("span", {
                                children: s.name
                            })]
                        }, s.path)
                    }
                    )
                }), a.jsx("div", {
                    className: "hidden md:block",
                    children: a.jsx(ae, {
                        variant: "default",
                        size: "sm",
                        className: "bg-accent-gradient hover:shadow-accent text-primary font-semibold",
                        children: "Get Started"
                    })
                }), a.jsx("div", {
                    className: "md:hidden",
                    children: a.jsx(ae, {
                        variant: "ghost",
                        size: "sm",
                        onClick: () => t(!e),
                        className: "text-primary",
                        children: e ? a.jsx(yf, {
                            className: "h-5 w-5"
                        }) : a.jsx(TS, {
                            className: "h-5 w-5"
                        })
                    })
                })]
            }), e && a.jsx("div", {
                className: "md:hidden absolute left-0 right-0 top-16 bg-background border-b shadow-medium animate-slide-up",
                children: a.jsxs("div", {
                    className: "px-4 py-4 space-y-2",
                    children: [r.map(s => {
                        const i = s.icon;
                        return a.jsxs(Fe, {
                            to: s.path,
                            onClick: () => t(!1),
                            className: `block px-4 py-3 rounded-lg text-base font-medium transition-all duration-200 flex items-center space-x-3 ${o(s.path) ? "bg-primary text-primary-foreground shadow-medium" : "text-muted-foreground hover:text-primary hover:bg-secondary"}`,
                            children: [a.jsx(i, {
                                className: "h-5 w-5"
                            }), a.jsx("span", {
                                children: s.name
                            })]
                        }, s.path)
                    }
                    ), a.jsx("div", {
                        className: "pt-4",
                        children: a.jsx(ae, {
                            variant: "default",
                            className: "w-full bg-accent-gradient hover:shadow-accent text-primary font-semibold",
                            children: "Get Started"
                        })
                    })]
                })
            })]
        })
    })
}
  , cE = () => a.jsx("footer", {
    className: "bg-primary text-primary-foreground",
    children: a.jsxs("div", {
        className: "max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12",
        children: [a.jsxs("div", {
            className: "grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8",
            children: [a.jsxs("div", {
                className: "space-y-4",
                children: [a.jsxs("div", {
                    className: "flex items-center space-x-2",
                    children: [a.jsx("div", {
                        className: "w-8 h-8 bg-accent-gradient rounded-lg flex items-center justify-center",
                        children: a.jsx(Vu, {
                            className: "h-5 w-5 text-primary"
                        })
                    }), a.jsx("span", {
                        className: "text-xl font-bold",
                        children: "RealtyPro"
                    })]
                }), a.jsx("p", {
                    className: "text-primary-foreground/80 text-sm leading-relaxed",
                    children: "Your trusted partner in finding the perfect property. We leverage AI-powered insights to deliver exceptional real estate experiences."
                }), a.jsxs("div", {
                    className: "flex space-x-4",
                    children: [a.jsx(jS, {
                        className: "h-5 w-5 text-primary-foreground/60 hover:text-accent cursor-pointer transition-colors"
                    }), a.jsx(OS, {
                        className: "h-5 w-5 text-primary-foreground/60 hover:text-accent cursor-pointer transition-colors"
                    }), a.jsx(ES, {
                        className: "h-5 w-5 text-primary-foreground/60 hover:text-accent cursor-pointer transition-colors"
                    }), a.jsx(PS, {
                        className: "h-5 w-5 text-primary-foreground/60 hover:text-accent cursor-pointer transition-colors"
                    })]
                })]
            }), a.jsxs("div", {
                className: "space-y-4",
                children: [a.jsx("h3", {
                    className: "text-lg font-semibold",
                    children: "Quick Links"
                }), a.jsxs("div", {
                    className: "space-y-2",
                    children: [a.jsx(Fe, {
                        to: "/buy-lease",
                        className: "block text-primary-foreground/80 hover:text-accent transition-colors text-sm",
                        children: "Buy / Lease Properties"
                    }), a.jsx(Fe, {
                        to: "/sell-evaluate",
                        className: "block text-primary-foreground/80 hover:text-accent transition-colors text-sm",
                        children: "Sell & Evaluate"
                    }), a.jsx(Fe, {
                        to: "/open-house",
                        className: "block text-primary-foreground/80 hover:text-accent transition-colors text-sm",
                        children: "Open Houses"
                    }), a.jsx(Fe, {
                        to: "/mortgage-calculator",
                        className: "block text-primary-foreground/80 hover:text-accent transition-colors text-sm",
                        children: "Mortgage Calculator"
                    })]
                })]
            }), a.jsxs("div", {
                className: "space-y-4",
                children: [a.jsx("h3", {
                    className: "text-lg font-semibold",
                    children: "Services"
                }), a.jsxs("div", {
                    className: "space-y-2 text-sm text-primary-foreground/80",
                    children: [a.jsx("p", {
                        children: "Property Evaluation"
                    }), a.jsx("p", {
                        children: "Market Analysis"
                    }), a.jsx("p", {
                        children: "Investment Consulting"
                    }), a.jsx("p", {
                        children: "Property Management"
                    }), a.jsx("p", {
                        children: "Home Staging"
                    })]
                })]
            }), a.jsxs("div", {
                className: "space-y-4",
                children: [a.jsx("h3", {
                    className: "text-lg font-semibold",
                    children: "Contact Us"
                }), a.jsxs("div", {
                    className: "space-y-3",
                    children: [a.jsxs("div", {
                        className: "flex items-center space-x-3",
                        children: [a.jsx(as, {
                            className: "h-4 w-4 text-accent"
                        }), a.jsx("span", {
                            className: "text-sm text-primary-foreground/80",
                            children: "(555) 123-4567"
                        })]
                    }), a.jsxs("div", {
                        className: "flex items-center space-x-3",
                        children: [a.jsx(ss, {
                            className: "h-4 w-4 text-accent"
                        }), a.jsx("span", {
                            className: "text-sm text-primary-foreground/80",
                            children: "info@realtypro.com"
                        })]
                    }), a.jsxs("div", {
                        className: "flex items-start space-x-3",
                        children: [a.jsx(Ra, {
                            className: "h-4 w-4 text-accent mt-0.5"
                        }), a.jsxs("span", {
                            className: "text-sm text-primary-foreground/80",
                            children: ["123 Real Estate Ave", a.jsx("br", {}), "Downtown District, NY 10001"]
                        })]
                    })]
                })]
            })]
        }), a.jsx("div", {
            className: "border-t border-primary-foreground/20 mt-8 pt-8",
            children: a.jsxs("div", {
                className: "flex flex-col md:flex-row justify-between items-center space-y-4 md:space-y-0",
                children: [a.jsx("p", {
                    className: "text-sm text-primary-foreground/60",
                    children: "© 2024 RealtyPro. All rights reserved."
                }), a.jsxs("div", {
                    className: "flex space-x-6 text-sm text-primary-foreground/60",
                    children: [a.jsx(Fe, {
                        to: "/privacy",
                        className: "hover:text-accent transition-colors",
                        children: "Privacy Policy"
                    }), a.jsx(Fe, {
                        to: "/terms",
                        className: "hover:text-accent transition-colors",
                        children: "Terms of Service"
                    }), a.jsx(Fe, {
                        to: "/contact",
                        className: "hover:text-accent transition-colors",
                        children: "Contact"
                    })]
                })]
            })
        })]
    })
})
  , Ce = m.forwardRef( ({className: e, ...t}, n) => a.jsx("div", {
    ref: n,
    className: re("rounded-lg border bg-card text-card-foreground shadow-sm", e),
    ...t
}));
Ce.displayName = "Card";
const uE = m.forwardRef( ({className: e, ...t}, n) => a.jsx("div", {
    ref: n,
    className: re("flex flex-col space-y-1.5 p-6", e),
    ...t
}));
uE.displayName = "CardHeader";
const dE = m.forwardRef( ({className: e, ...t}, n) => a.jsx("h3", {
    ref: n,
    className: re("text-2xl font-semibold leading-none tracking-tight", e),
    ...t
}));
dE.displayName = "CardTitle";
const fE = m.forwardRef( ({className: e, ...t}, n) => a.jsx("p", {
    ref: n,
    className: re("text-sm text-muted-foreground", e),
    ...t
}));
fE.displayName = "CardDescription";
const mE = m.forwardRef( ({className: e, ...t}, n) => a.jsx("div", {
    ref: n,
    className: re("p-6 pt-0", e),
    ...t
}));
mE.displayName = "CardContent";
const hE = m.forwardRef( ({className: e, ...t}, n) => a.jsx("div", {
    ref: n,
    className: re("flex items-center p-6 pt-0", e),
    ...t
}));
hE.displayName = "CardFooter";
const pE = Ol("inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2", {
    variants: {
        variant: {
            default: "border-transparent bg-primary text-primary-foreground hover:bg-primary/80",
            secondary: "border-transparent bg-secondary text-secondary-foreground hover:bg-secondary/80",
            destructive: "border-transparent bg-destructive text-destructive-foreground hover:bg-destructive/80",
            outline: "text-foreground"
        }
    },
    defaultVariants: {
        variant: "default"
    }
});
function rt({className: e, variant: t, ...n}) {
    return a.jsx("div", {
        className: re(pE({
            variant: t
        }), e),
        ...n
    })
}
const Px = ({property: e, onViewDetails: t}) => a.jsxs(Ce, {
    className: "group overflow-hidden shadow-soft hover:shadow-medium transition-all duration-300 animate-fade-in",
    children: [a.jsxs("div", {
        className: "relative overflow-hidden",
        children: [a.jsx("img", {
            src: e.image,
            alt: e.title,
            className: "w-full h-48 object-cover group-hover:scale-105 transition-transform duration-300"
        }), a.jsxs("div", {
            className: "absolute top-4 left-4 flex gap-2",
            children: [a.jsxs(rt, {
                variant: e.type === "sale" ? "default" : "secondary",
                className: "bg-primary text-primary-foreground",
                children: ["For ", e.type === "sale" ? "Sale" : "Lease"]
            }), e.status !== "available" && a.jsx(rt, {
                variant: "destructive",
                className: "bg-accent text-accent-foreground",
                children: e.status === "sold" ? "Sold" : "Leased"
            })]
        }), a.jsx(ae, {
            variant: "ghost",
            size: "sm",
            className: "absolute top-4 right-4 bg-background/80 hover:bg-background text-primary",
            children: a.jsx(kS, {
                className: "h-4 w-4"
            })
        })]
    }), a.jsxs("div", {
        className: "p-6 space-y-4",
        children: [a.jsxs("div", {
            children: [a.jsx("h3", {
                className: "text-lg font-semibold text-foreground mb-2 line-clamp-1",
                children: e.title
            }), a.jsxs("div", {
                className: "flex items-center text-muted-foreground mb-3",
                children: [a.jsx(Ra, {
                    className: "h-4 w-4 mr-1"
                }), a.jsx("span", {
                    className: "text-sm",
                    children: e.location
                })]
            })]
        }), a.jsx("div", {
            className: "flex items-center justify-between text-sm text-muted-foreground",
            children: a.jsxs("div", {
                className: "flex items-center space-x-4",
                children: [a.jsxs("div", {
                    className: "flex items-center",
                    children: [a.jsx(gS, {
                        className: "h-4 w-4 mr-1"
                    }), a.jsx("span", {
                        children: e.beds
                    })]
                }), a.jsxs("div", {
                    className: "flex items-center",
                    children: [a.jsx(vS, {
                        className: "h-4 w-4 mr-1"
                    }), a.jsx("span", {
                        children: e.baths
                    })]
                }), a.jsxs("div", {
                    className: "flex items-center",
                    children: [a.jsx(DS, {
                        className: "h-4 w-4 mr-1"
                    }), a.jsx("span", {
                        children: e.sqft.toLocaleString()
                    })]
                })]
            })
        }), a.jsxs("div", {
            className: "flex items-center justify-between pt-4 border-t",
            children: [a.jsx("div", {
                className: "text-2xl font-bold text-primary",
                children: e.price
            }), a.jsx(ae, {
                variant: "outline",
                onClick: () => t == null ? void 0 : t(e),
                className: "border-primary text-primary hover:bg-primary hover:text-primary-foreground",
                children: "View Details"
            })]
        })]
    })]
})
  , vE = "/assets/hero-bg-B0SdPJip.jpg"
  , Xt = "/assets/property-1-CwUzGizS.jpg"
  , yn = "/assets/property-2-COxkmT0M.jpg"
  , _n = "/assets/property-3-B4Vm0zCp.jpg"
  , gE = () => {
    const e = [{
        id: "1",
        title: "Modern Family Home",
        price: "$750,000",
        location: "Downtown District",
        image: Xt,
        beds: 4,
        baths: 3,
        sqft: 2400,
        type: "sale",
        status: "sold"
    }, {
        id: "2",
        title: "Luxury Contemporary Villa",
        price: "$1,200,000",
        location: "Hillside Heights",
        image: yn,
        beds: 5,
        baths: 4,
        sqft: 3200,
        type: "sale",
        status: "sold"
    }, {
        id: "3",
        title: "Elegant Victorian Estate",
        price: "$950,000",
        location: "Heritage Gardens",
        image: _n,
        beds: 4,
        baths: 3,
        sqft: 2800,
        type: "sale",
        status: "leased"
    }, {
        id: "4",
        title: "Cozy Suburban Home",
        price: "$650,000",
        location: "Green Valley",
        image: Xt,
        beds: 3,
        baths: 2,
        sqft: 1800,
        type: "lease",
        status: "leased"
    }]
      , t = [{
        name: "Sarah Johnson",
        role: "Home Buyer",
        content: "RealtyPro made finding my dream home effortless. Their AI-powered recommendations were spot on!",
        rating: 5
    }, {
        name: "Michael Chen",
        role: "Property Investor",
        content: "Outstanding service and market insights. They helped me make informed investment decisions.",
        rating: 5
    }, {
        name: "Emily Davis",
        role: "First-time Seller",
        content: "The team guided me through every step of selling my home. Couldn't be happier with the results!",
        rating: 5
    }]
      , n = [{
        icon: AS,
        number: "10,000+",
        label: "Happy Clients"
    }, {
        icon: gy,
        number: "500+",
        label: "Properties Sold"
    }, {
        icon: nl,
        number: "15+",
        label: "Years Experience"
    }, {
        icon: Nh,
        number: "4.9",
        label: "Client Rating"
    }]
      , r = ["Bank of America", "Wells Fargo", "Chase", "Quicken Loans", "Century 21", "Coldwell Banker"];
    return a.jsxs("div", {
        className: "min-h-screen",
        children: [a.jsxs("section", {
            className: "relative h-screen flex items-center justify-center overflow-hidden",
            children: [a.jsx("div", {
                className: "absolute inset-0 bg-cover bg-center bg-no-repeat",
                style: {
                    backgroundImage: `url(${vE})`
                }
            }), a.jsx("div", {
                className: "absolute inset-0 bg-gradient-hero"
            }), a.jsx("div", {
                className: "relative z-10 text-center max-w-4xl mx-auto px-4 sm:px-6 lg:px-8",
                children: a.jsxs("div", {
                    className: "animate-fade-in-up",
                    children: [a.jsxs("h1", {
                        className: "font-display text-balance leading-[1.1] text-primary-foreground mb-8",
                        children: ["Find Your Dream Home with", " ", a.jsx("span", {
                            className: "bg-gradient-accent bg-clip-text text-transparent",
                            children: "RealtyPro"
                        })]
                    }), a.jsx("p", {
                        className: "text-xl md:text-2xl text-primary-foreground/90 mb-10 max-w-3xl mx-auto leading-relaxed text-balance",
                        children: "Discover the best properties and insights with our AI-powered real estate solutions."
                    }), a.jsxs("div", {
                        className: "grid grid-cols-2 md:grid-cols-4 gap-4 max-w-3xl mx-auto mb-12",
                        children: [a.jsx(Fe, {
                            to: "/sell-evaluate",
                            children: a.jsx(ae, {
                                variant: "outline",
                                className: "w-full bg-primary-foreground/10 border-primary-foreground/20 text-primary-foreground hover:bg-primary-foreground/20 transition-smooth backdrop-blur-sm",
                                children: "Sell Your Home"
                            })
                        }), a.jsx(Fe, {
                            to: "/buy-lease",
                            children: a.jsx(ae, {
                                variant: "outline",
                                className: "w-full bg-primary-foreground/10 border-primary-foreground/20 text-primary-foreground hover:bg-primary-foreground/20 transition-smooth backdrop-blur-sm",
                                children: "Lease Property"
                            })
                        }), a.jsx(Fe, {
                            to: "/open-house",
                            children: a.jsx(ae, {
                                variant: "outline",
                                className: "w-full bg-primary-foreground/10 border-primary-foreground/20 text-primary-foreground hover:bg-primary-foreground/20 transition-smooth backdrop-blur-sm",
                                children: "Open Houses"
                            })
                        }), a.jsx(Fe, {
                            to: "/mortgage-calculator",
                            children: a.jsx(ae, {
                                variant: "outline",
                                className: "w-full bg-primary-foreground/10 border-primary-foreground/20 text-primary-foreground hover:bg-primary-foreground/20 transition-smooth backdrop-blur-sm",
                                children: "Mortgage Calculator"
                            })
                        })]
                    }), a.jsxs(ae, {
                        size: "lg",
                        className: "bg-gradient-accent hover:shadow-accent text-primary font-semibold text-lg px-10 py-4 transition-smooth transform hover:scale-105",
                        children: [a.jsx(MS, {
                            className: "w-5 h-5 mr-3"
                        }), "Watch Our Story"]
                    })]
                })
            })]
        }), a.jsx("section", {
            className: "py-24 bg-gradient-surface",
            children: a.jsx("div", {
                className: "max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
                children: a.jsxs("div", {
                    className: "grid lg:grid-cols-2 gap-16 items-center",
                    children: [a.jsxs("div", {
                        className: "animate-fade-in-up",
                        children: [a.jsx(rt, {
                            className: "mb-6 bg-accent/10 text-accent-foreground border-accent/20 px-4 py-2",
                            children: "About RealtyPro"
                        }), a.jsx("h2", {
                            className: "font-display text-balance mb-8",
                            children: "Your Trusted Real Estate Partner"
                        }), a.jsx("p", {
                            className: "text-muted-foreground text-lg leading-relaxed mb-8 text-balance",
                            children: "With over 15 years of experience in the real estate industry, RealtyPro combines traditional expertise with cutting-edge AI technology to deliver exceptional results for our clients."
                        }), a.jsxs("div", {
                            className: "space-y-6 mb-10",
                            children: [a.jsxs("div", {
                                className: "flex items-center space-x-4",
                                children: [a.jsx(ir, {
                                    className: "w-6 h-6 text-accent flex-shrink-0"
                                }), a.jsxs("div", {
                                    children: [a.jsx("h4", {
                                        className: "font-semibold text-foreground mb-1",
                                        children: "AI-powered property matching"
                                    }), a.jsx("p", {
                                        className: "text-muted-foreground text-sm",
                                        children: "Smart algorithms find properties that perfectly match your preferences"
                                    })]
                                })]
                            }), a.jsxs("div", {
                                className: "flex items-center space-x-4",
                                children: [a.jsx(ir, {
                                    className: "w-6 h-6 text-accent flex-shrink-0"
                                }), a.jsxs("div", {
                                    children: [a.jsx("h4", {
                                        className: "font-semibold text-foreground mb-1",
                                        children: "Expert market analysis"
                                    }), a.jsx("p", {
                                        className: "text-muted-foreground text-sm",
                                        children: "Deep insights into market trends and property valuations"
                                    })]
                                })]
                            }), a.jsxs("div", {
                                className: "flex items-center space-x-4",
                                children: [a.jsx(ir, {
                                    className: "w-6 h-6 text-accent flex-shrink-0"
                                }), a.jsxs("div", {
                                    children: [a.jsx("h4", {
                                        className: "font-semibold text-foreground mb-1",
                                        children: "Personalized client service"
                                    }), a.jsx("p", {
                                        className: "text-muted-foreground text-sm",
                                        children: "Dedicated support throughout your real estate journey"
                                    })]
                                })]
                            })]
                        }), a.jsxs(ae, {
                            className: "bg-primary hover:bg-primary-dark text-primary-foreground shadow-md hover:shadow-lg transition-smooth",
                            children: ["Learn More About Us", a.jsx(ha, {
                                className: "w-5 h-5 ml-2"
                            })]
                        })]
                    }), a.jsxs("div", {
                        className: "relative",
                        children: [a.jsx("img", {
                            src: yn,
                            alt: "About RealtyPro",
                            className: "rounded-2xl shadow-xl w-full h-96 object-cover animate-scale-in"
                        }), a.jsxs("div", {
                            className: "absolute -bottom-6 -right-6 bg-accent text-accent-foreground p-6 rounded-xl shadow-accent",
                            children: [a.jsx("div", {
                                className: "text-2xl font-bold",
                                children: "15+"
                            }), a.jsx("div", {
                                className: "text-sm font-medium",
                                children: "Years Experience"
                            })]
                        })]
                    })]
                })
            })
        }), a.jsx("section", {
            className: "py-16 bg-background",
            children: a.jsxs("div", {
                className: "max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center",
                children: [a.jsx(rt, {
                    className: "mb-4 bg-primary/10 text-primary border-primary/20",
                    children: "Our Strategic Partners"
                }), a.jsx("h2", {
                    className: "text-3xl md:text-4xl font-bold text-foreground mb-12",
                    children: "Trusted by Leading Financial Institutions"
                }), a.jsx("div", {
                    className: "grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-8 items-center",
                    children: r.map( (o, s) => a.jsx("div", {
                        className: "text-muted-foreground font-semibold text-lg hover:text-primary transition-colors",
                        children: o
                    }, s))
                })]
            })
        }), a.jsx("section", {
            className: "py-16 bg-surface-gradient",
            children: a.jsxs("div", {
                className: "max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
                children: [a.jsxs("div", {
                    className: "text-center mb-12",
                    children: [a.jsx(rt, {
                        className: "mb-4 bg-accent/10 text-accent-foreground border-accent/20",
                        children: "Client Testimonials"
                    }), a.jsx("h2", {
                        className: "text-3xl md:text-4xl font-bold text-foreground mb-4",
                        children: "What Our Clients Say"
                    }), a.jsx("p", {
                        className: "text-muted-foreground text-lg max-w-2xl mx-auto",
                        children: "Don't just take our word for it. Here's what our satisfied clients have to say about their experience with RealtyPro."
                    })]
                }), a.jsx("div", {
                    className: "grid md:grid-cols-3 gap-8",
                    children: t.map( (o, s) => a.jsxs(Ce, {
                        className: "p-6 shadow-soft hover:shadow-medium transition-all duration-300 animate-fade-in border-0",
                        children: [a.jsx("div", {
                            className: "flex items-center mb-4",
                            children: [...Array(o.rating)].map( (i, l) => a.jsx(Nh, {
                                className: "w-4 h-4 text-accent fill-current"
                            }, l))
                        }), a.jsx(RS, {
                            className: "w-8 h-8 text-accent/20 mb-4"
                        }), a.jsxs("p", {
                            className: "text-muted-foreground mb-4 leading-relaxed",
                            children: ['"', o.content, '"']
                        }), a.jsxs("div", {
                            children: [a.jsx("p", {
                                className: "font-semibold text-foreground",
                                children: o.name
                            }), a.jsx("p", {
                                className: "text-sm text-muted-foreground",
                                children: o.role
                            })]
                        })]
                    }, s))
                })]
            })
        }), a.jsx("section", {
            className: "py-16 bg-background",
            children: a.jsxs("div", {
                className: "max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
                children: [a.jsxs("div", {
                    className: "text-center mb-12",
                    children: [a.jsx(rt, {
                        className: "mb-4 bg-primary/10 text-primary border-primary/20",
                        children: "Recent Success Stories"
                    }), a.jsx("h2", {
                        className: "text-3xl md:text-4xl font-bold text-foreground mb-4",
                        children: "Recently Sold and Leased"
                    }), a.jsx("p", {
                        className: "text-muted-foreground text-lg max-w-2xl mx-auto",
                        children: "Take a look at some of our recent successful transactions. Your dream property could be next!"
                    })]
                }), a.jsx("div", {
                    className: "grid md:grid-cols-2 lg:grid-cols-4 gap-6",
                    children: e.map(o => a.jsx(Px, {
                        property: o,
                        onViewDetails: () => console.log("View details:", o)
                    }, o.id))
                }), a.jsx("div", {
                    className: "text-center mt-12",
                    children: a.jsx(Fe, {
                        to: "/buy-lease",
                        children: a.jsxs(ae, {
                            size: "lg",
                            className: "bg-primary hover:bg-primary-dark text-primary-foreground",
                            children: ["View All Properties", a.jsx(ha, {
                                className: "w-4 h-4 ml-2"
                            })]
                        })
                    })
                })]
            })
        }), a.jsx("section", {
            className: "py-16 bg-primary text-primary-foreground",
            children: a.jsxs("div", {
                className: "max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
                children: [a.jsxs("div", {
                    className: "text-center mb-12",
                    children: [a.jsx(rt, {
                        className: "mb-4 bg-accent text-accent-foreground",
                        children: "Our Achievements"
                    }), a.jsx("h2", {
                        className: "text-3xl md:text-4xl font-bold mb-4",
                        children: "Numbers That Speak for Themselves"
                    }), a.jsx("p", {
                        className: "text-primary-foreground/80 text-lg max-w-2xl mx-auto",
                        children: "Our track record of success demonstrates our commitment to excellence and client satisfaction."
                    })]
                }), a.jsx("div", {
                    className: "grid grid-cols-2 lg:grid-cols-4 gap-8",
                    children: n.map( (o, s) => {
                        const i = o.icon;
                        return a.jsxs("div", {
                            className: "text-center animate-fade-in",
                            children: [a.jsx("div", {
                                className: "bg-accent/10 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4",
                                children: a.jsx(i, {
                                    className: "w-8 h-8 text-accent"
                                })
                            }), a.jsx("div", {
                                className: "text-3xl lg:text-4xl font-bold text-accent mb-2",
                                children: o.number
                            }), a.jsx("div", {
                                className: "text-primary-foreground/80 font-medium",
                                children: o.label
                            })]
                        }, s)
                    }
                    )
                })]
            })
        })]
    })
}
  , Ee = m.forwardRef( ({className: e, type: t, ...n}, r) => a.jsx("input", {
    type: t,
    className: re("flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-base ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium file:text-foreground placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 md:text-sm", e),
    ref: r,
    ...n
}));
Ee.displayName = "Input";
var yE = "Label"
  , Tx = m.forwardRef( (e, t) => a.jsx(te.label, {
    ...e,
    ref: t,
    onMouseDown: n => {
        var o;
        n.target.closest("button, input, select, textarea") || ((o = e.onMouseDown) == null || o.call(e, n),
        !n.defaultPrevented && n.detail > 1 && n.preventDefault())
    }
}));
Tx.displayName = yE;
var Mx = Tx;
const xE = Ol("text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70")
  , se = m.forwardRef( ({className: e, ...t}, n) => a.jsx(Mx, {
    ref: n,
    className: re(xE(), e),
    ...t
}));
se.displayName = Mx.displayName;
const Oa = m.forwardRef( ({className: e, ...t}, n) => a.jsx("textarea", {
    className: re("flex min-h-[80px] w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50", e),
    ref: n,
    ...t
}));
Oa.displayName = "Textarea";
function ul(e, [t,n]) {
    return Math.min(n, Math.max(t, e))
}
var wE = m.createContext(void 0);
function Rx(e) {
    const t = m.useContext(wE);
    return e || t || "ltr"
}
var Oc = 0;
function _x() {
    m.useEffect( () => {
        const e = document.querySelectorAll("[data-radix-focus-guard]");
        return document.body.insertAdjacentElement("afterbegin", e[0] ?? Zh()),
        document.body.insertAdjacentElement("beforeend", e[1] ?? Zh()),
        Oc++,
        () => {
            Oc === 1 && document.querySelectorAll("[data-radix-focus-guard]").forEach(t => t.remove()),
            Oc--
        }
    }
    , [])
}
function Zh() {
    const e = document.createElement("span");
    return e.setAttribute("data-radix-focus-guard", ""),
    e.tabIndex = 0,
    e.style.outline = "none",
    e.style.opacity = "0",
    e.style.position = "fixed",
    e.style.pointerEvents = "none",
    e
}
var Ac = "focusScope.autoFocusOnMount"
  , Ic = "focusScope.autoFocusOnUnmount"
  , ep = {
    bubbles: !1,
    cancelable: !0
}
  , bE = "FocusScope"
  , Of = m.forwardRef( (e, t) => {
    const {loop: n=!1, trapped: r=!1, onMountAutoFocus: o, onUnmountAutoFocus: s, ...i} = e
      , [l,c] = m.useState(null)
      , u = Zt(o)
      , d = Zt(s)
      , f = m.useRef(null)
      , g = fe(t, v => c(v))
      , h = m.useRef({
        paused: !1,
        pause() {
            this.paused = !0
        },
        resume() {
            this.paused = !1
        }
    }).current;
    m.useEffect( () => {
        if (r) {
            let v = function(x) {
                if (h.paused || !l)
                    return;
                const N = x.target;
                l.contains(N) ? f.current = N : Gn(f.current, {
                    select: !0
                })
            }
              , w = function(x) {
                if (h.paused || !l)
                    return;
                const N = x.relatedTarget;
                N !== null && (l.contains(N) || Gn(f.current, {
                    select: !0
                }))
            }
              , y = function(x) {
                if (document.activeElement === document.body)
                    for (const S of x)
                        S.removedNodes.length > 0 && Gn(l)
            };
            document.addEventListener("focusin", v),
            document.addEventListener("focusout", w);
            const p = new MutationObserver(y);
            return l && p.observe(l, {
                childList: !0,
                subtree: !0
            }),
            () => {
                document.removeEventListener("focusin", v),
                document.removeEventListener("focusout", w),
                p.disconnect()
            }
        }
    }
    , [r, l, h.paused]),
    m.useEffect( () => {
        if (l) {
            np.add(h);
            const v = document.activeElement;
            if (!l.contains(v)) {
                const y = new CustomEvent(Ac,ep);
                l.addEventListener(Ac, u),
                l.dispatchEvent(y),
                y.defaultPrevented || (NE(EE(Dx(l)), {
                    select: !0
                }),
                document.activeElement === v && Gn(l))
            }
            return () => {
                l.removeEventListener(Ac, u),
                setTimeout( () => {
                    const y = new CustomEvent(Ic,ep);
                    l.addEventListener(Ic, d),
                    l.dispatchEvent(y),
                    y.defaultPrevented || Gn(v ?? document.body, {
                        select: !0
                    }),
                    l.removeEventListener(Ic, d),
                    np.remove(h)
                }
                , 0)
            }
        }
    }
    , [l, u, d, h]);
    const b = m.useCallback(v => {
        if (!n && !r || h.paused)
            return;
        const w = v.key === "Tab" && !v.altKey && !v.ctrlKey && !v.metaKey
          , y = document.activeElement;
        if (w && y) {
            const p = v.currentTarget
              , [x,N] = SE(p);
            x && N ? !v.shiftKey && y === N ? (v.preventDefault(),
            n && Gn(x, {
                select: !0
            })) : v.shiftKey && y === x && (v.preventDefault(),
            n && Gn(N, {
                select: !0
            })) : y === p && v.preventDefault()
        }
    }
    , [n, r, h.paused]);
    return a.jsx(te.div, {
        tabIndex: -1,
        ...i,
        ref: g,
        onKeyDown: b
    })
}
);
Of.displayName = bE;
function NE(e, {select: t=!1}={}) {
    const n = document.activeElement;
    for (const r of e)
        if (Gn(r, {
            select: t
        }),
        document.activeElement !== n)
            return
}
function SE(e) {
    const t = Dx(e)
      , n = tp(t, e)
      , r = tp(t.reverse(), e);
    return [n, r]
}
function Dx(e) {
    const t = []
      , n = document.createTreeWalker(e, NodeFilter.SHOW_ELEMENT, {
        acceptNode: r => {
            const o = r.tagName === "INPUT" && r.type === "hidden";
            return r.disabled || r.hidden || o ? NodeFilter.FILTER_SKIP : r.tabIndex >= 0 ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_SKIP
        }
    });
    for (; n.nextNode(); )
        t.push(n.currentNode);
    return t
}
function tp(e, t) {
    for (const n of e)
        if (!jE(n, {
            upTo: t
        }))
            return n
}
function jE(e, {upTo: t}) {
    if (getComputedStyle(e).visibility === "hidden")
        return !0;
    for (; e; ) {
        if (t !== void 0 && e === t)
            return !1;
        if (getComputedStyle(e).display === "none")
            return !0;
        e = e.parentElement
    }
    return !1
}
function CE(e) {
    return e instanceof HTMLInputElement && "select"in e
}
function Gn(e, {select: t=!1}={}) {
    if (e && e.focus) {
        const n = document.activeElement;
        e.focus({
            preventScroll: !0
        }),
        e !== n && CE(e) && t && e.select()
    }
}
var np = kE();
function kE() {
    let e = [];
    return {
        add(t) {
            const n = e[0];
            t !== n && (n == null || n.pause()),
            e = rp(e, t),
            e.unshift(t)
        },
        remove(t) {
            var n;
            e = rp(e, t),
            (n = e[0]) == null || n.resume()
        }
    }
}
function rp(e, t) {
    const n = [...e]
      , r = n.indexOf(t);
    return r !== -1 && n.splice(r, 1),
    n
}
function EE(e) {
    return e.filter(t => t.tagName !== "A")
}
function Ox(e) {
    const t = m.useRef({
        value: e,
        previous: e
    });
    return m.useMemo( () => (t.current.value !== e && (t.current.previous = t.current.value,
    t.current.value = e),
    t.current.previous), [e])
}
var PE = function(e) {
    if (typeof document > "u")
        return null;
    var t = Array.isArray(e) ? e[0] : e;
    return t.ownerDocument.body
}
  , vo = new WeakMap
  , ci = new WeakMap
  , ui = {}
  , Lc = 0
  , Ax = function(e) {
    return e && (e.host || Ax(e.parentNode))
}
  , TE = function(e, t) {
    return t.map(function(n) {
        if (e.contains(n))
            return n;
        var r = Ax(n);
        return r && e.contains(r) ? r : (console.error("aria-hidden", n, "in not contained inside", e, ". Doing nothing"),
        null)
    }).filter(function(n) {
        return !!n
    })
}
  , ME = function(e, t, n, r) {
    var o = TE(t, Array.isArray(e) ? e : [e]);
    ui[n] || (ui[n] = new WeakMap);
    var s = ui[n]
      , i = []
      , l = new Set
      , c = new Set(o)
      , u = function(f) {
        !f || l.has(f) || (l.add(f),
        u(f.parentNode))
    };
    o.forEach(u);
    var d = function(f) {
        !f || c.has(f) || Array.prototype.forEach.call(f.children, function(g) {
            if (l.has(g))
                d(g);
            else
                try {
                    var h = g.getAttribute(r)
                      , b = h !== null && h !== "false"
                      , v = (vo.get(g) || 0) + 1
                      , w = (s.get(g) || 0) + 1;
                    vo.set(g, v),
                    s.set(g, w),
                    i.push(g),
                    v === 1 && b && ci.set(g, !0),
                    w === 1 && g.setAttribute(n, "true"),
                    b || g.setAttribute(r, "true")
                } catch (y) {
                    console.error("aria-hidden: cannot operate on ", g, y)
                }
        })
    };
    return d(t),
    l.clear(),
    Lc++,
    function() {
        i.forEach(function(f) {
            var g = vo.get(f) - 1
              , h = s.get(f) - 1;
            vo.set(f, g),
            s.set(f, h),
            g || (ci.has(f) || f.removeAttribute(r),
            ci.delete(f)),
            h || f.removeAttribute(n)
        }),
        Lc--,
        Lc || (vo = new WeakMap,
        vo = new WeakMap,
        ci = new WeakMap,
        ui = {})
    }
}
  , Ix = function(e, t, n) {
    n === void 0 && (n = "data-aria-hidden");
    var r = Array.from(Array.isArray(e) ? e : [e])
      , o = PE(e);
    return o ? (r.push.apply(r, Array.from(o.querySelectorAll("[aria-live]"))),
    ME(r, o, n, "aria-hidden")) : function() {
        return null
    }
}
  , fn = function() {
    return fn = Object.assign || function(t) {
        for (var n, r = 1, o = arguments.length; r < o; r++) {
            n = arguments[r];
            for (var s in n)
                Object.prototype.hasOwnProperty.call(n, s) && (t[s] = n[s])
        }
        return t
    }
    ,
    fn.apply(this, arguments)
};
function Lx(e, t) {
    var n = {};
    for (var r in e)
        Object.prototype.hasOwnProperty.call(e, r) && t.indexOf(r) < 0 && (n[r] = e[r]);
    if (e != null && typeof Object.getOwnPropertySymbols == "function")
        for (var o = 0, r = Object.getOwnPropertySymbols(e); o < r.length; o++)
            t.indexOf(r[o]) < 0 && Object.prototype.propertyIsEnumerable.call(e, r[o]) && (n[r[o]] = e[r[o]]);
    return n
}
function RE(e, t, n) {
    if (n || arguments.length === 2)
        for (var r = 0, o = t.length, s; r < o; r++)
            (s || !(r in t)) && (s || (s = Array.prototype.slice.call(t, 0, r)),
            s[r] = t[r]);
    return e.concat(s || Array.prototype.slice.call(t))
}
var Pi = "right-scroll-bar-position"
  , Ti = "width-before-scroll-bar"
  , _E = "with-scroll-bars-hidden"
  , DE = "--removed-body-scroll-bar-size";
function Fc(e, t) {
    return typeof e == "function" ? e(t) : e && (e.current = t),
    e
}
function OE(e, t) {
    var n = m.useState(function() {
        return {
            value: e,
            callback: t,
            facade: {
                get current() {
                    return n.value
                },
                set current(r) {
                    var o = n.value;
                    o !== r && (n.value = r,
                    n.callback(r, o))
                }
            }
        }
    })[0];
    return n.callback = t,
    n.facade
}
var AE = typeof window < "u" ? m.useLayoutEffect : m.useEffect
  , op = new WeakMap;
function IE(e, t) {
    var n = OE(null, function(r) {
        return e.forEach(function(o) {
            return Fc(o, r)
        })
    });
    return AE(function() {
        var r = op.get(n);
        if (r) {
            var o = new Set(r)
              , s = new Set(e)
              , i = n.current;
            o.forEach(function(l) {
                s.has(l) || Fc(l, null)
            }),
            s.forEach(function(l) {
                o.has(l) || Fc(l, i)
            })
        }
        op.set(n, e)
    }, [e]),
    n
}
function LE(e) {
    return e
}
function FE(e, t) {
    t === void 0 && (t = LE);
    var n = []
      , r = !1
      , o = {
        read: function() {
            if (r)
                throw new Error("Sidecar: could not `read` from an `assigned` medium. `read` could be used only with `useMedium`.");
            return n.length ? n[n.length - 1] : e
        },
        useMedium: function(s) {
            var i = t(s, r);
            return n.push(i),
            function() {
                n = n.filter(function(l) {
                    return l !== i
                })
            }
        },
        assignSyncMedium: function(s) {
            for (r = !0; n.length; ) {
                var i = n;
                n = [],
                i.forEach(s)
            }
            n = {
                push: function(l) {
                    return s(l)
                },
                filter: function() {
                    return n
                }
            }
        },
        assignMedium: function(s) {
            r = !0;
            var i = [];
            if (n.length) {
                var l = n;
                n = [],
                l.forEach(s),
                i = n
            }
            var c = function() {
                var d = i;
                i = [],
                d.forEach(s)
            }
              , u = function() {
                return Promise.resolve().then(c)
            };
            u(),
            n = {
                push: function(d) {
                    i.push(d),
                    u()
                },
                filter: function(d) {
                    return i = i.filter(d),
                    n
                }
            }
        }
    };
    return o
}
function zE(e) {
    e === void 0 && (e = {});
    var t = FE(null);
    return t.options = fn({
        async: !0,
        ssr: !1
    }, e),
    t
}
var Fx = function(e) {
    var t = e.sideCar
      , n = Lx(e, ["sideCar"]);
    if (!t)
        throw new Error("Sidecar: please provide `sideCar` property to import the right car");
    var r = t.read();
    if (!r)
        throw new Error("Sidecar medium not found");
    return m.createElement(r, fn({}, n))
};
Fx.isSideCarExport = !0;
function $E(e, t) {
    return e.useMedium(t),
    Fx
}
var zx = zE()
  , zc = function() {}
  , Vl = m.forwardRef(function(e, t) {
    var n = m.useRef(null)
      , r = m.useState({
        onScrollCapture: zc,
        onWheelCapture: zc,
        onTouchMoveCapture: zc
    })
      , o = r[0]
      , s = r[1]
      , i = e.forwardProps
      , l = e.children
      , c = e.className
      , u = e.removeScrollBar
      , d = e.enabled
      , f = e.shards
      , g = e.sideCar
      , h = e.noRelative
      , b = e.noIsolation
      , v = e.inert
      , w = e.allowPinchZoom
      , y = e.as
      , p = y === void 0 ? "div" : y
      , x = e.gapMode
      , N = Lx(e, ["forwardProps", "children", "className", "removeScrollBar", "enabled", "shards", "sideCar", "noRelative", "noIsolation", "inert", "allowPinchZoom", "as", "gapMode"])
      , S = g
      , k = IE([n, t])
      , C = fn(fn({}, N), o);
    return m.createElement(m.Fragment, null, d && m.createElement(S, {
        sideCar: zx,
        removeScrollBar: u,
        shards: f,
        noRelative: h,
        noIsolation: b,
        inert: v,
        setCallbacks: s,
        allowPinchZoom: !!w,
        lockRef: n,
        gapMode: x
    }), i ? m.cloneElement(m.Children.only(l), fn(fn({}, C), {
        ref: k
    })) : m.createElement(p, fn({}, C, {
        className: c,
        ref: k
    }), l))
});
Vl.defaultProps = {
    enabled: !0,
    removeScrollBar: !0,
    inert: !1
};
Vl.classNames = {
    fullWidth: Ti,
    zeroRight: Pi
};
var BE = function() {
    if (typeof __webpack_nonce__ < "u")
        return __webpack_nonce__
};
function WE() {
    if (!document)
        return null;
    var e = document.createElement("style");
    e.type = "text/css";
    var t = BE();
    return t && e.setAttribute("nonce", t),
    e
}
function HE(e, t) {
    e.styleSheet ? e.styleSheet.cssText = t : e.appendChild(document.createTextNode(t))
}
function VE(e) {
    var t = document.head || document.getElementsByTagName("head")[0];
    t.appendChild(e)
}
var UE = function() {
    var e = 0
      , t = null;
    return {
        add: function(n) {
            e == 0 && (t = WE()) && (HE(t, n),
            VE(t)),
            e++
        },
        remove: function() {
            e--,
            !e && t && (t.parentNode && t.parentNode.removeChild(t),
            t = null)
        }
    }
}
  , YE = function() {
    var e = UE();
    return function(t, n) {
        m.useEffect(function() {
            return e.add(t),
            function() {
                e.remove()
            }
        }, [t && n])
    }
}
  , $x = function() {
    var e = YE()
      , t = function(n) {
        var r = n.styles
          , o = n.dynamic;
        return e(r, o),
        null
    };
    return t
}
  , KE = {
    left: 0,
    top: 0,
    right: 0,
    gap: 0
}
  , $c = function(e) {
    return parseInt(e || "", 10) || 0
}
  , QE = function(e) {
    var t = window.getComputedStyle(document.body)
      , n = t[e === "padding" ? "paddingLeft" : "marginLeft"]
      , r = t[e === "padding" ? "paddingTop" : "marginTop"]
      , o = t[e === "padding" ? "paddingRight" : "marginRight"];
    return [$c(n), $c(r), $c(o)]
}
  , GE = function(e) {
    if (e === void 0 && (e = "margin"),
    typeof window > "u")
        return KE;
    var t = QE(e)
      , n = document.documentElement.clientWidth
      , r = window.innerWidth;
    return {
        left: t[0],
        top: t[1],
        right: t[2],
        gap: Math.max(0, r - n + t[2] - t[0])
    }
}
  , qE = $x()
  , Bo = "data-scroll-locked"
  , XE = function(e, t, n, r) {
    var o = e.left
      , s = e.top
      , i = e.right
      , l = e.gap;
    return n === void 0 && (n = "margin"),
    `
  .`.concat(_E, ` {
   overflow: hidden `).concat(r, `;
   padding-right: `).concat(l, "px ").concat(r, `;
  }
  body[`).concat(Bo, `] {
    overflow: hidden `).concat(r, `;
    overscroll-behavior: contain;
    `).concat([t && "position: relative ".concat(r, ";"), n === "margin" && `
    padding-left: `.concat(o, `px;
    padding-top: `).concat(s, `px;
    padding-right: `).concat(i, `px;
    margin-left:0;
    margin-top:0;
    margin-right: `).concat(l, "px ").concat(r, `;
    `), n === "padding" && "padding-right: ".concat(l, "px ").concat(r, ";")].filter(Boolean).join(""), `
  }
  
  .`).concat(Pi, ` {
    right: `).concat(l, "px ").concat(r, `;
  }
  
  .`).concat(Ti, ` {
    margin-right: `).concat(l, "px ").concat(r, `;
  }
  
  .`).concat(Pi, " .").concat(Pi, ` {
    right: 0 `).concat(r, `;
  }
  
  .`).concat(Ti, " .").concat(Ti, ` {
    margin-right: 0 `).concat(r, `;
  }
  
  body[`).concat(Bo, `] {
    `).concat(DE, ": ").concat(l, `px;
  }
`)
}
  , sp = function() {
    var e = parseInt(document.body.getAttribute(Bo) || "0", 10);
    return isFinite(e) ? e : 0
}
  , JE = function() {
    m.useEffect(function() {
        return document.body.setAttribute(Bo, (sp() + 1).toString()),
        function() {
            var e = sp() - 1;
            e <= 0 ? document.body.removeAttribute(Bo) : document.body.setAttribute(Bo, e.toString())
        }
    }, [])
}
  , ZE = function(e) {
    var t = e.noRelative
      , n = e.noImportant
      , r = e.gapMode
      , o = r === void 0 ? "margin" : r;
    JE();
    var s = m.useMemo(function() {
        return GE(o)
    }, [o]);
    return m.createElement(qE, {
        styles: XE(s, !t, o, n ? "" : "!important")
    })
}
  , ad = !1;
if (typeof window < "u")
    try {
        var di = Object.defineProperty({}, "passive", {
            get: function() {
                return ad = !0,
                !0
            }
        });
        window.addEventListener("test", di, di),
        window.removeEventListener("test", di, di)
    } catch {
        ad = !1
    }
var go = ad ? {
    passive: !1
} : !1
  , eP = function(e) {
    return e.tagName === "TEXTAREA"
}
  , Bx = function(e, t) {
    if (!(e instanceof Element))
        return !1;
    var n = window.getComputedStyle(e);
    return n[t] !== "hidden" && !(n.overflowY === n.overflowX && !eP(e) && n[t] === "visible")
}
  , tP = function(e) {
    return Bx(e, "overflowY")
}
  , nP = function(e) {
    return Bx(e, "overflowX")
}
  , ap = function(e, t) {
    var n = t.ownerDocument
      , r = t;
    do {
        typeof ShadowRoot < "u" && r instanceof ShadowRoot && (r = r.host);
        var o = Wx(e, r);
        if (o) {
            var s = Hx(e, r)
              , i = s[1]
              , l = s[2];
            if (i > l)
                return !0
        }
        r = r.parentNode
    } while (r && r !== n.body);
    return !1
}
  , rP = function(e) {
    var t = e.scrollTop
      , n = e.scrollHeight
      , r = e.clientHeight;
    return [t, n, r]
}
  , oP = function(e) {
    var t = e.scrollLeft
      , n = e.scrollWidth
      , r = e.clientWidth;
    return [t, n, r]
}
  , Wx = function(e, t) {
    return e === "v" ? tP(t) : nP(t)
}
  , Hx = function(e, t) {
    return e === "v" ? rP(t) : oP(t)
}
  , sP = function(e, t) {
    return e === "h" && t === "rtl" ? -1 : 1
}
  , aP = function(e, t, n, r, o) {
    var s = sP(e, window.getComputedStyle(t).direction)
      , i = s * r
      , l = n.target
      , c = t.contains(l)
      , u = !1
      , d = i > 0
      , f = 0
      , g = 0;
    do {
        if (!l)
            break;
        var h = Hx(e, l)
          , b = h[0]
          , v = h[1]
          , w = h[2]
          , y = v - w - s * b;
        (b || y) && Wx(e, l) && (f += y,
        g += b);
        var p = l.parentNode;
        l = p && p.nodeType === Node.DOCUMENT_FRAGMENT_NODE ? p.host : p
    } while (!c && l !== document.body || c && (t.contains(l) || t === l));
    return (d && (Math.abs(f) < 1 || !o) || !d && (Math.abs(g) < 1 || !o)) && (u = !0),
    u
}
  , fi = function(e) {
    return "changedTouches"in e ? [e.changedTouches[0].clientX, e.changedTouches[0].clientY] : [0, 0]
}
  , ip = function(e) {
    return [e.deltaX, e.deltaY]
}
  , lp = function(e) {
    return e && "current"in e ? e.current : e
}
  , iP = function(e, t) {
    return e[0] === t[0] && e[1] === t[1]
}
  , lP = function(e) {
    return `
  .block-interactivity-`.concat(e, ` {pointer-events: none;}
  .allow-interactivity-`).concat(e, ` {pointer-events: all;}
`)
}
  , cP = 0
  , yo = [];
function uP(e) {
    var t = m.useRef([])
      , n = m.useRef([0, 0])
      , r = m.useRef()
      , o = m.useState(cP++)[0]
      , s = m.useState($x)[0]
      , i = m.useRef(e);
    m.useEffect(function() {
        i.current = e
    }, [e]),
    m.useEffect(function() {
        if (e.inert) {
            document.body.classList.add("block-interactivity-".concat(o));
            var v = RE([e.lockRef.current], (e.shards || []).map(lp), !0).filter(Boolean);
            return v.forEach(function(w) {
                return w.classList.add("allow-interactivity-".concat(o))
            }),
            function() {
                document.body.classList.remove("block-interactivity-".concat(o)),
                v.forEach(function(w) {
                    return w.classList.remove("allow-interactivity-".concat(o))
                })
            }
        }
    }, [e.inert, e.lockRef.current, e.shards]);
    var l = m.useCallback(function(v, w) {
        if ("touches"in v && v.touches.length === 2 || v.type === "wheel" && v.ctrlKey)
            return !i.current.allowPinchZoom;
        var y = fi(v), p = n.current, x = "deltaX"in v ? v.deltaX : p[0] - y[0], N = "deltaY"in v ? v.deltaY : p[1] - y[1], S, k = v.target, C = Math.abs(x) > Math.abs(N) ? "h" : "v";
        if ("touches"in v && C === "h" && k.type === "range")
            return !1;
        var T = ap(C, k);
        if (!T)
            return !0;
        if (T ? S = C : (S = C === "v" ? "h" : "v",
        T = ap(C, k)),
        !T)
            return !1;
        if (!r.current && "changedTouches"in v && (x || N) && (r.current = S),
        !S)
            return !0;
        var D = r.current || S;
        return aP(D, w, v, D === "h" ? x : N, !0)
    }, [])
      , c = m.useCallback(function(v) {
        var w = v;
        if (!(!yo.length || yo[yo.length - 1] !== s)) {
            var y = "deltaY"in w ? ip(w) : fi(w)
              , p = t.current.filter(function(S) {
                return S.name === w.type && (S.target === w.target || w.target === S.shadowParent) && iP(S.delta, y)
            })[0];
            if (p && p.should) {
                w.cancelable && w.preventDefault();
                return
            }
            if (!p) {
                var x = (i.current.shards || []).map(lp).filter(Boolean).filter(function(S) {
                    return S.contains(w.target)
                })
                  , N = x.length > 0 ? l(w, x[0]) : !i.current.noIsolation;
                N && w.cancelable && w.preventDefault()
            }
        }
    }, [])
      , u = m.useCallback(function(v, w, y, p) {
        var x = {
            name: v,
            delta: w,
            target: y,
            should: p,
            shadowParent: dP(y)
        };
        t.current.push(x),
        setTimeout(function() {
            t.current = t.current.filter(function(N) {
                return N !== x
            })
        }, 1)
    }, [])
      , d = m.useCallback(function(v) {
        n.current = fi(v),
        r.current = void 0
    }, [])
      , f = m.useCallback(function(v) {
        u(v.type, ip(v), v.target, l(v, e.lockRef.current))
    }, [])
      , g = m.useCallback(function(v) {
        u(v.type, fi(v), v.target, l(v, e.lockRef.current))
    }, []);
    m.useEffect(function() {
        return yo.push(s),
        e.setCallbacks({
            onScrollCapture: f,
            onWheelCapture: f,
            onTouchMoveCapture: g
        }),
        document.addEventListener("wheel", c, go),
        document.addEventListener("touchmove", c, go),
        document.addEventListener("touchstart", d, go),
        function() {
            yo = yo.filter(function(v) {
                return v !== s
            }),
            document.removeEventListener("wheel", c, go),
            document.removeEventListener("touchmove", c, go),
            document.removeEventListener("touchstart", d, go)
        }
    }, []);
    var h = e.removeScrollBar
      , b = e.inert;
    return m.createElement(m.Fragment, null, b ? m.createElement(s, {
        styles: lP(o)
    }) : null, h ? m.createElement(ZE, {
        noRelative: e.noRelative,
        gapMode: e.gapMode
    }) : null)
}
function dP(e) {
    for (var t = null; e !== null; )
        e instanceof ShadowRoot && (t = e.host,
        e = e.host),
        e = e.parentNode;
    return t
}
const fP = $E(zx, uP);
var Af = m.forwardRef(function(e, t) {
    return m.createElement(Vl, fn({}, e, {
        ref: t,
        sideCar: fP
    }))
});
Af.classNames = Vl.classNames;
var mP = [" ", "Enter", "ArrowUp", "ArrowDown"]
  , hP = [" ", "Enter"]
  , eo = "Select"
  , [Ul,Yl,pP] = mf(eo)
  , [xs,kR] = io(eo, [pP, Fl])
  , Kl = Fl()
  , [vP,Er] = xs(eo)
  , [gP,yP] = xs(eo)
  , Vx = e => {
    const {__scopeSelect: t, children: n, open: r, defaultOpen: o, onOpenChange: s, value: i, defaultValue: l, onValueChange: c, dir: u, name: d, autoComplete: f, disabled: g, required: h, form: b} = e
      , v = Kl(t)
      , [w,y] = m.useState(null)
      , [p,x] = m.useState(null)
      , [N,S] = m.useState(!1)
      , k = Rx(u)
      , [C,T] = ma({
        prop: r,
        defaultProp: o ?? !1,
        onChange: s,
        caller: eo
    })
      , [D,R] = ma({
        prop: i,
        defaultProp: l,
        onChange: c,
        caller: eo
    })
      , F = m.useRef(null)
      , A = w ? b || !!w.closest("form") : !0
      , [W,O] = m.useState(new Set)
      , V = Array.from(W).map($ => $.props.value).join(";");
    return a.jsx(vC, {
        ...v,
        children: a.jsxs(vP, {
            required: h,
            scope: t,
            trigger: w,
            onTriggerChange: y,
            valueNode: p,
            onValueNodeChange: x,
            valueNodeHasChildren: N,
            onValueNodeHasChildrenChange: S,
            contentId: zo(),
            value: D,
            onValueChange: R,
            open: C,
            onOpenChange: T,
            dir: k,
            triggerPointerDownPosRef: F,
            disabled: g,
            children: [a.jsx(Ul.Provider, {
                scope: t,
                children: a.jsx(gP, {
                    scope: e.__scopeSelect,
                    onNativeOptionAdd: m.useCallback($ => {
                        O(M => new Set(M).add($))
                    }
                    , []),
                    onNativeOptionRemove: m.useCallback($ => {
                        O(M => {
                            const j = new Set(M);
                            return j.delete($),
                            j
                        }
                        )
                    }
                    , []),
                    children: n
                })
            }), A ? a.jsxs(h0, {
                "aria-hidden": !0,
                required: h,
                tabIndex: -1,
                name: d,
                autoComplete: f,
                value: D,
                onChange: $ => R($.target.value),
                disabled: g,
                form: b,
                children: [D === void 0 ? a.jsx("option", {
                    value: ""
                }) : null, Array.from(W)]
            }, V) : null]
        })
    })
}
;
Vx.displayName = eo;
var Ux = "SelectTrigger"
  , Yx = m.forwardRef( (e, t) => {
    const {__scopeSelect: n, disabled: r=!1, ...o} = e
      , s = Kl(n)
      , i = Er(Ux, n)
      , l = i.disabled || r
      , c = fe(t, i.onTriggerChange)
      , u = Yl(n)
      , d = m.useRef("touch")
      , [f,g,h] = v0(v => {
        const w = u().filter(x => !x.disabled)
          , y = w.find(x => x.value === i.value)
          , p = g0(w, v, y);
        p !== void 0 && i.onValueChange(p.value)
    }
    )
      , b = v => {
        l || (i.onOpenChange(!0),
        h()),
        v && (i.triggerPointerDownPosRef.current = {
            x: Math.round(v.pageX),
            y: Math.round(v.pageY)
        })
    }
    ;
    return a.jsx(Zy, {
        asChild: !0,
        ...s,
        children: a.jsx(te.button, {
            type: "button",
            role: "combobox",
            "aria-controls": i.contentId,
            "aria-expanded": i.open,
            "aria-required": i.required,
            "aria-autocomplete": "none",
            dir: i.dir,
            "data-state": i.open ? "open" : "closed",
            disabled: l,
            "data-disabled": l ? "" : void 0,
            "data-placeholder": p0(i.value) ? "" : void 0,
            ...o,
            ref: c,
            onClick: Q(o.onClick, v => {
                v.currentTarget.focus(),
                d.current !== "mouse" && b(v)
            }
            ),
            onPointerDown: Q(o.onPointerDown, v => {
                d.current = v.pointerType;
                const w = v.target;
                w.hasPointerCapture(v.pointerId) && w.releasePointerCapture(v.pointerId),
                v.button === 0 && v.ctrlKey === !1 && v.pointerType === "mouse" && (b(v),
                v.preventDefault())
            }
            ),
            onKeyDown: Q(o.onKeyDown, v => {
                const w = f.current !== "";
                !(v.ctrlKey || v.altKey || v.metaKey) && v.key.length === 1 && g(v.key),
                !(w && v.key === " ") && mP.includes(v.key) && (b(),
                v.preventDefault())
            }
            )
        })
    })
}
);
Yx.displayName = Ux;
var Kx = "SelectValue"
  , Qx = m.forwardRef( (e, t) => {
    const {__scopeSelect: n, className: r, style: o, children: s, placeholder: i="", ...l} = e
      , c = Er(Kx, n)
      , {onValueNodeHasChildrenChange: u} = c
      , d = s !== void 0
      , f = fe(t, c.onValueNodeChange);
    return Ue( () => {
        u(d)
    }
    , [u, d]),
    a.jsx(te.span, {
        ...l,
        ref: f,
        style: {
            pointerEvents: "none"
        },
        children: p0(c.value) ? a.jsx(a.Fragment, {
            children: i
        }) : s
    })
}
);
Qx.displayName = Kx;
var xP = "SelectIcon"
  , Gx = m.forwardRef( (e, t) => {
    const {__scopeSelect: n, children: r, ...o} = e;
    return a.jsx(te.span, {
        "aria-hidden": !0,
        ...o,
        ref: t,
        children: r || "▼"
    })
}
);
Gx.displayName = xP;
var wP = "SelectPortal"
  , qx = e => a.jsx(Rl, {
    asChild: !0,
    ...e
});
qx.displayName = wP;
var to = "SelectContent"
  , Xx = m.forwardRef( (e, t) => {
    const n = Er(to, e.__scopeSelect)
      , [r,o] = m.useState();
    if (Ue( () => {
        o(new DocumentFragment)
    }
    , []),
    !n.open) {
        const s = r;
        return s ? ao.createPortal(a.jsx(Jx, {
            scope: e.__scopeSelect,
            children: a.jsx(Ul.Slot, {
                scope: e.__scopeSelect,
                children: a.jsx("div", {
                    children: e.children
                })
            })
        }), s) : null
    }
    return a.jsx(Zx, {
        ...e,
        ref: t
    })
}
);
Xx.displayName = to;
var $t = 10
  , [Jx,Pr] = xs(to)
  , bP = "SelectContentImpl"
  , NP = rs("SelectContent.RemoveScroll")
  , Zx = m.forwardRef( (e, t) => {
    const {__scopeSelect: n, position: r="item-aligned", onCloseAutoFocus: o, onEscapeKeyDown: s, onPointerDownOutside: i, side: l, sideOffset: c, align: u, alignOffset: d, arrowPadding: f, collisionBoundary: g, collisionPadding: h, sticky: b, hideWhenDetached: v, avoidCollisions: w, ...y} = e
      , p = Er(to, n)
      , [x,N] = m.useState(null)
      , [S,k] = m.useState(null)
      , C = fe(t, z => N(z))
      , [T,D] = m.useState(null)
      , [R,F] = m.useState(null)
      , A = Yl(n)
      , [W,O] = m.useState(!1)
      , V = m.useRef(!1);
    m.useEffect( () => {
        if (x)
            return Ix(x)
    }
    , [x]),
    _x();
    const $ = m.useCallback(z => {
        const [me,...Re] = A().map(ce => ce.ref.current)
          , [de] = Re.slice(-1)
          , oe = document.activeElement;
        for (const ce of z)
            if (ce === oe || (ce == null || ce.scrollIntoView({
                block: "nearest"
            }),
            ce === me && S && (S.scrollTop = 0),
            ce === de && S && (S.scrollTop = S.scrollHeight),
            ce == null || ce.focus(),
            document.activeElement !== oe))
                return
    }
    , [A, S])
      , M = m.useCallback( () => $([T, x]), [$, T, x]);
    m.useEffect( () => {
        W && M()
    }
    , [W, M]);
    const {onOpenChange: j, triggerPointerDownPosRef: E} = p;
    m.useEffect( () => {
        if (x) {
            let z = {
                x: 0,
                y: 0
            };
            const me = de => {
                var oe, ce;
                z = {
                    x: Math.abs(Math.round(de.pageX) - (((oe = E.current) == null ? void 0 : oe.x) ?? 0)),
                    y: Math.abs(Math.round(de.pageY) - (((ce = E.current) == null ? void 0 : ce.y) ?? 0))
                }
            }
              , Re = de => {
                z.x <= 10 && z.y <= 10 ? de.preventDefault() : x.contains(de.target) || j(!1),
                document.removeEventListener("pointermove", me),
                E.current = null
            }
            ;
            return E.current !== null && (document.addEventListener("pointermove", me),
            document.addEventListener("pointerup", Re, {
                capture: !0,
                once: !0
            })),
            () => {
                document.removeEventListener("pointermove", me),
                document.removeEventListener("pointerup", Re, {
                    capture: !0
                })
            }
        }
    }
    , [x, j, E]),
    m.useEffect( () => {
        const z = () => j(!1);
        return window.addEventListener("blur", z),
        window.addEventListener("resize", z),
        () => {
            window.removeEventListener("blur", z),
            window.removeEventListener("resize", z)
        }
    }
    , [j]);
    const [L,U] = v0(z => {
        const me = A().filter(oe => !oe.disabled)
          , Re = me.find(oe => oe.ref.current === document.activeElement)
          , de = g0(me, z, Re);
        de && setTimeout( () => de.ref.current.focus())
    }
    )
      , H = m.useCallback( (z, me, Re) => {
        const de = !V.current && !Re;
        (p.value !== void 0 && p.value === me || de) && (D(z),
        de && (V.current = !0))
    }
    , [p.value])
      , J = m.useCallback( () => x == null ? void 0 : x.focus(), [x])
      , G = m.useCallback( (z, me, Re) => {
        const de = !V.current && !Re;
        (p.value !== void 0 && p.value === me || de) && F(z)
    }
    , [p.value])
      , xe = r === "popper" ? id : e0
      , Me = xe === id ? {
        side: l,
        sideOffset: c,
        align: u,
        alignOffset: d,
        arrowPadding: f,
        collisionBoundary: g,
        collisionPadding: h,
        sticky: b,
        hideWhenDetached: v,
        avoidCollisions: w
    } : {};
    return a.jsx(Jx, {
        scope: n,
        content: x,
        viewport: S,
        onViewportChange: k,
        itemRefCallback: H,
        selectedItem: T,
        onItemLeave: J,
        itemTextRefCallback: G,
        focusSelectedItem: M,
        selectedItemText: R,
        position: r,
        isPositioned: W,
        searchRef: L,
        children: a.jsx(Af, {
            as: NP,
            allowPinchZoom: !0,
            children: a.jsx(Of, {
                asChild: !0,
                trapped: p.open,
                onMountAutoFocus: z => {
                    z.preventDefault()
                }
                ,
                onUnmountAutoFocus: Q(o, z => {
                    var me;
                    (me = p.trigger) == null || me.focus({
                        preventScroll: !0
                    }),
                    z.preventDefault()
                }
                ),
                children: a.jsx(Ta, {
                    asChild: !0,
                    disableOutsidePointerEvents: !0,
                    onEscapeKeyDown: s,
                    onPointerDownOutside: i,
                    onFocusOutside: z => z.preventDefault(),
                    onDismiss: () => p.onOpenChange(!1),
                    children: a.jsx(xe, {
                        role: "listbox",
                        id: p.contentId,
                        "data-state": p.open ? "open" : "closed",
                        dir: p.dir,
                        onContextMenu: z => z.preventDefault(),
                        ...y,
                        ...Me,
                        onPlaced: () => O(!0),
                        ref: C,
                        style: {
                            display: "flex",
                            flexDirection: "column",
                            outline: "none",
                            ...y.style
                        },
                        onKeyDown: Q(y.onKeyDown, z => {
                            const me = z.ctrlKey || z.altKey || z.metaKey;
                            if (z.key === "Tab" && z.preventDefault(),
                            !me && z.key.length === 1 && U(z.key),
                            ["ArrowUp", "ArrowDown", "Home", "End"].includes(z.key)) {
                                let de = A().filter(oe => !oe.disabled).map(oe => oe.ref.current);
                                if (["ArrowUp", "End"].includes(z.key) && (de = de.slice().reverse()),
                                ["ArrowUp", "ArrowDown"].includes(z.key)) {
                                    const oe = z.target
                                      , ce = de.indexOf(oe);
                                    de = de.slice(ce + 1)
                                }
                                setTimeout( () => $(de)),
                                z.preventDefault()
                            }
                        }
                        )
                    })
                })
            })
        })
    })
}
);
Zx.displayName = bP;
var SP = "SelectItemAlignedPosition"
  , e0 = m.forwardRef( (e, t) => {
    const {__scopeSelect: n, onPlaced: r, ...o} = e
      , s = Er(to, n)
      , i = Pr(to, n)
      , [l,c] = m.useState(null)
      , [u,d] = m.useState(null)
      , f = fe(t, C => d(C))
      , g = Yl(n)
      , h = m.useRef(!1)
      , b = m.useRef(!0)
      , {viewport: v, selectedItem: w, selectedItemText: y, focusSelectedItem: p} = i
      , x = m.useCallback( () => {
        if (s.trigger && s.valueNode && l && u && v && w && y) {
            const C = s.trigger.getBoundingClientRect()
              , T = u.getBoundingClientRect()
              , D = s.valueNode.getBoundingClientRect()
              , R = y.getBoundingClientRect();
            if (s.dir !== "rtl") {
                const oe = R.left - T.left
                  , ce = D.left - oe
                  , Ye = C.left - ce
                  , jt = C.width + Ye
                  , Tr = Math.max(jt, T.width)
                  , $n = window.innerWidth - $t
                  , Mr = ul(ce, [$t, Math.max($t, $n - Tr)]);
                l.style.minWidth = jt + "px",
                l.style.left = Mr + "px"
            } else {
                const oe = T.right - R.right
                  , ce = window.innerWidth - D.right - oe
                  , Ye = window.innerWidth - C.right - ce
                  , jt = C.width + Ye
                  , Tr = Math.max(jt, T.width)
                  , $n = window.innerWidth - $t
                  , Mr = ul(ce, [$t, Math.max($t, $n - Tr)]);
                l.style.minWidth = jt + "px",
                l.style.right = Mr + "px"
            }
            const F = g()
              , A = window.innerHeight - $t * 2
              , W = v.scrollHeight
              , O = window.getComputedStyle(u)
              , V = parseInt(O.borderTopWidth, 10)
              , $ = parseInt(O.paddingTop, 10)
              , M = parseInt(O.borderBottomWidth, 10)
              , j = parseInt(O.paddingBottom, 10)
              , E = V + $ + W + j + M
              , L = Math.min(w.offsetHeight * 5, E)
              , U = window.getComputedStyle(v)
              , H = parseInt(U.paddingTop, 10)
              , J = parseInt(U.paddingBottom, 10)
              , G = C.top + C.height / 2 - $t
              , xe = A - G
              , Me = w.offsetHeight / 2
              , z = w.offsetTop + Me
              , me = V + $ + z
              , Re = E - me;
            if (me <= G) {
                const oe = F.length > 0 && w === F[F.length - 1].ref.current;
                l.style.bottom = "0px";
                const ce = u.clientHeight - v.offsetTop - v.offsetHeight
                  , Ye = Math.max(xe, Me + (oe ? J : 0) + ce + M)
                  , jt = me + Ye;
                l.style.height = jt + "px"
            } else {
                const oe = F.length > 0 && w === F[0].ref.current;
                l.style.top = "0px";
                const Ye = Math.max(G, V + v.offsetTop + (oe ? H : 0) + Me) + Re;
                l.style.height = Ye + "px",
                v.scrollTop = me - G + v.offsetTop
            }
            l.style.margin = `${$t}px 0`,
            l.style.minHeight = L + "px",
            l.style.maxHeight = A + "px",
            r == null || r(),
            requestAnimationFrame( () => h.current = !0)
        }
    }
    , [g, s.trigger, s.valueNode, l, u, v, w, y, s.dir, r]);
    Ue( () => x(), [x]);
    const [N,S] = m.useState();
    Ue( () => {
        u && S(window.getComputedStyle(u).zIndex)
    }
    , [u]);
    const k = m.useCallback(C => {
        C && b.current === !0 && (x(),
        p == null || p(),
        b.current = !1)
    }
    , [x, p]);
    return a.jsx(CP, {
        scope: n,
        contentWrapper: l,
        shouldExpandOnScrollRef: h,
        onScrollButtonChange: k,
        children: a.jsx("div", {
            ref: c,
            style: {
                display: "flex",
                flexDirection: "column",
                position: "fixed",
                zIndex: N
            },
            children: a.jsx(te.div, {
                ...o,
                ref: f,
                style: {
                    boxSizing: "border-box",
                    maxHeight: "100%",
                    ...o.style
                }
            })
        })
    })
}
);
e0.displayName = SP;
var jP = "SelectPopperPosition"
  , id = m.forwardRef( (e, t) => {
    const {__scopeSelect: n, align: r="start", collisionPadding: o=$t, ...s} = e
      , i = Kl(n);
    return a.jsx(ex, {
        ...i,
        ...s,
        ref: t,
        align: r,
        collisionPadding: o,
        style: {
            boxSizing: "border-box",
            ...s.style,
            "--radix-select-content-transform-origin": "var(--radix-popper-transform-origin)",
            "--radix-select-content-available-width": "var(--radix-popper-available-width)",
            "--radix-select-content-available-height": "var(--radix-popper-available-height)",
            "--radix-select-trigger-width": "var(--radix-popper-anchor-width)",
            "--radix-select-trigger-height": "var(--radix-popper-anchor-height)"
        }
    })
}
);
id.displayName = jP;
var [CP,If] = xs(to, {})
  , ld = "SelectViewport"
  , t0 = m.forwardRef( (e, t) => {
    const {__scopeSelect: n, nonce: r, ...o} = e
      , s = Pr(ld, n)
      , i = If(ld, n)
      , l = fe(t, s.onViewportChange)
      , c = m.useRef(0);
    return a.jsxs(a.Fragment, {
        children: [a.jsx("style", {
            dangerouslySetInnerHTML: {
                __html: "[data-radix-select-viewport]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}[data-radix-select-viewport]::-webkit-scrollbar{display:none}"
            },
            nonce: r
        }), a.jsx(Ul.Slot, {
            scope: n,
            children: a.jsx(te.div, {
                "data-radix-select-viewport": "",
                role: "presentation",
                ...o,
                ref: l,
                style: {
                    position: "relative",
                    flex: 1,
                    overflow: "hidden auto",
                    ...o.style
                },
                onScroll: Q(o.onScroll, u => {
                    const d = u.currentTarget
                      , {contentWrapper: f, shouldExpandOnScrollRef: g} = i;
                    if (g != null && g.current && f) {
                        const h = Math.abs(c.current - d.scrollTop);
                        if (h > 0) {
                            const b = window.innerHeight - $t * 2
                              , v = parseFloat(f.style.minHeight)
                              , w = parseFloat(f.style.height)
                              , y = Math.max(v, w);
                            if (y < b) {
                                const p = y + h
                                  , x = Math.min(b, p)
                                  , N = p - x;
                                f.style.height = x + "px",
                                f.style.bottom === "0px" && (d.scrollTop = N > 0 ? N : 0,
                                f.style.justifyContent = "flex-end")
                            }
                        }
                    }
                    c.current = d.scrollTop
                }
                )
            })
        })]
    })
}
);
t0.displayName = ld;
var n0 = "SelectGroup"
  , [kP,EP] = xs(n0)
  , PP = m.forwardRef( (e, t) => {
    const {__scopeSelect: n, ...r} = e
      , o = zo();
    return a.jsx(kP, {
        scope: n,
        id: o,
        children: a.jsx(te.div, {
            role: "group",
            "aria-labelledby": o,
            ...r,
            ref: t
        })
    })
}
);
PP.displayName = n0;
var r0 = "SelectLabel"
  , o0 = m.forwardRef( (e, t) => {
    const {__scopeSelect: n, ...r} = e
      , o = EP(r0, n);
    return a.jsx(te.div, {
        id: o.id,
        ...r,
        ref: t
    })
}
);
o0.displayName = r0;
var dl = "SelectItem"
  , [TP,s0] = xs(dl)
  , a0 = m.forwardRef( (e, t) => {
    const {__scopeSelect: n, value: r, disabled: o=!1, textValue: s, ...i} = e
      , l = Er(dl, n)
      , c = Pr(dl, n)
      , u = l.value === r
      , [d,f] = m.useState(s ?? "")
      , [g,h] = m.useState(!1)
      , b = fe(t, p => {
        var x;
        return (x = c.itemRefCallback) == null ? void 0 : x.call(c, p, r, o)
    }
    )
      , v = zo()
      , w = m.useRef("touch")
      , y = () => {
        o || (l.onValueChange(r),
        l.onOpenChange(!1))
    }
    ;
    if (r === "")
        throw new Error("A <Select.Item /> must have a value prop that is not an empty string. This is because the Select value can be set to an empty string to clear the selection and show the placeholder.");
    return a.jsx(TP, {
        scope: n,
        value: r,
        disabled: o,
        textId: v,
        isSelected: u,
        onItemTextChange: m.useCallback(p => {
            f(x => x || ((p == null ? void 0 : p.textContent) ?? "").trim())
        }
        , []),
        children: a.jsx(Ul.ItemSlot, {
            scope: n,
            value: r,
            disabled: o,
            textValue: d,
            children: a.jsx(te.div, {
                role: "option",
                "aria-labelledby": v,
                "data-highlighted": g ? "" : void 0,
                "aria-selected": u && g,
                "data-state": u ? "checked" : "unchecked",
                "aria-disabled": o || void 0,
                "data-disabled": o ? "" : void 0,
                tabIndex: o ? void 0 : -1,
                ...i,
                ref: b,
                onFocus: Q(i.onFocus, () => h(!0)),
                onBlur: Q(i.onBlur, () => h(!1)),
                onClick: Q(i.onClick, () => {
                    w.current !== "mouse" && y()
                }
                ),
                onPointerUp: Q(i.onPointerUp, () => {
                    w.current === "mouse" && y()
                }
                ),
                onPointerDown: Q(i.onPointerDown, p => {
                    w.current = p.pointerType
                }
                ),
                onPointerMove: Q(i.onPointerMove, p => {
                    var x;
                    w.current = p.pointerType,
                    o ? (x = c.onItemLeave) == null || x.call(c) : w.current === "mouse" && p.currentTarget.focus({
                        preventScroll: !0
                    })
                }
                ),
                onPointerLeave: Q(i.onPointerLeave, p => {
                    var x;
                    p.currentTarget === document.activeElement && ((x = c.onItemLeave) == null || x.call(c))
                }
                ),
                onKeyDown: Q(i.onKeyDown, p => {
                    var N;
                    ((N = c.searchRef) == null ? void 0 : N.current) !== "" && p.key === " " || (hP.includes(p.key) && y(),
                    p.key === " " && p.preventDefault())
                }
                )
            })
        })
    })
}
);
a0.displayName = dl;
var zs = "SelectItemText"
  , i0 = m.forwardRef( (e, t) => {
    const {__scopeSelect: n, className: r, style: o, ...s} = e
      , i = Er(zs, n)
      , l = Pr(zs, n)
      , c = s0(zs, n)
      , u = yP(zs, n)
      , [d,f] = m.useState(null)
      , g = fe(t, y => f(y), c.onItemTextChange, y => {
        var p;
        return (p = l.itemTextRefCallback) == null ? void 0 : p.call(l, y, c.value, c.disabled)
    }
    )
      , h = d == null ? void 0 : d.textContent
      , b = m.useMemo( () => a.jsx("option", {
        value: c.value,
        disabled: c.disabled,
        children: h
    }, c.value), [c.disabled, c.value, h])
      , {onNativeOptionAdd: v, onNativeOptionRemove: w} = u;
    return Ue( () => (v(b),
    () => w(b)), [v, w, b]),
    a.jsxs(a.Fragment, {
        children: [a.jsx(te.span, {
            id: c.textId,
            ...s,
            ref: g
        }), c.isSelected && i.valueNode && !i.valueNodeHasChildren ? ao.createPortal(s.children, i.valueNode) : null]
    })
}
);
i0.displayName = zs;
var l0 = "SelectItemIndicator"
  , c0 = m.forwardRef( (e, t) => {
    const {__scopeSelect: n, ...r} = e;
    return s0(l0, n).isSelected ? a.jsx(te.span, {
        "aria-hidden": !0,
        ...r,
        ref: t
    }) : null
}
);
c0.displayName = l0;
var cd = "SelectScrollUpButton"
  , u0 = m.forwardRef( (e, t) => {
    const n = Pr(cd, e.__scopeSelect)
      , r = If(cd, e.__scopeSelect)
      , [o,s] = m.useState(!1)
      , i = fe(t, r.onScrollButtonChange);
    return Ue( () => {
        if (n.viewport && n.isPositioned) {
            let l = function() {
                const u = c.scrollTop > 0;
                s(u)
            };
            const c = n.viewport;
            return l(),
            c.addEventListener("scroll", l),
            () => c.removeEventListener("scroll", l)
        }
    }
    , [n.viewport, n.isPositioned]),
    o ? a.jsx(f0, {
        ...e,
        ref: i,
        onAutoScroll: () => {
            const {viewport: l, selectedItem: c} = n;
            l && c && (l.scrollTop = l.scrollTop - c.offsetHeight)
        }
    }) : null
}
);
u0.displayName = cd;
var ud = "SelectScrollDownButton"
  , d0 = m.forwardRef( (e, t) => {
    const n = Pr(ud, e.__scopeSelect)
      , r = If(ud, e.__scopeSelect)
      , [o,s] = m.useState(!1)
      , i = fe(t, r.onScrollButtonChange);
    return Ue( () => {
        if (n.viewport && n.isPositioned) {
            let l = function() {
                const u = c.scrollHeight - c.clientHeight
                  , d = Math.ceil(c.scrollTop) < u;
                s(d)
            };
            const c = n.viewport;
            return l(),
            c.addEventListener("scroll", l),
            () => c.removeEventListener("scroll", l)
        }
    }
    , [n.viewport, n.isPositioned]),
    o ? a.jsx(f0, {
        ...e,
        ref: i,
        onAutoScroll: () => {
            const {viewport: l, selectedItem: c} = n;
            l && c && (l.scrollTop = l.scrollTop + c.offsetHeight)
        }
    }) : null
}
);
d0.displayName = ud;
var f0 = m.forwardRef( (e, t) => {
    const {__scopeSelect: n, onAutoScroll: r, ...o} = e
      , s = Pr("SelectScrollButton", n)
      , i = m.useRef(null)
      , l = Yl(n)
      , c = m.useCallback( () => {
        i.current !== null && (window.clearInterval(i.current),
        i.current = null)
    }
    , []);
    return m.useEffect( () => () => c(), [c]),
    Ue( () => {
        var d;
        const u = l().find(f => f.ref.current === document.activeElement);
        (d = u == null ? void 0 : u.ref.current) == null || d.scrollIntoView({
            block: "nearest"
        })
    }
    , [l]),
    a.jsx(te.div, {
        "aria-hidden": !0,
        ...o,
        ref: t,
        style: {
            flexShrink: 0,
            ...o.style
        },
        onPointerDown: Q(o.onPointerDown, () => {
            i.current === null && (i.current = window.setInterval(r, 50))
        }
        ),
        onPointerMove: Q(o.onPointerMove, () => {
            var u;
            (u = s.onItemLeave) == null || u.call(s),
            i.current === null && (i.current = window.setInterval(r, 50))
        }
        ),
        onPointerLeave: Q(o.onPointerLeave, () => {
            c()
        }
        )
    })
}
)
  , MP = "SelectSeparator"
  , m0 = m.forwardRef( (e, t) => {
    const {__scopeSelect: n, ...r} = e;
    return a.jsx(te.div, {
        "aria-hidden": !0,
        ...r,
        ref: t
    })
}
);
m0.displayName = MP;
var dd = "SelectArrow"
  , RP = m.forwardRef( (e, t) => {
    const {__scopeSelect: n, ...r} = e
      , o = Kl(n)
      , s = Er(dd, n)
      , i = Pr(dd, n);
    return s.open && i.position === "popper" ? a.jsx(tx, {
        ...o,
        ...r,
        ref: t
    }) : null
}
);
RP.displayName = dd;
var _P = "SelectBubbleInput"
  , h0 = m.forwardRef( ({__scopeSelect: e, value: t, ...n}, r) => {
    const o = m.useRef(null)
      , s = fe(r, o)
      , i = Ox(t);
    return m.useEffect( () => {
        const l = o.current;
        if (!l)
            return;
        const c = window.HTMLSelectElement.prototype
          , d = Object.getOwnPropertyDescriptor(c, "value").set;
        if (i !== t && d) {
            const f = new Event("change",{
                bubbles: !0
            });
            d.call(l, t),
            l.dispatchEvent(f)
        }
    }
    , [i, t]),
    a.jsx(te.select, {
        ...n,
        style: {
            ...Qg,
            ...n.style
        },
        ref: s,
        defaultValue: t
    })
}
);
h0.displayName = _P;
function p0(e) {
    return e === "" || e === void 0
}
function v0(e) {
    const t = Zt(e)
      , n = m.useRef("")
      , r = m.useRef(0)
      , o = m.useCallback(i => {
        const l = n.current + i;
        t(l),
        function c(u) {
            n.current = u,
            window.clearTimeout(r.current),
            u !== "" && (r.current = window.setTimeout( () => c(""), 1e3))
        }(l)
    }
    , [t])
      , s = m.useCallback( () => {
        n.current = "",
        window.clearTimeout(r.current)
    }
    , []);
    return m.useEffect( () => () => window.clearTimeout(r.current), []),
    [n, o, s]
}
function g0(e, t, n) {
    const o = t.length > 1 && Array.from(t).every(u => u === t[0]) ? t[0] : t
      , s = n ? e.indexOf(n) : -1;
    let i = DP(e, Math.max(s, 0));
    o.length === 1 && (i = i.filter(u => u !== n));
    const c = i.find(u => u.textValue.toLowerCase().startsWith(o.toLowerCase()));
    return c !== n ? c : void 0
}
function DP(e, t) {
    return e.map( (n, r) => e[(t + r) % e.length])
}
var OP = Vx
  , y0 = Yx
  , AP = Qx
  , IP = Gx
  , LP = qx
  , x0 = Xx
  , FP = t0
  , w0 = o0
  , b0 = a0
  , zP = i0
  , $P = c0
  , N0 = u0
  , S0 = d0
  , j0 = m0;
const Kt = OP
  , Qt = AP
  , Mt = m.forwardRef( ({className: e, children: t, ...n}, r) => a.jsxs(y0, {
    ref: r,
    className: re("flex h-10 w-full items-center justify-between rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 [&>span]:line-clamp-1", e),
    ...n,
    children: [t, a.jsx(IP, {
        asChild: !0,
        children: a.jsx(yy, {
            className: "h-4 w-4 opacity-50"
        })
    })]
}));
Mt.displayName = y0.displayName;
const C0 = m.forwardRef( ({className: e, ...t}, n) => a.jsx(N0, {
    ref: n,
    className: re("flex cursor-default items-center justify-center py-1", e),
    ...t,
    children: a.jsx(SS, {
        className: "h-4 w-4"
    })
}));
C0.displayName = N0.displayName;
const k0 = m.forwardRef( ({className: e, ...t}, n) => a.jsx(S0, {
    ref: n,
    className: re("flex cursor-default items-center justify-center py-1", e),
    ...t,
    children: a.jsx(yy, {
        className: "h-4 w-4"
    })
}));
k0.displayName = S0.displayName;
const Rt = m.forwardRef( ({className: e, children: t, position: n="popper", ...r}, o) => a.jsx(LP, {
    children: a.jsxs(x0, {
        ref: o,
        className: re("relative z-50 max-h-96 min-w-[8rem] overflow-hidden rounded-md border bg-popover text-popover-foreground shadow-md data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2", n === "popper" && "data-[side=bottom]:translate-y-1 data-[side=left]:-translate-x-1 data-[side=right]:translate-x-1 data-[side=top]:-translate-y-1", e),
        position: n,
        ...r,
        children: [a.jsx(C0, {}), a.jsx(FP, {
            className: re("p-1", n === "popper" && "h-[var(--radix-select-trigger-height)] w-full min-w-[var(--radix-select-trigger-width)]"),
            children: t
        }), a.jsx(k0, {})]
    })
}));
Rt.displayName = x0.displayName;
const BP = m.forwardRef( ({className: e, ...t}, n) => a.jsx(w0, {
    ref: n,
    className: re("py-1.5 pl-8 pr-2 text-sm font-semibold", e),
    ...t
}));
BP.displayName = w0.displayName;
const Y = m.forwardRef( ({className: e, children: t, ...n}, r) => a.jsxs(b0, {
    ref: r,
    className: re("relative flex w-full cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none data-[disabled]:pointer-events-none data-[disabled]:opacity-50 focus:bg-accent focus:text-accent-foreground", e),
    ...n,
    children: [a.jsx("span", {
        className: "absolute left-2 flex h-3.5 w-3.5 items-center justify-center",
        children: a.jsx($P, {
            children: a.jsx(wS, {
                className: "h-4 w-4"
            })
        })
    }), a.jsx(zP, {
        children: t
    })]
}));
Y.displayName = b0.displayName;
const WP = m.forwardRef( ({className: e, ...t}, n) => a.jsx(j0, {
    ref: n,
    className: re("-mx-1 my-1 h-px bg-muted", e),
    ...t
}));
WP.displayName = j0.displayName;
var Ql = "Dialog"
  , [E0,ER] = io(Ql)
  , [HP,on] = E0(Ql)
  , P0 = e => {
    const {__scopeDialog: t, children: n, open: r, defaultOpen: o, onOpenChange: s, modal: i=!0} = e
      , l = m.useRef(null)
      , c = m.useRef(null)
      , [u,d] = ma({
        prop: r,
        defaultProp: o ?? !1,
        onChange: s,
        caller: Ql
    });
    return a.jsx(HP, {
        scope: t,
        triggerRef: l,
        contentRef: c,
        contentId: zo(),
        titleId: zo(),
        descriptionId: zo(),
        open: u,
        onOpenChange: d,
        onOpenToggle: m.useCallback( () => d(f => !f), [d]),
        modal: i,
        children: n
    })
}
;
P0.displayName = Ql;
var T0 = "DialogTrigger"
  , VP = m.forwardRef( (e, t) => {
    const {__scopeDialog: n, ...r} = e
      , o = on(T0, n)
      , s = fe(t, o.triggerRef);
    return a.jsx(te.button, {
        type: "button",
        "aria-haspopup": "dialog",
        "aria-expanded": o.open,
        "aria-controls": o.contentId,
        "data-state": zf(o.open),
        ...r,
        ref: s,
        onClick: Q(e.onClick, o.onOpenToggle)
    })
}
);
VP.displayName = T0;
var Lf = "DialogPortal"
  , [UP,M0] = E0(Lf, {
    forceMount: void 0
})
  , R0 = e => {
    const {__scopeDialog: t, forceMount: n, children: r, container: o} = e
      , s = on(Lf, t);
    return a.jsx(UP, {
        scope: t,
        forceMount: n,
        children: m.Children.map(r, i => a.jsx(ms, {
            present: n || s.open,
            children: a.jsx(Rl, {
                asChild: !0,
                container: o,
                children: i
            })
        }))
    })
}
;
R0.displayName = Lf;
var fl = "DialogOverlay"
  , _0 = m.forwardRef( (e, t) => {
    const n = M0(fl, e.__scopeDialog)
      , {forceMount: r=n.forceMount, ...o} = e
      , s = on(fl, e.__scopeDialog);
    return s.modal ? a.jsx(ms, {
        present: r || s.open,
        children: a.jsx(KP, {
            ...o,
            ref: t
        })
    }) : null
}
);
_0.displayName = fl;
var YP = rs("DialogOverlay.RemoveScroll")
  , KP = m.forwardRef( (e, t) => {
    const {__scopeDialog: n, ...r} = e
      , o = on(fl, n);
    return a.jsx(Af, {
        as: YP,
        allowPinchZoom: !0,
        shards: [o.contentRef],
        children: a.jsx(te.div, {
            "data-state": zf(o.open),
            ...r,
            ref: t,
            style: {
                pointerEvents: "auto",
                ...r.style
            }
        })
    })
}
)
  , no = "DialogContent"
  , D0 = m.forwardRef( (e, t) => {
    const n = M0(no, e.__scopeDialog)
      , {forceMount: r=n.forceMount, ...o} = e
      , s = on(no, e.__scopeDialog);
    return a.jsx(ms, {
        present: r || s.open,
        children: s.modal ? a.jsx(QP, {
            ...o,
            ref: t
        }) : a.jsx(GP, {
            ...o,
            ref: t
        })
    })
}
);
D0.displayName = no;
var QP = m.forwardRef( (e, t) => {
    const n = on(no, e.__scopeDialog)
      , r = m.useRef(null)
      , o = fe(t, n.contentRef, r);
    return m.useEffect( () => {
        const s = r.current;
        if (s)
            return Ix(s)
    }
    , []),
    a.jsx(O0, {
        ...e,
        ref: o,
        trapFocus: n.open,
        disableOutsidePointerEvents: !0,
        onCloseAutoFocus: Q(e.onCloseAutoFocus, s => {
            var i;
            s.preventDefault(),
            (i = n.triggerRef.current) == null || i.focus()
        }
        ),
        onPointerDownOutside: Q(e.onPointerDownOutside, s => {
            const i = s.detail.originalEvent
              , l = i.button === 0 && i.ctrlKey === !0;
            (i.button === 2 || l) && s.preventDefault()
        }
        ),
        onFocusOutside: Q(e.onFocusOutside, s => s.preventDefault())
    })
}
)
  , GP = m.forwardRef( (e, t) => {
    const n = on(no, e.__scopeDialog)
      , r = m.useRef(!1)
      , o = m.useRef(!1);
    return a.jsx(O0, {
        ...e,
        ref: t,
        trapFocus: !1,
        disableOutsidePointerEvents: !1,
        onCloseAutoFocus: s => {
            var i, l;
            (i = e.onCloseAutoFocus) == null || i.call(e, s),
            s.defaultPrevented || (r.current || (l = n.triggerRef.current) == null || l.focus(),
            s.preventDefault()),
            r.current = !1,
            o.current = !1
        }
        ,
        onInteractOutside: s => {
            var c, u;
            (c = e.onInteractOutside) == null || c.call(e, s),
            s.defaultPrevented || (r.current = !0,
            s.detail.originalEvent.type === "pointerdown" && (o.current = !0));
            const i = s.target;
            ((u = n.triggerRef.current) == null ? void 0 : u.contains(i)) && s.preventDefault(),
            s.detail.originalEvent.type === "focusin" && o.current && s.preventDefault()
        }
    })
}
)
  , O0 = m.forwardRef( (e, t) => {
    const {__scopeDialog: n, trapFocus: r, onOpenAutoFocus: o, onCloseAutoFocus: s, ...i} = e
      , l = on(no, n)
      , c = m.useRef(null)
      , u = fe(t, c);
    return _x(),
    a.jsxs(a.Fragment, {
        children: [a.jsx(Of, {
            asChild: !0,
            loop: !0,
            trapped: r,
            onMountAutoFocus: o,
            onUnmountAutoFocus: s,
            children: a.jsx(Ta, {
                role: "dialog",
                id: l.contentId,
                "aria-describedby": l.descriptionId,
                "aria-labelledby": l.titleId,
                "data-state": zf(l.open),
                ...i,
                ref: u,
                onDismiss: () => l.onOpenChange(!1)
            })
        }), a.jsxs(a.Fragment, {
            children: [a.jsx(qP, {
                titleId: l.titleId
            }), a.jsx(JP, {
                contentRef: c,
                descriptionId: l.descriptionId
            })]
        })]
    })
}
)
  , Ff = "DialogTitle"
  , A0 = m.forwardRef( (e, t) => {
    const {__scopeDialog: n, ...r} = e
      , o = on(Ff, n);
    return a.jsx(te.h2, {
        id: o.titleId,
        ...r,
        ref: t
    })
}
);
A0.displayName = Ff;
var I0 = "DialogDescription"
  , L0 = m.forwardRef( (e, t) => {
    const {__scopeDialog: n, ...r} = e
      , o = on(I0, n);
    return a.jsx(te.p, {
        id: o.descriptionId,
        ...r,
        ref: t
    })
}
);
L0.displayName = I0;
var F0 = "DialogClose"
  , z0 = m.forwardRef( (e, t) => {
    const {__scopeDialog: n, ...r} = e
      , o = on(F0, n);
    return a.jsx(te.button, {
        type: "button",
        ...r,
        ref: t,
        onClick: Q(e.onClick, () => o.onOpenChange(!1))
    })
}
);
z0.displayName = F0;
function zf(e) {
    return e ? "open" : "closed"
}
var $0 = "DialogTitleWarning"
  , [PR,B0] = bN($0, {
    contentName: no,
    titleName: Ff,
    docsSlug: "dialog"
})
  , qP = ({titleId: e}) => {
    const t = B0($0)
      , n = `\`${t.contentName}\` requires a \`${t.titleName}\` for the component to be accessible for screen reader users.

If you want to hide the \`${t.titleName}\`, you can wrap it with our VisuallyHidden component.

For more information, see https://radix-ui.com/primitives/docs/components/${t.docsSlug}`;
    return m.useEffect( () => {
        e && (document.getElementById(e) || console.error(n))
    }
    , [n, e]),
    null
}
  , XP = "DialogDescriptionWarning"
  , JP = ({contentRef: e, descriptionId: t}) => {
    const r = `Warning: Missing \`Description\` or \`aria-describedby={undefined}\` for {${B0(XP).contentName}}.`;
    return m.useEffect( () => {
        var s;
        const o = (s = e.current) == null ? void 0 : s.getAttribute("aria-describedby");
        t && o && (document.getElementById(t) || console.warn(r))
    }
    , [r, e, t]),
    null
}
  , ZP = P0
  , e4 = R0
  , W0 = _0
  , H0 = D0
  , V0 = A0
  , U0 = L0
  , t4 = z0;
const n4 = ZP
  , r4 = e4
  , Y0 = m.forwardRef( ({className: e, ...t}, n) => a.jsx(W0, {
    ref: n,
    className: re("fixed inset-0 z-50 bg-black/80 data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0", e),
    ...t
}));
Y0.displayName = W0.displayName;
const K0 = m.forwardRef( ({className: e, children: t, ...n}, r) => a.jsxs(r4, {
    children: [a.jsx(Y0, {}), a.jsxs(H0, {
        ref: r,
        className: re("fixed left-[50%] top-[50%] z-50 grid w-full max-w-lg translate-x-[-50%] translate-y-[-50%] gap-4 border bg-background p-6 shadow-lg duration-200 data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[state=closed]:slide-out-to-left-1/2 data-[state=closed]:slide-out-to-top-[48%] data-[state=open]:slide-in-from-left-1/2 data-[state=open]:slide-in-from-top-[48%] sm:rounded-lg", e),
        ...n,
        children: [t, a.jsxs(t4, {
            className: "absolute right-4 top-4 rounded-sm opacity-70 ring-offset-background transition-opacity data-[state=open]:bg-accent data-[state=open]:text-muted-foreground hover:opacity-100 focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:pointer-events-none",
            children: [a.jsx(yf, {
                className: "h-4 w-4"
            }), a.jsx("span", {
                className: "sr-only",
                children: "Close"
            })]
        })]
    })]
}));
K0.displayName = H0.displayName;
const Q0 = ({className: e, ...t}) => a.jsx("div", {
    className: re("flex flex-col space-y-1.5 text-center sm:text-left", e),
    ...t
});
Q0.displayName = "DialogHeader";
const G0 = m.forwardRef( ({className: e, ...t}, n) => a.jsx(V0, {
    ref: n,
    className: re("text-lg font-semibold leading-none tracking-tight", e),
    ...t
}));
G0.displayName = V0.displayName;
const o4 = m.forwardRef( ({className: e, ...t}, n) => a.jsx(U0, {
    ref: n,
    className: re("text-sm text-muted-foreground", e),
    ...t
}));
o4.displayName = U0.displayName;
const s4 = () => {
    var c;
    const [e,t] = m.useState(null)
      , [n,r] = m.useState("")
      , [o,s] = m.useState("")
      , i = [{
        id: "1",
        title: "Modern Family Home",
        price: "$2,500/month",
        location: "Downtown District, NY",
        image: Xt,
        beds: 4,
        baths: 3,
        sqft: 2400,
        type: "lease",
        status: "available",
        description: "Beautiful modern family home with spacious rooms, updated kitchen, and large backyard. Perfect for families looking for comfort and convenience.",
        features: ["Garage", "Garden", "Modern Kitchen", "Hardwood Floors", "Central AC"]
    }, {
        id: "2",
        title: "Luxury Contemporary Villa",
        price: "$1,200,000",
        location: "Hillside Heights, NY",
        image: yn,
        beds: 5,
        baths: 4,
        sqft: 3200,
        type: "sale",
        status: "available",
        description: "Stunning contemporary villa with panoramic views, premium finishes, and state-of-the-art amenities. An exclusive opportunity for discerning buyers.",
        features: ["Pool", "Home Theater", "Wine Cellar", "Smart Home", "Panoramic Views"]
    }, {
        id: "3",
        title: "Elegant Victorian Estate",
        price: "$950,000",
        location: "Heritage Gardens, NY",
        image: _n,
        beds: 4,
        baths: 3,
        sqft: 2800,
        type: "sale",
        status: "available",
        description: "Charming Victorian estate with period features, beautifully landscaped gardens, and modern conveniences. A perfect blend of historic charm and contemporary comfort.",
        features: ["Historic Details", "Fireplace", "Crown Molding", "Bay Windows", "Mature Gardens"]
    }, {
        id: "4",
        title: "Cozy Suburban Home",
        price: "$1,800/month",
        location: "Green Valley, NY",
        image: Xt,
        beds: 3,
        baths: 2,
        sqft: 1800,
        type: "lease",
        status: "available",
        description: "Comfortable suburban home in a quiet neighborhood. Features include updated appliances, fenced yard, and close proximity to schools and parks.",
        features: ["Fenced Yard", "Updated Kitchen", "Near Schools", "Quiet Street", "Storage Space"]
    }, {
        id: "5",
        title: "Downtown Penthouse",
        price: "$4,500/month",
        location: "City Center, NY",
        image: yn,
        beds: 2,
        baths: 2,
        sqft: 1500,
        type: "lease",
        status: "available",
        description: "Luxury penthouse with city views, modern amenities, and prime location. Walk to restaurants, shopping, and entertainment.",
        features: ["City Views", "Rooftop Access", "Concierge", "Gym", "Walking Distance"]
    }, {
        id: "6",
        title: "Waterfront Mansion",
        price: "$2,800,000",
        location: "Lakeside Estates, NY",
        image: _n,
        beds: 6,
        baths: 5,
        sqft: 4500,
        type: "sale",
        status: "available",
        description: "Magnificent waterfront mansion with private dock, swimming pool, and breathtaking lake views. Ultimate luxury living experience.",
        features: ["Private Dock", "Pool", "Lake Views", "Guest House", "Tennis Court"]
    }]
      , l = u => {
        t(u)
    }
    ;
    return a.jsxs("div", {
        className: "min-h-screen bg-surface-gradient",
        children: [a.jsxs("div", {
            className: "max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12",
            children: [a.jsxs("div", {
                className: "text-center mb-12",
                children: [a.jsx("h1", {
                    className: "text-4xl md:text-5xl font-bold text-foreground mb-4",
                    children: "Find Your Perfect Property"
                }), a.jsx("p", {
                    className: "text-xl text-muted-foreground max-w-2xl mx-auto",
                    children: "Discover amazing properties available for sale and lease. Use our advanced search to find exactly what you're looking for."
                })]
            }), a.jsx(Ce, {
                className: "p-6 mb-8 shadow-soft",
                children: a.jsxs("div", {
                    className: "grid md:grid-cols-4 gap-4",
                    children: [a.jsxs("div", {
                        className: "relative",
                        children: [a.jsx(wy, {
                            className: "absolute left-3 top-3 h-4 w-4 text-muted-foreground"
                        }), a.jsx(Ee, {
                            placeholder: "Search properties...",
                            value: n,
                            onChange: u => r(u.target.value),
                            className: "pl-10"
                        })]
                    }), a.jsxs(Kt, {
                        value: o,
                        onValueChange: s,
                        children: [a.jsx(Mt, {
                            children: a.jsx(Qt, {
                                placeholder: "Property Type"
                            })
                        }), a.jsxs(Rt, {
                            children: [a.jsx(Y, {
                                value: "all",
                                children: "All Types"
                            }), a.jsx(Y, {
                                value: "sale",
                                children: "For Sale"
                            }), a.jsx(Y, {
                                value: "lease",
                                children: "For Lease"
                            })]
                        })]
                    }), a.jsxs(Kt, {
                        children: [a.jsx(Mt, {
                            children: a.jsx(Qt, {
                                placeholder: "Price Range"
                            })
                        }), a.jsxs(Rt, {
                            children: [a.jsx(Y, {
                                value: "0-500k",
                                children: "$0 - $500k"
                            }), a.jsx(Y, {
                                value: "500k-1m",
                                children: "$500k - $1M"
                            }), a.jsx(Y, {
                                value: "1m-2m",
                                children: "$1M - $2M"
                            }), a.jsx(Y, {
                                value: "2m+",
                                children: "$2M+"
                            })]
                        })]
                    }), a.jsxs(ae, {
                        className: "bg-primary hover:bg-primary-dark text-primary-foreground",
                        children: [a.jsx(CS, {
                            className: "w-4 h-4 mr-2"
                        }), "Search"]
                    })]
                })
            }), a.jsx("div", {
                className: "grid md:grid-cols-2 lg:grid-cols-3 gap-6 mb-16",
                children: i.map(u => a.jsx(Px, {
                    property: u,
                    onViewDetails: l
                }, u.id))
            }), a.jsxs(Ce, {
                className: "p-8 shadow-medium",
                children: [a.jsxs("div", {
                    className: "text-center mb-8",
                    children: [a.jsx("h2", {
                        className: "text-3xl font-bold text-foreground mb-4",
                        children: "Can't Find What You're Looking For?"
                    }), a.jsx("p", {
                        className: "text-muted-foreground text-lg",
                        children: "Let our expert team help you find the perfect property. Fill out the form below and we'll contact you with matching options."
                    })]
                }), a.jsxs("form", {
                    className: "grid md:grid-cols-2 gap-6 max-w-4xl mx-auto",
                    children: [a.jsxs("div", {
                        className: "space-y-2",
                        children: [a.jsx(se, {
                            htmlFor: "name",
                            children: "Full Name"
                        }), a.jsxs("div", {
                            className: "relative",
                            children: [a.jsx(wr, {
                                className: "absolute left-3 top-3 h-4 w-4 text-muted-foreground"
                            }), a.jsx(Ee, {
                                id: "name",
                                placeholder: "Enter your full name",
                                className: "pl-10"
                            })]
                        })]
                    }), a.jsxs("div", {
                        className: "space-y-2",
                        children: [a.jsx(se, {
                            htmlFor: "email",
                            children: "Email Address"
                        }), a.jsxs("div", {
                            className: "relative",
                            children: [a.jsx(ss, {
                                className: "absolute left-3 top-3 h-4 w-4 text-muted-foreground"
                            }), a.jsx(Ee, {
                                id: "email",
                                type: "email",
                                placeholder: "Enter your email",
                                className: "pl-10"
                            })]
                        })]
                    }), a.jsxs("div", {
                        className: "space-y-2",
                        children: [a.jsx(se, {
                            htmlFor: "phone",
                            children: "Phone Number"
                        }), a.jsxs("div", {
                            className: "relative",
                            children: [a.jsx(as, {
                                className: "absolute left-3 top-3 h-4 w-4 text-muted-foreground"
                            }), a.jsx(Ee, {
                                id: "phone",
                                placeholder: "Enter your phone number",
                                className: "pl-10"
                            })]
                        })]
                    }), a.jsxs("div", {
                        className: "space-y-2",
                        children: [a.jsx(se, {
                            htmlFor: "budget",
                            children: "Budget Range"
                        }), a.jsxs(Kt, {
                            children: [a.jsx(Mt, {
                                children: a.jsx(Qt, {
                                    placeholder: "Select your budget"
                                })
                            }), a.jsxs(Rt, {
                                children: [a.jsx(Y, {
                                    value: "under-500k",
                                    children: "Under $500k"
                                }), a.jsx(Y, {
                                    value: "500k-1m",
                                    children: "$500k - $1M"
                                }), a.jsx(Y, {
                                    value: "1m-2m",
                                    children: "$1M - $2M"
                                }), a.jsx(Y, {
                                    value: "2m-5m",
                                    children: "$2M - $5M"
                                }), a.jsx(Y, {
                                    value: "5m+",
                                    children: "$5M+"
                                })]
                            })]
                        })]
                    }), a.jsxs("div", {
                        className: "space-y-2",
                        children: [a.jsx(se, {
                            htmlFor: "propertyType",
                            children: "Property Type"
                        }), a.jsxs(Kt, {
                            children: [a.jsx(Mt, {
                                children: a.jsx(Qt, {
                                    placeholder: "Select property type"
                                })
                            }), a.jsxs(Rt, {
                                children: [a.jsx(Y, {
                                    value: "house",
                                    children: "House"
                                }), a.jsx(Y, {
                                    value: "condo",
                                    children: "Condo"
                                }), a.jsx(Y, {
                                    value: "apartment",
                                    children: "Apartment"
                                }), a.jsx(Y, {
                                    value: "land",
                                    children: "Land"
                                }), a.jsx(Y, {
                                    value: "commercial",
                                    children: "Commercial"
                                })]
                            })]
                        })]
                    }), a.jsxs("div", {
                        className: "space-y-2",
                        children: [a.jsx(se, {
                            htmlFor: "location",
                            children: "Preferred Location"
                        }), a.jsxs("div", {
                            className: "relative",
                            children: [a.jsx(Ra, {
                                className: "absolute left-3 top-3 h-4 w-4 text-muted-foreground"
                            }), a.jsx(Ee, {
                                id: "location",
                                placeholder: "Enter preferred area",
                                className: "pl-10"
                            })]
                        })]
                    }), a.jsxs("div", {
                        className: "md:col-span-2 space-y-2",
                        children: [a.jsx(se, {
                            htmlFor: "requirements",
                            children: "Additional Requirements"
                        }), a.jsx(Oa, {
                            id: "requirements",
                            placeholder: "Tell us about your specific requirements, preferences, or any questions you have...",
                            className: "min-h-[120px]"
                        })]
                    }), a.jsx("div", {
                        className: "md:col-span-2 text-center",
                        children: a.jsx(ae, {
                            size: "lg",
                            className: "bg-accent-gradient hover:shadow-accent text-primary font-semibold px-8",
                            children: "Get Personalized Recommendations"
                        })
                    })]
                })]
            })]
        }), a.jsx(n4, {
            open: !!e,
            onOpenChange: () => t(null),
            children: a.jsx(K0, {
                className: "max-w-4xl max-h-[90vh] overflow-y-auto",
                children: e && a.jsxs(a.Fragment, {
                    children: [a.jsx(Q0, {
                        children: a.jsx(G0, {
                            className: "text-2xl font-bold",
                            children: e.title
                        })
                    }), a.jsxs("div", {
                        className: "space-y-6",
                        children: [a.jsx("img", {
                            src: e.image,
                            alt: e.title,
                            className: "w-full h-64 md:h-80 object-cover rounded-lg"
                        }), a.jsxs("div", {
                            className: "grid md:grid-cols-2 gap-6",
                            children: [a.jsxs("div", {
                                children: [a.jsx("h3", {
                                    className: "text-xl font-semibold mb-4",
                                    children: "Property Details"
                                }), a.jsxs("div", {
                                    className: "space-y-2 text-sm",
                                    children: [a.jsxs("div", {
                                        className: "flex justify-between",
                                        children: [a.jsx("span", {
                                            className: "text-muted-foreground",
                                            children: "Price:"
                                        }), a.jsx("span", {
                                            className: "font-semibold text-primary",
                                            children: e.price
                                        })]
                                    }), a.jsxs("div", {
                                        className: "flex justify-between",
                                        children: [a.jsx("span", {
                                            className: "text-muted-foreground",
                                            children: "Location:"
                                        }), a.jsx("span", {
                                            children: e.location
                                        })]
                                    }), a.jsxs("div", {
                                        className: "flex justify-between",
                                        children: [a.jsx("span", {
                                            className: "text-muted-foreground",
                                            children: "Bedrooms:"
                                        }), a.jsx("span", {
                                            children: e.beds
                                        })]
                                    }), a.jsxs("div", {
                                        className: "flex justify-between",
                                        children: [a.jsx("span", {
                                            className: "text-muted-foreground",
                                            children: "Bathrooms:"
                                        }), a.jsx("span", {
                                            children: e.baths
                                        })]
                                    }), a.jsxs("div", {
                                        className: "flex justify-between",
                                        children: [a.jsx("span", {
                                            className: "text-muted-foreground",
                                            children: "Square Feet:"
                                        }), a.jsx("span", {
                                            children: e.sqft.toLocaleString()
                                        })]
                                    })]
                                })]
                            }), a.jsxs("div", {
                                children: [a.jsx("h3", {
                                    className: "text-xl font-semibold mb-4",
                                    children: "Features"
                                }), a.jsx("div", {
                                    className: "flex flex-wrap gap-2",
                                    children: (c = e.features) == null ? void 0 : c.map( (u, d) => a.jsx("span", {
                                        className: "bg-secondary text-secondary-foreground px-3 py-1 rounded-full text-sm",
                                        children: u
                                    }, d))
                                })]
                            })]
                        }), a.jsxs("div", {
                            children: [a.jsx("h3", {
                                className: "text-xl font-semibold mb-4",
                                children: "Description"
                            }), a.jsx("p", {
                                className: "text-muted-foreground leading-relaxed",
                                children: e.description
                            })]
                        }), a.jsxs("div", {
                            className: "flex gap-4",
                            children: [a.jsx(ae, {
                                className: "flex-1 bg-primary hover:bg-primary-dark text-primary-foreground",
                                children: "Schedule Viewing"
                            }), a.jsx(ae, {
                                variant: "outline",
                                className: "flex-1 border-accent text-accent hover:bg-accent hover:text-accent-foreground",
                                children: "Contact Agent"
                            })]
                        })]
                    })]
                })
            })
        })]
    })
}
  , a4 = () => {
    const e = [{
        icon: nl,
        title: "Maximum Market Value",
        description: "Our AI-powered analysis ensures you get the best possible price for your property"
    }, {
        icon: os,
        title: "Fast Sales Process",
        description: "Average time to sale is 30% faster than industry standard"
    }, {
        icon: Ku,
        title: "Expert Guidance",
        description: "Professional support through every step of the selling process"
    }, {
        icon: gy,
        title: "Proven Track Record",
        description: "500+ successful sales with 98% client satisfaction rate"
    }]
      , t = [{
        step: "1",
        title: "Property Evaluation",
        description: "We conduct a comprehensive analysis of your property and market conditions"
    }, {
        step: "2",
        title: "Strategic Pricing",
        description: "Our experts set the optimal price to attract buyers and maximize returns"
    }, {
        step: "3",
        title: "Professional Marketing",
        description: "High-quality photography, virtual tours, and multi-channel marketing"
    }, {
        step: "4",
        title: "Closing Support",
        description: "Full support through negotiations, inspections, and closing procedures"
    }];
    return a.jsx("div", {
        className: "min-h-screen bg-surface-gradient",
        children: a.jsxs("div", {
            className: "max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12",
            children: [a.jsxs("div", {
                className: "text-center mb-16",
                children: [a.jsx(rt, {
                    className: "mb-4 bg-accent/10 text-accent-foreground border-accent/20",
                    children: "Sell Your Property"
                }), a.jsx("h1", {
                    className: "text-4xl md:text-5xl font-bold text-foreground mb-6",
                    children: "Get Top Dollar for Your Property"
                }), a.jsx("p", {
                    className: "text-xl text-muted-foreground max-w-3xl mx-auto mb-8",
                    children: "Our expert team combines market knowledge with AI-powered insights to help you sell your property quickly and for the best price. Join thousands of satisfied sellers who chose RealtyPro."
                }), a.jsxs("div", {
                    className: "flex flex-col sm:flex-row gap-4 justify-center",
                    children: [a.jsxs(ae, {
                        size: "lg",
                        className: "bg-accent-gradient hover:shadow-accent text-primary font-semibold",
                        children: [a.jsx(Yu, {
                            className: "w-5 h-5 mr-2"
                        }), "Get Free Property Evaluation"]
                    }), a.jsx(ae, {
                        size: "lg",
                        variant: "outline",
                        className: "border-primary text-primary hover:bg-primary hover:text-primary-foreground",
                        children: "Learn About Our Process"
                    })]
                })]
            }), a.jsx("div", {
                className: "grid md:grid-cols-2 lg:grid-cols-4 gap-6 mb-16",
                children: e.map( (n, r) => {
                    const o = n.icon;
                    return a.jsxs(Ce, {
                        className: "p-6 text-center shadow-soft hover:shadow-medium transition-all duration-300 animate-fade-in",
                        children: [a.jsx("div", {
                            className: "bg-accent/10 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4",
                            children: a.jsx(o, {
                                className: "w-8 h-8 text-accent"
                            })
                        }), a.jsx("h3", {
                            className: "text-lg font-semibold text-foreground mb-2",
                            children: n.title
                        }), a.jsx("p", {
                            className: "text-muted-foreground text-sm leading-relaxed",
                            children: n.description
                        })]
                    }, r)
                }
                )
            }), a.jsx(Ce, {
                className: "p-8 md:p-12 mb-16 shadow-medium",
                children: a.jsxs("div", {
                    className: "grid lg:grid-cols-2 gap-12 items-center",
                    children: [a.jsxs("div", {
                        children: [a.jsx("h2", {
                            className: "text-3xl md:text-4xl font-bold text-foreground mb-6",
                            children: "Why Sell With RealtyPro?"
                        }), a.jsxs("div", {
                            className: "space-y-4 mb-8",
                            children: [a.jsxs("div", {
                                className: "flex items-start space-x-3",
                                children: [a.jsx(ir, {
                                    className: "w-6 h-6 text-accent mt-1 flex-shrink-0"
                                }), a.jsxs("div", {
                                    children: [a.jsx("h4", {
                                        className: "font-semibold text-foreground mb-1",
                                        children: "AI-Powered Market Analysis"
                                    }), a.jsx("p", {
                                        className: "text-muted-foreground text-sm",
                                        children: "Advanced algorithms analyze market trends to price your property competitively"
                                    })]
                                })]
                            }), a.jsxs("div", {
                                className: "flex items-start space-x-3",
                                children: [a.jsx(ir, {
                                    className: "w-6 h-6 text-accent mt-1 flex-shrink-0"
                                }), a.jsxs("div", {
                                    children: [a.jsx("h4", {
                                        className: "font-semibold text-foreground mb-1",
                                        children: "Professional Marketing"
                                    }), a.jsx("p", {
                                        className: "text-muted-foreground text-sm",
                                        children: "High-quality photography, virtual tours, and targeted advertising campaigns"
                                    })]
                                })]
                            }), a.jsxs("div", {
                                className: "flex items-start space-x-3",
                                children: [a.jsx(ir, {
                                    className: "w-6 h-6 text-accent mt-1 flex-shrink-0"
                                }), a.jsxs("div", {
                                    children: [a.jsx("h4", {
                                        className: "font-semibold text-foreground mb-1",
                                        children: "Expert Negotiation"
                                    }), a.jsx("p", {
                                        className: "text-muted-foreground text-sm",
                                        children: "Skilled agents who know how to get the best deal for your property"
                                    })]
                                })]
                            }), a.jsxs("div", {
                                className: "flex items-start space-x-3",
                                children: [a.jsx(ir, {
                                    className: "w-6 h-6 text-accent mt-1 flex-shrink-0"
                                }), a.jsxs("div", {
                                    children: [a.jsx("h4", {
                                        className: "font-semibold text-foreground mb-1",
                                        children: "Full-Service Support"
                                    }), a.jsx("p", {
                                        className: "text-muted-foreground text-sm",
                                        children: "From listing to closing, we handle every detail of your sale"
                                    })]
                                })]
                            })]
                        })]
                    }), a.jsxs("div", {
                        className: "bg-primary text-primary-foreground rounded-2xl p-8",
                        children: [a.jsx("h3", {
                            className: "text-2xl font-bold mb-6",
                            children: "Success Statistics"
                        }), a.jsxs("div", {
                            className: "grid grid-cols-2 gap-6",
                            children: [a.jsxs("div", {
                                className: "text-center",
                                children: [a.jsx("div", {
                                    className: "text-3xl font-bold text-accent mb-2",
                                    children: "98%"
                                }), a.jsx("div", {
                                    className: "text-sm text-primary-foreground/80",
                                    children: "Client Satisfaction"
                                })]
                            }), a.jsxs("div", {
                                className: "text-center",
                                children: [a.jsx("div", {
                                    className: "text-3xl font-bold text-accent mb-2",
                                    children: "30%"
                                }), a.jsx("div", {
                                    className: "text-sm text-primary-foreground/80",
                                    children: "Faster Sales"
                                })]
                            }), a.jsxs("div", {
                                className: "text-center",
                                children: [a.jsx("div", {
                                    className: "text-3xl font-bold text-accent mb-2",
                                    children: "500+"
                                }), a.jsx("div", {
                                    className: "text-sm text-primary-foreground/80",
                                    children: "Properties Sold"
                                })]
                            }), a.jsxs("div", {
                                className: "text-center",
                                children: [a.jsx("div", {
                                    className: "text-3xl font-bold text-accent mb-2",
                                    children: "15+"
                                }), a.jsx("div", {
                                    className: "text-sm text-primary-foreground/80",
                                    children: "Years Experience"
                                })]
                            })]
                        })]
                    })]
                })
            }), a.jsxs("div", {
                className: "mb-16",
                children: [a.jsxs("div", {
                    className: "text-center mb-12",
                    children: [a.jsx("h2", {
                        className: "text-3xl md:text-4xl font-bold text-foreground mb-4",
                        children: "Our Proven Selling Process"
                    }), a.jsx("p", {
                        className: "text-muted-foreground text-lg max-w-2xl mx-auto",
                        children: "We've refined our process to ensure maximum results for every client. Here's how we'll help you sell your property."
                    })]
                }), a.jsx("div", {
                    className: "grid md:grid-cols-2 lg:grid-cols-4 gap-6",
                    children: t.map( (n, r) => a.jsxs(Ce, {
                        className: "p-6 text-center shadow-soft hover:shadow-medium transition-all duration-300",
                        children: [a.jsx("div", {
                            className: "bg-accent text-accent-foreground w-12 h-12 rounded-full flex items-center justify-center mx-auto mb-4 text-xl font-bold",
                            children: n.step
                        }), a.jsx("h3", {
                            className: "text-lg font-semibold text-foreground mb-3",
                            children: n.title
                        }), a.jsx("p", {
                            className: "text-muted-foreground text-sm leading-relaxed",
                            children: n.description
                        })]
                    }, r))
                })]
            }), a.jsxs(Ce, {
                className: "p-8 shadow-strong",
                children: [a.jsxs("div", {
                    className: "text-center mb-8",
                    children: [a.jsx("h2", {
                        className: "text-3xl font-bold text-foreground mb-4",
                        children: "Ready to Sell Your Property?"
                    }), a.jsx("p", {
                        className: "text-muted-foreground text-lg max-w-2xl mx-auto",
                        children: "Fill out the form below and our expert team will contact you within 24 hours with a comprehensive market analysis and selling strategy for your property."
                    })]
                }), a.jsxs("form", {
                    className: "grid md:grid-cols-2 gap-6 max-w-4xl mx-auto",
                    children: [a.jsxs("div", {
                        className: "space-y-2",
                        children: [a.jsx(se, {
                            htmlFor: "ownerName",
                            children: "Full Name"
                        }), a.jsxs("div", {
                            className: "relative",
                            children: [a.jsx(wr, {
                                className: "absolute left-3 top-3 h-4 w-4 text-muted-foreground"
                            }), a.jsx(Ee, {
                                id: "ownerName",
                                placeholder: "Enter your full name",
                                className: "pl-10"
                            })]
                        })]
                    }), a.jsxs("div", {
                        className: "space-y-2",
                        children: [a.jsx(se, {
                            htmlFor: "ownerEmail",
                            children: "Email Address"
                        }), a.jsxs("div", {
                            className: "relative",
                            children: [a.jsx(ss, {
                                className: "absolute left-3 top-3 h-4 w-4 text-muted-foreground"
                            }), a.jsx(Ee, {
                                id: "ownerEmail",
                                type: "email",
                                placeholder: "Enter your email",
                                className: "pl-10"
                            })]
                        })]
                    }), a.jsxs("div", {
                        className: "space-y-2",
                        children: [a.jsx(se, {
                            htmlFor: "ownerPhone",
                            children: "Phone Number"
                        }), a.jsxs("div", {
                            className: "relative",
                            children: [a.jsx(as, {
                                className: "absolute left-3 top-3 h-4 w-4 text-muted-foreground"
                            }), a.jsx(Ee, {
                                id: "ownerPhone",
                                placeholder: "Enter your phone number",
                                className: "pl-10"
                            })]
                        })]
                    }), a.jsxs("div", {
                        className: "space-y-2",
                        children: [a.jsx(se, {
                            htmlFor: "propertyAddress",
                            children: "Property Address"
                        }), a.jsxs("div", {
                            className: "relative",
                            children: [a.jsx(Ra, {
                                className: "absolute left-3 top-3 h-4 w-4 text-muted-foreground"
                            }), a.jsx(Ee, {
                                id: "propertyAddress",
                                placeholder: "Enter property address",
                                className: "pl-10"
                            })]
                        })]
                    }), a.jsxs("div", {
                        className: "space-y-2",
                        children: [a.jsx(se, {
                            htmlFor: "propertyTypeSelect",
                            children: "Property Type"
                        }), a.jsxs(Kt, {
                            children: [a.jsx(Mt, {
                                children: a.jsx(Qt, {
                                    placeholder: "Select property type"
                                })
                            }), a.jsxs(Rt, {
                                children: [a.jsx(Y, {
                                    value: "single-family",
                                    children: "Single Family Home"
                                }), a.jsx(Y, {
                                    value: "condo",
                                    children: "Condominium"
                                }), a.jsx(Y, {
                                    value: "townhouse",
                                    children: "Townhouse"
                                }), a.jsx(Y, {
                                    value: "multi-family",
                                    children: "Multi-Family"
                                }), a.jsx(Y, {
                                    value: "land",
                                    children: "Land/Lot"
                                }), a.jsx(Y, {
                                    value: "commercial",
                                    children: "Commercial Property"
                                })]
                            })]
                        })]
                    }), a.jsxs("div", {
                        className: "space-y-2",
                        children: [a.jsx(se, {
                            htmlFor: "timeframe",
                            children: "Selling Timeframe"
                        }), a.jsxs(Kt, {
                            children: [a.jsx(Mt, {
                                children: a.jsx(Qt, {
                                    placeholder: "When do you want to sell?"
                                })
                            }), a.jsxs(Rt, {
                                children: [a.jsx(Y, {
                                    value: "immediate",
                                    children: "ASAP"
                                }), a.jsx(Y, {
                                    value: "1-3months",
                                    children: "1-3 Months"
                                }), a.jsx(Y, {
                                    value: "3-6months",
                                    children: "3-6 Months"
                                }), a.jsx(Y, {
                                    value: "6-12months",
                                    children: "6-12 Months"
                                }), a.jsx(Y, {
                                    value: "just-exploring",
                                    children: "Just Exploring"
                                })]
                            })]
                        })]
                    }), a.jsxs("div", {
                        className: "space-y-2",
                        children: [a.jsx(se, {
                            htmlFor: "estimatedValue",
                            children: "Estimated Property Value"
                        }), a.jsxs("div", {
                            className: "relative",
                            children: [a.jsx(Yu, {
                                className: "absolute left-3 top-3 h-4 w-4 text-muted-foreground"
                            }), a.jsx(Ee, {
                                id: "estimatedValue",
                                placeholder: "Your estimated value",
                                className: "pl-10"
                            })]
                        })]
                    }), a.jsxs("div", {
                        className: "space-y-2",
                        children: [a.jsx(se, {
                            htmlFor: "propertySize",
                            children: "Property Size (sq ft)"
                        }), a.jsxs("div", {
                            className: "relative",
                            children: [a.jsx(gf, {
                                className: "absolute left-3 top-3 h-4 w-4 text-muted-foreground"
                            }), a.jsx(Ee, {
                                id: "propertySize",
                                placeholder: "Enter property size",
                                className: "pl-10"
                            })]
                        })]
                    }), a.jsxs("div", {
                        className: "md:col-span-2 space-y-2",
                        children: [a.jsx(se, {
                            htmlFor: "propertyDetails",
                            children: "Property Details & Goals"
                        }), a.jsx(Oa, {
                            id: "propertyDetails",
                            placeholder: "Tell us about your property, any unique features, recent improvements, and your selling goals...",
                            className: "min-h-[120px]"
                        })]
                    }), a.jsxs("div", {
                        className: "md:col-span-2 text-center",
                        children: [a.jsx(ae, {
                            size: "lg",
                            className: "bg-accent-gradient hover:shadow-accent text-primary font-semibold px-12 py-4",
                            children: "Get Free Property Evaluation"
                        }), a.jsx("p", {
                            className: "text-sm text-muted-foreground mt-4",
                            children: "Our team will contact you within 24 hours with your personalized market analysis"
                        })]
                    })]
                })]
            })]
        })
    })
}
  , i4 = () => {
    const e = [{
        id: "1",
        slug: "home-buying-guide-2024",
        title: "The Complete Home Buying Guide for 2024",
        excerpt: "Everything you need to know about buying your first home in today's market, from getting pre-approved to closing day.",
        content: "Full article content would go here...",
        image: Xt,
        category: "Buying Guide",
        author: "Sarah Johnson",
        date: "2024-01-15",
        readTime: "8 min read",
        featured: !0
    }, {
        id: "2",
        slug: "market-trends-analysis",
        title: "Real Estate Market Trends: What to Expect This Year",
        excerpt: "Our expert analysis of current market conditions and predictions for the remainder of 2024.",
        content: "Full article content would go here...",
        image: yn,
        category: "Market Analysis",
        author: "Michael Chen",
        date: "2024-01-12",
        readTime: "6 min read",
        featured: !0
    }, {
        id: "3",
        slug: "selling-tips-maximize-value",
        title: "10 Tips to Maximize Your Home's Value Before Selling",
        excerpt: "Simple improvements and staging techniques that can significantly increase your property's selling price.",
        content: "Full article content would go here...",
        image: _n,
        category: "Selling Tips",
        author: "Emily Davis",
        date: "2024-01-10",
        readTime: "5 min read",
        featured: !1
    }, {
        id: "4",
        slug: "investment-opportunities",
        title: "Investment Opportunities in Emerging Neighborhoods",
        excerpt: "Discover up-and-coming areas with great potential for real estate investment returns.",
        content: "Full article content would go here...",
        image: Xt,
        category: "Investment",
        author: "David Wilson",
        date: "2024-01-08",
        readTime: "7 min read",
        featured: !1
    }, {
        id: "5",
        slug: "mortgage-rates-explained",
        title: "Understanding Mortgage Rates: Fixed vs Variable",
        excerpt: "A comprehensive breakdown of mortgage options to help you make the best financial decision.",
        content: "Full article content would go here...",
        image: yn,
        category: "Finance",
        author: "Lisa Thompson",
        date: "2024-01-05",
        readTime: "6 min read",
        featured: !1
    }, {
        id: "6",
        slug: "home-inspection-checklist",
        title: "Home Inspection Checklist: What to Look For",
        excerpt: "Essential items to check during a home inspection to avoid costly surprises after purchase.",
        content: "Full article content would go here...",
        image: _n,
        category: "Buying Guide",
        author: "Robert Martinez",
        date: "2024-01-03",
        readTime: "9 min read",
        featured: !1
    }]
      , t = ["All", "Buying Guide", "Selling Tips", "Market Analysis", "Investment", "Finance"]
      , n = e.filter(o => o.featured)
      , r = e.filter(o => !o.featured);
    return a.jsx("div", {
        className: "min-h-screen bg-surface-gradient",
        children: a.jsxs("div", {
            className: "max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12",
            children: [a.jsxs("div", {
                className: "text-center mb-12",
                children: [a.jsx("h1", {
                    className: "text-4xl md:text-5xl font-bold text-foreground mb-4",
                    children: "Real Estate Insights & Tips"
                }), a.jsx("p", {
                    className: "text-xl text-muted-foreground max-w-2xl mx-auto mb-8",
                    children: "Stay informed with the latest market trends, expert advice, and insider tips from our real estate professionals."
                }), a.jsxs("div", {
                    className: "max-w-md mx-auto relative",
                    children: [a.jsx(wy, {
                        className: "absolute left-3 top-3 h-4 w-4 text-muted-foreground"
                    }), a.jsx(Ee, {
                        placeholder: "Search articles...",
                        className: "pl-10"
                    })]
                })]
            }), a.jsx("div", {
                className: "flex flex-wrap justify-center gap-2 mb-12",
                children: t.map(o => a.jsx(rt, {
                    variant: "outline",
                    className: "cursor-pointer hover:bg-primary hover:text-primary-foreground transition-colors",
                    children: o
                }, o))
            }), a.jsxs("div", {
                className: "mb-16",
                children: [a.jsx("h2", {
                    className: "text-2xl font-bold text-foreground mb-8",
                    children: "Featured Articles"
                }), a.jsx("div", {
                    className: "grid lg:grid-cols-2 gap-8",
                    children: n.map(o => a.jsxs(Ce, {
                        className: "overflow-hidden shadow-medium hover:shadow-strong transition-all duration-300 group",
                        children: [a.jsxs("div", {
                            className: "relative overflow-hidden",
                            children: [a.jsx("img", {
                                src: o.image,
                                alt: o.title,
                                className: "w-full h-64 object-cover group-hover:scale-105 transition-transform duration-300"
                            }), a.jsx(rt, {
                                className: "absolute top-4 left-4 bg-accent text-accent-foreground",
                                children: o.category
                            })]
                        }), a.jsxs("div", {
                            className: "p-6",
                            children: [a.jsxs("div", {
                                className: "flex items-center text-sm text-muted-foreground mb-3 space-x-4",
                                children: [a.jsxs("div", {
                                    className: "flex items-center",
                                    children: [a.jsx(wr, {
                                        className: "w-4 h-4 mr-1"
                                    }), a.jsx("span", {
                                        children: o.author
                                    })]
                                }), a.jsxs("div", {
                                    className: "flex items-center",
                                    children: [a.jsx(Jr, {
                                        className: "w-4 h-4 mr-1"
                                    }), a.jsx("span", {
                                        children: new Date(o.date).toLocaleDateString()
                                    })]
                                }), a.jsxs("div", {
                                    className: "flex items-center",
                                    children: [a.jsx(os, {
                                        className: "w-4 h-4 mr-1"
                                    }), a.jsx("span", {
                                        children: o.readTime
                                    })]
                                })]
                            }), a.jsx("h3", {
                                className: "text-xl font-bold text-foreground mb-3 line-clamp-2",
                                children: o.title
                            }), a.jsx("p", {
                                className: "text-muted-foreground leading-relaxed mb-4 line-clamp-3",
                                children: o.excerpt
                            }), a.jsx(Fe, {
                                to: `/blog/${o.slug}`,
                                children: a.jsxs(ae, {
                                    variant: "ghost",
                                    className: "text-primary hover:text-primary-dark p-0",
                                    children: ["Read More", a.jsx(ha, {
                                        className: "w-4 h-4 ml-2"
                                    })]
                                })
                            })]
                        })]
                    }, o.id))
                })]
            }), a.jsxs("div", {
                children: [a.jsx("h2", {
                    className: "text-2xl font-bold text-foreground mb-8",
                    children: "Latest Articles"
                }), a.jsx("div", {
                    className: "grid md:grid-cols-2 lg:grid-cols-3 gap-6",
                    children: r.map(o => a.jsxs(Ce, {
                        className: "overflow-hidden shadow-soft hover:shadow-medium transition-all duration-300 group",
                        children: [a.jsxs("div", {
                            className: "relative overflow-hidden",
                            children: [a.jsx("img", {
                                src: o.image,
                                alt: o.title,
                                className: "w-full h-48 object-cover group-hover:scale-105 transition-transform duration-300"
                            }), a.jsx(rt, {
                                className: "absolute top-4 left-4 bg-primary text-primary-foreground",
                                children: o.category
                            })]
                        }), a.jsxs("div", {
                            className: "p-6",
                            children: [a.jsxs("div", {
                                className: "flex items-center text-sm text-muted-foreground mb-3",
                                children: [a.jsx(Jr, {
                                    className: "w-4 h-4 mr-1"
                                }), a.jsx("span", {
                                    children: new Date(o.date).toLocaleDateString()
                                }), a.jsx("span", {
                                    className: "mx-2",
                                    children: "•"
                                }), a.jsx(os, {
                                    className: "w-4 h-4 mr-1"
                                }), a.jsx("span", {
                                    children: o.readTime
                                })]
                            }), a.jsx("h3", {
                                className: "text-lg font-semibold text-foreground mb-3 line-clamp-2",
                                children: o.title
                            }), a.jsx("p", {
                                className: "text-muted-foreground text-sm leading-relaxed mb-4 line-clamp-3",
                                children: o.excerpt
                            }), a.jsxs("div", {
                                className: "flex items-center justify-between",
                                children: [a.jsxs("div", {
                                    className: "flex items-center text-sm text-muted-foreground",
                                    children: [a.jsx(wr, {
                                        className: "w-4 h-4 mr-1"
                                    }), a.jsx("span", {
                                        children: o.author
                                    })]
                                }), a.jsx(Fe, {
                                    to: `/blog/${o.slug}`,
                                    children: a.jsxs(ae, {
                                        variant: "ghost",
                                        size: "sm",
                                        className: "text-primary hover:text-primary-dark p-0",
                                        children: ["Read More", a.jsx(ha, {
                                            className: "w-4 h-4 ml-1"
                                        })]
                                    })
                                })]
                            })]
                        })]
                    }, o.id))
                })]
            }), a.jsxs(Ce, {
                className: "mt-16 p-8 text-center shadow-medium bg-primary text-primary-foreground",
                children: [a.jsx("h3", {
                    className: "text-2xl font-bold mb-4",
                    children: "Stay Updated with Market Insights"
                }), a.jsx("p", {
                    className: "text-primary-foreground/80 mb-6 max-w-2xl mx-auto",
                    children: "Subscribe to our newsletter for the latest real estate trends, market analysis, and expert tips delivered straight to your inbox."
                }), a.jsxs("div", {
                    className: "flex flex-col sm:flex-row gap-4 max-w-md mx-auto",
                    children: [a.jsx(Ee, {
                        placeholder: "Enter your email",
                        className: "bg-primary-foreground text-primary flex-1"
                    }), a.jsx(ae, {
                        className: "bg-accent-gradient hover:shadow-accent text-primary font-semibold",
                        children: "Subscribe"
                    })]
                })]
            })]
        })
    })
}
;
var l4 = "Separator"
  , cp = "horizontal"
  , c4 = ["horizontal", "vertical"]
  , q0 = m.forwardRef( (e, t) => {
    const {decorative: n, orientation: r=cp, ...o} = e
      , s = u4(r) ? r : cp
      , l = n ? {
        role: "none"
    } : {
        "aria-orientation": s === "vertical" ? s : void 0,
        role: "separator"
    };
    return a.jsx(te.div, {
        "data-orientation": s,
        ...l,
        ...o,
        ref: t
    })
}
);
q0.displayName = l4;
function u4(e) {
    return c4.includes(e)
}
var X0 = q0;
const J0 = m.forwardRef( ({className: e, orientation: t="horizontal", decorative: n=!0, ...r}, o) => a.jsx(X0, {
    ref: o,
    decorative: n,
    orientation: t,
    className: re("shrink-0 bg-border", t === "horizontal" ? "h-[1px] w-full" : "h-full w-[1px]", e),
    ...r
}));
J0.displayName = X0.displayName;
const d4 = () => {
    Ik();
    const e = {
        id: "1",
        slug: "home-buying-guide-2024",
        title: "The Complete Home Buying Guide for 2024",
        excerpt: "Everything you need to know about buying your first home in today's market, from getting pre-approved to closing day.",
        image: Xt,
        category: "Buying Guide",
        author: "Sarah Johnson",
        date: "2024-01-15",
        readTime: "8 min read",
        content: `
      <h2>Getting Started with Your Home Purchase</h2>
      <p>Buying your first home is one of the most significant financial decisions you'll make in your lifetime. With the right preparation and knowledge, you can navigate the process confidently and secure the home of your dreams.</p>
      
      <h3>1. Determine Your Budget</h3>
      <p>Before you start looking at properties, it's crucial to understand what you can afford. A good rule of thumb is that your monthly housing payment shouldn't exceed 28% of your gross monthly income.</p>
      
      <h3>2. Get Pre-Approved for a Mortgage</h3>
      <p>Getting pre-approved for a mortgage gives you a clear picture of how much you can borrow and shows sellers that you're a serious buyer. This can give you a competitive edge in a hot market.</p>
      
      <h3>3. Find the Right Real Estate Agent</h3>
      <p>A good real estate agent will be your guide through the entire process. Look for someone with experience in your target area and a track record of successful transactions.</p>
      
      <h3>4. Start House Hunting</h3>
      <p>Once you know your budget and have your financing in place, the fun part begins! Make a list of your must-haves versus nice-to-haves to help narrow down your options.</p>
      
      <h3>5. Make an Offer</h3>
      <p>When you find the right property, your agent will help you craft a competitive offer. In today's market, you may need to be prepared to act quickly.</p>
      
      <h3>6. Get a Home Inspection</h3>
      <p>Never skip the home inspection! This is your opportunity to identify any potential issues with the property before finalizing the purchase.</p>
      
      <h3>7. Finalize Your Mortgage</h3>
      <p>Work with your lender to complete all necessary paperwork and meet any conditions required for your loan approval.</p>
      
      <h3>8. Close on Your Home</h3>
      <p>The final step is the closing, where you'll sign all the paperwork and get the keys to your new home!</p>
      
      <h2>Tips for Success</h2>
      <ul>
        <li>Start saving for a down payment early</li>
        <li>Improve your credit score before applying for a mortgage</li>
        <li>Get quotes from multiple lenders</li>
        <li>Don't forget about closing costs</li>
        <li>Be prepared to act quickly in competitive markets</li>
      </ul>
      
      <h2>Common Mistakes to Avoid</h2>
      <p>Many first-time homebuyers make similar mistakes that can be easily avoided with proper preparation:</p>
      <ul>
        <li>Not getting pre-approved before house hunting</li>
        <li>Falling in love with a home outside your budget</li>
        <li>Skipping the home inspection</li>
        <li>Making major financial changes during the mortgage process</li>
        <li>Not budgeting for maintenance and repairs</li>
      </ul>
      
      <h2>Conclusion</h2>
      <p>Buying a home is a significant milestone, but with proper preparation and the right team of professionals, it can be an exciting and rewarding experience. Take your time, do your research, and don't be afraid to ask questions along the way.</p>
    `
    }
      , t = [{
        id: "2",
        slug: "market-trends-analysis",
        title: "Real Estate Market Trends: What to Expect This Year",
        image: yn,
        category: "Market Analysis",
        date: "2024-01-12",
        readTime: "6 min read"
    }, {
        id: "3",
        slug: "selling-tips-maximize-value",
        title: "10 Tips to Maximize Your Home's Value Before Selling",
        image: _n,
        category: "Selling Tips",
        date: "2024-01-10",
        readTime: "5 min read"
    }, {
        id: "4",
        slug: "investment-opportunities",
        title: "Investment Opportunities in Emerging Neighborhoods",
        image: Xt,
        category: "Investment",
        date: "2024-01-08",
        readTime: "7 min read"
    }];
    return a.jsx("div", {
        className: "min-h-screen bg-surface-gradient",
        children: a.jsxs("div", {
            className: "max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8",
            children: [a.jsx(Fe, {
                to: "/blog",
                children: a.jsxs(ae, {
                    variant: "ghost",
                    className: "mb-6 text-primary hover:text-primary-dark",
                    children: [a.jsx(pS, {
                        className: "w-4 h-4 mr-2"
                    }), "Back to Blog"]
                })
            }), a.jsxs("article", {
                className: "mb-12",
                children: [a.jsxs("div", {
                    className: "mb-6",
                    children: [a.jsx(rt, {
                        className: "mb-4 bg-accent/10 text-accent-foreground border-accent/20",
                        children: e.category
                    }), a.jsx("h1", {
                        className: "text-3xl md:text-4xl lg:text-5xl font-bold text-foreground mb-4 leading-tight",
                        children: e.title
                    }), a.jsx("p", {
                        className: "text-xl text-muted-foreground leading-relaxed",
                        children: e.excerpt
                    })]
                }), a.jsxs("div", {
                    className: "flex flex-wrap items-center justify-between gap-4 mb-8",
                    children: [a.jsxs("div", {
                        className: "flex items-center space-x-6 text-sm text-muted-foreground",
                        children: [a.jsxs("div", {
                            className: "flex items-center",
                            children: [a.jsx(wr, {
                                className: "w-4 h-4 mr-2"
                            }), a.jsx("span", {
                                className: "font-medium",
                                children: e.author
                            })]
                        }), a.jsxs("div", {
                            className: "flex items-center",
                            children: [a.jsx(Jr, {
                                className: "w-4 h-4 mr-2"
                            }), a.jsx("span", {
                                children: new Date(e.date).toLocaleDateString()
                            })]
                        }), a.jsxs("div", {
                            className: "flex items-center",
                            children: [a.jsx(os, {
                                className: "w-4 h-4 mr-2"
                            }), a.jsx("span", {
                                children: e.readTime
                            })]
                        })]
                    }), a.jsxs("div", {
                        className: "flex items-center space-x-2",
                        children: [a.jsxs(ae, {
                            variant: "outline",
                            size: "sm",
                            children: [a.jsx(_S, {
                                className: "w-4 h-4 mr-2"
                            }), "Share"]
                        }), a.jsxs(ae, {
                            variant: "outline",
                            size: "sm",
                            children: [a.jsx(xS, {
                                className: "w-4 h-4 mr-2"
                            }), "Save"]
                        })]
                    })]
                }), a.jsx("img", {
                    src: e.image,
                    alt: e.title,
                    className: "w-full h-64 md:h-96 object-cover rounded-xl shadow-medium mb-8"
                }), a.jsx("div", {
                    className: "prose prose-lg max-w-none text-foreground",
                    dangerouslySetInnerHTML: {
                        __html: e.content
                    },
                    style: {
                        color: "hsl(var(--foreground))"
                    }
                })]
            }), a.jsx(J0, {
                className: "my-12"
            }), a.jsx(Ce, {
                className: "p-6 mb-12 shadow-soft",
                children: a.jsxs("div", {
                    className: "flex items-start space-x-4",
                    children: [a.jsx("div", {
                        className: "w-16 h-16 bg-accent/10 rounded-full flex items-center justify-center",
                        children: a.jsx(wr, {
                            className: "w-8 h-8 text-accent"
                        })
                    }), a.jsxs("div", {
                        className: "flex-1",
                        children: [a.jsxs("h3", {
                            className: "text-lg font-semibold text-foreground mb-2",
                            children: ["About ", e.author]
                        }), a.jsx("p", {
                            className: "text-muted-foreground leading-relaxed",
                            children: "Sarah is a senior real estate advisor with over 10 years of experience helping clients navigate the home buying process. She specializes in first-time buyer education and market analysis."
                        })]
                    })]
                })
            }), a.jsxs("div", {
                children: [a.jsx("h2", {
                    className: "text-2xl font-bold text-foreground mb-8",
                    children: "Recommended Articles"
                }), a.jsx("div", {
                    className: "grid md:grid-cols-3 gap-6",
                    children: t.map(n => a.jsxs(Ce, {
                        className: "overflow-hidden shadow-soft hover:shadow-medium transition-all duration-300 group",
                        children: [a.jsxs("div", {
                            className: "relative overflow-hidden",
                            children: [a.jsx("img", {
                                src: n.image,
                                alt: n.title,
                                className: "w-full h-48 object-cover group-hover:scale-105 transition-transform duration-300"
                            }), a.jsx(rt, {
                                className: "absolute top-4 left-4 bg-primary text-primary-foreground",
                                children: n.category
                            })]
                        }), a.jsxs("div", {
                            className: "p-6",
                            children: [a.jsxs("div", {
                                className: "flex items-center text-sm text-muted-foreground mb-3",
                                children: [a.jsx(Jr, {
                                    className: "w-4 h-4 mr-1"
                                }), a.jsx("span", {
                                    children: new Date(n.date).toLocaleDateString()
                                }), a.jsx("span", {
                                    className: "mx-2",
                                    children: "•"
                                }), a.jsx(os, {
                                    className: "w-4 h-4 mr-1"
                                }), a.jsx("span", {
                                    children: n.readTime
                                })]
                            }), a.jsx("h3", {
                                className: "text-lg font-semibold text-foreground mb-4 line-clamp-2",
                                children: n.title
                            }), a.jsx(Fe, {
                                to: `/blog/${n.slug}`,
                                children: a.jsxs(ae, {
                                    variant: "ghost",
                                    className: "text-primary hover:text-primary-dark p-0",
                                    children: ["Read Article", a.jsx(ha, {
                                        className: "w-4 h-4 ml-2"
                                    })]
                                })
                            })]
                        })]
                    }, n.id))
                })]
            }), a.jsxs(Ce, {
                className: "mt-12 p-8 text-center shadow-medium bg-primary text-primary-foreground",
                children: [a.jsx("h3", {
                    className: "text-2xl font-bold mb-4",
                    children: "Stay Updated with Our Latest Articles"
                }), a.jsx("p", {
                    className: "text-primary-foreground/80 mb-6",
                    children: "Get the latest real estate insights and tips delivered to your inbox"
                }), a.jsx(ae, {
                    className: "bg-accent-gradient hover:shadow-accent text-primary font-semibold",
                    children: "Subscribe to Newsletter"
                })]
            })]
        })
    })
}
;
function le(e) {
    const t = Object.prototype.toString.call(e);
    return e instanceof Date || typeof e == "object" && t === "[object Date]" ? new e.constructor(+e) : typeof e == "number" || t === "[object Number]" || typeof e == "string" || t === "[object String]" ? new Date(e) : new Date(NaN)
}
function bt(e, t) {
    return e instanceof Date ? new e.constructor(t) : new Date(t)
}
function tt(e, t) {
    const n = le(e);
    return isNaN(t) ? bt(e, NaN) : (t && n.setDate(n.getDate() + t),
    n)
}
function nn(e, t) {
    const n = le(e);
    if (isNaN(t))
        return bt(e, NaN);
    if (!t)
        return n;
    const r = n.getDate()
      , o = bt(e, n.getTime());
    o.setMonth(n.getMonth() + t + 1, 0);
    const s = o.getDate();
    return r >= s ? o : (n.setFullYear(o.getFullYear(), o.getMonth(), r),
    n)
}
const $f = 6048e5
  , f4 = 864e5;
let m4 = {};
function Aa() {
    return m4
}
function wn(e, t) {
    var l, c, u, d;
    const n = Aa()
      , r = (t == null ? void 0 : t.weekStartsOn) ?? ((c = (l = t == null ? void 0 : t.locale) == null ? void 0 : l.options) == null ? void 0 : c.weekStartsOn) ?? n.weekStartsOn ?? ((d = (u = n.locale) == null ? void 0 : u.options) == null ? void 0 : d.weekStartsOn) ?? 0
      , o = le(e)
      , s = o.getDay()
      , i = (s < r ? 7 : 0) + s - r;
    return o.setDate(o.getDate() - i),
    o.setHours(0, 0, 0, 0),
    o
}
function ro(e) {
    return wn(e, {
        weekStartsOn: 1
    })
}
function Z0(e) {
    const t = le(e)
      , n = t.getFullYear()
      , r = bt(e, 0);
    r.setFullYear(n + 1, 0, 4),
    r.setHours(0, 0, 0, 0);
    const o = ro(r)
      , s = bt(e, 0);
    s.setFullYear(n, 0, 4),
    s.setHours(0, 0, 0, 0);
    const i = ro(s);
    return t.getTime() >= o.getTime() ? n + 1 : t.getTime() >= i.getTime() ? n : n - 1
}
function cs(e) {
    const t = le(e);
    return t.setHours(0, 0, 0, 0),
    t
}
function ml(e) {
    const t = le(e)
      , n = new Date(Date.UTC(t.getFullYear(), t.getMonth(), t.getDate(), t.getHours(), t.getMinutes(), t.getSeconds(), t.getMilliseconds()));
    return n.setUTCFullYear(t.getFullYear()),
    +e - +n
}
function hn(e, t) {
    const n = cs(e)
      , r = cs(t)
      , o = +n - ml(n)
      , s = +r - ml(r);
    return Math.round((o - s) / f4)
}
function h4(e) {
    const t = Z0(e)
      , n = bt(e, 0);
    return n.setFullYear(t, 0, 4),
    n.setHours(0, 0, 0, 0),
    ro(n)
}
function fd(e, t) {
    const n = t * 7;
    return tt(e, n)
}
function p4(e, t) {
    return nn(e, t * 12)
}
function v4(e) {
    let t;
    return e.forEach(function(n) {
        const r = le(n);
        (t === void 0 || t < r || isNaN(Number(r))) && (t = r)
    }),
    t || new Date(NaN)
}
function g4(e) {
    let t;
    return e.forEach(n => {
        const r = le(n);
        (!t || t > r || isNaN(+r)) && (t = r)
    }
    ),
    t || new Date(NaN)
}
function ut(e, t) {
    const n = cs(e)
      , r = cs(t);
    return +n == +r
}
function Bf(e) {
    return e instanceof Date || typeof e == "object" && Object.prototype.toString.call(e) === "[object Date]"
}
function y4(e) {
    if (!Bf(e) && typeof e != "number")
        return !1;
    const t = le(e);
    return !isNaN(Number(t))
}
function ba(e, t) {
    const n = le(e)
      , r = le(t)
      , o = n.getFullYear() - r.getFullYear()
      , s = n.getMonth() - r.getMonth();
    return o * 12 + s
}
function x4(e, t, n) {
    const r = wn(e, n)
      , o = wn(t, n)
      , s = +r - ml(r)
      , i = +o - ml(o);
    return Math.round((s - i) / $f)
}
function Wf(e) {
    const t = le(e)
      , n = t.getMonth();
    return t.setFullYear(t.getFullYear(), n + 1, 0),
    t.setHours(23, 59, 59, 999),
    t
}
function ht(e) {
    const t = le(e);
    return t.setDate(1),
    t.setHours(0, 0, 0, 0),
    t
}
function ew(e) {
    const t = le(e)
      , n = bt(e, 0);
    return n.setFullYear(t.getFullYear(), 0, 1),
    n.setHours(0, 0, 0, 0),
    n
}
function Hf(e, t) {
    var l, c, u, d;
    const n = Aa()
      , r = (t == null ? void 0 : t.weekStartsOn) ?? ((c = (l = t == null ? void 0 : t.locale) == null ? void 0 : l.options) == null ? void 0 : c.weekStartsOn) ?? n.weekStartsOn ?? ((d = (u = n.locale) == null ? void 0 : u.options) == null ? void 0 : d.weekStartsOn) ?? 0
      , o = le(e)
      , s = o.getDay()
      , i = (s < r ? -7 : 0) + 6 - (s - r);
    return o.setDate(o.getDate() + i),
    o.setHours(23, 59, 59, 999),
    o
}
function tw(e) {
    return Hf(e, {
        weekStartsOn: 1
    })
}
const w4 = {
    lessThanXSeconds: {
        one: "less than a second",
        other: "less than {{count}} seconds"
    },
    xSeconds: {
        one: "1 second",
        other: "{{count}} seconds"
    },
    halfAMinute: "half a minute",
    lessThanXMinutes: {
        one: "less than a minute",
        other: "less than {{count}} minutes"
    },
    xMinutes: {
        one: "1 minute",
        other: "{{count}} minutes"
    },
    aboutXHours: {
        one: "about 1 hour",
        other: "about {{count}} hours"
    },
    xHours: {
        one: "1 hour",
        other: "{{count}} hours"
    },
    xDays: {
        one: "1 day",
        other: "{{count}} days"
    },
    aboutXWeeks: {
        one: "about 1 week",
        other: "about {{count}} weeks"
    },
    xWeeks: {
        one: "1 week",
        other: "{{count}} weeks"
    },
    aboutXMonths: {
        one: "about 1 month",
        other: "about {{count}} months"
    },
    xMonths: {
        one: "1 month",
        other: "{{count}} months"
    },
    aboutXYears: {
        one: "about 1 year",
        other: "about {{count}} years"
    },
    xYears: {
        one: "1 year",
        other: "{{count}} years"
    },
    overXYears: {
        one: "over 1 year",
        other: "over {{count}} years"
    },
    almostXYears: {
        one: "almost 1 year",
        other: "almost {{count}} years"
    }
}
  , b4 = (e, t, n) => {
    let r;
    const o = w4[e];
    return typeof o == "string" ? r = o : t === 1 ? r = o.one : r = o.other.replace("{{count}}", t.toString()),
    n != null && n.addSuffix ? n.comparison && n.comparison > 0 ? "in " + r : r + " ago" : r
}
;
function Bc(e) {
    return (t={}) => {
        const n = t.width ? String(t.width) : e.defaultWidth;
        return e.formats[n] || e.formats[e.defaultWidth]
    }
}
const N4 = {
    full: "EEEE, MMMM do, y",
    long: "MMMM do, y",
    medium: "MMM d, y",
    short: "MM/dd/yyyy"
}
  , S4 = {
    full: "h:mm:ss a zzzz",
    long: "h:mm:ss a z",
    medium: "h:mm:ss a",
    short: "h:mm a"
}
  , j4 = {
    full: "{{date}} 'at' {{time}}",
    long: "{{date}} 'at' {{time}}",
    medium: "{{date}}, {{time}}",
    short: "{{date}}, {{time}}"
}
  , C4 = {
    date: Bc({
        formats: N4,
        defaultWidth: "full"
    }),
    time: Bc({
        formats: S4,
        defaultWidth: "full"
    }),
    dateTime: Bc({
        formats: j4,
        defaultWidth: "full"
    })
}
  , k4 = {
    lastWeek: "'last' eeee 'at' p",
    yesterday: "'yesterday at' p",
    today: "'today at' p",
    tomorrow: "'tomorrow at' p",
    nextWeek: "eeee 'at' p",
    other: "P"
}
  , E4 = (e, t, n, r) => k4[e];
function Ds(e) {
    return (t, n) => {
        const r = n != null && n.context ? String(n.context) : "standalone";
        let o;
        if (r === "formatting" && e.formattingValues) {
            const i = e.defaultFormattingWidth || e.defaultWidth
              , l = n != null && n.width ? String(n.width) : i;
            o = e.formattingValues[l] || e.formattingValues[i]
        } else {
            const i = e.defaultWidth
              , l = n != null && n.width ? String(n.width) : e.defaultWidth;
            o = e.values[l] || e.values[i]
        }
        const s = e.argumentCallback ? e.argumentCallback(t) : t;
        return o[s]
    }
}
const P4 = {
    narrow: ["B", "A"],
    abbreviated: ["BC", "AD"],
    wide: ["Before Christ", "Anno Domini"]
}
  , T4 = {
    narrow: ["1", "2", "3", "4"],
    abbreviated: ["Q1", "Q2", "Q3", "Q4"],
    wide: ["1st quarter", "2nd quarter", "3rd quarter", "4th quarter"]
}
  , M4 = {
    narrow: ["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"],
    abbreviated: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    wide: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
}
  , R4 = {
    narrow: ["S", "M", "T", "W", "T", "F", "S"],
    short: ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"],
    abbreviated: ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
    wide: ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
}
  , _4 = {
    narrow: {
        am: "a",
        pm: "p",
        midnight: "mi",
        noon: "n",
        morning: "morning",
        afternoon: "afternoon",
        evening: "evening",
        night: "night"
    },
    abbreviated: {
        am: "AM",
        pm: "PM",
        midnight: "midnight",
        noon: "noon",
        morning: "morning",
        afternoon: "afternoon",
        evening: "evening",
        night: "night"
    },
    wide: {
        am: "a.m.",
        pm: "p.m.",
        midnight: "midnight",
        noon: "noon",
        morning: "morning",
        afternoon: "afternoon",
        evening: "evening",
        night: "night"
    }
}
  , D4 = {
    narrow: {
        am: "a",
        pm: "p",
        midnight: "mi",
        noon: "n",
        morning: "in the morning",
        afternoon: "in the afternoon",
        evening: "in the evening",
        night: "at night"
    },
    abbreviated: {
        am: "AM",
        pm: "PM",
        midnight: "midnight",
        noon: "noon",
        morning: "in the morning",
        afternoon: "in the afternoon",
        evening: "in the evening",
        night: "at night"
    },
    wide: {
        am: "a.m.",
        pm: "p.m.",
        midnight: "midnight",
        noon: "noon",
        morning: "in the morning",
        afternoon: "in the afternoon",
        evening: "in the evening",
        night: "at night"
    }
}
  , O4 = (e, t) => {
    const n = Number(e)
      , r = n % 100;
    if (r > 20 || r < 10)
        switch (r % 10) {
        case 1:
            return n + "st";
        case 2:
            return n + "nd";
        case 3:
            return n + "rd"
        }
    return n + "th"
}
  , A4 = {
    ordinalNumber: O4,
    era: Ds({
        values: P4,
        defaultWidth: "wide"
    }),
    quarter: Ds({
        values: T4,
        defaultWidth: "wide",
        argumentCallback: e => e - 1
    }),
    month: Ds({
        values: M4,
        defaultWidth: "wide"
    }),
    day: Ds({
        values: R4,
        defaultWidth: "wide"
    }),
    dayPeriod: Ds({
        values: _4,
        defaultWidth: "wide",
        formattingValues: D4,
        defaultFormattingWidth: "wide"
    })
};
function Os(e) {
    return (t, n={}) => {
        const r = n.width
          , o = r && e.matchPatterns[r] || e.matchPatterns[e.defaultMatchWidth]
          , s = t.match(o);
        if (!s)
            return null;
        const i = s[0]
          , l = r && e.parsePatterns[r] || e.parsePatterns[e.defaultParseWidth]
          , c = Array.isArray(l) ? L4(l, f => f.test(i)) : I4(l, f => f.test(i));
        let u;
        u = e.valueCallback ? e.valueCallback(c) : c,
        u = n.valueCallback ? n.valueCallback(u) : u;
        const d = t.slice(i.length);
        return {
            value: u,
            rest: d
        }
    }
}
function I4(e, t) {
    for (const n in e)
        if (Object.prototype.hasOwnProperty.call(e, n) && t(e[n]))
            return n
}
function L4(e, t) {
    for (let n = 0; n < e.length; n++)
        if (t(e[n]))
            return n
}
function F4(e) {
    return (t, n={}) => {
        const r = t.match(e.matchPattern);
        if (!r)
            return null;
        const o = r[0]
          , s = t.match(e.parsePattern);
        if (!s)
            return null;
        let i = e.valueCallback ? e.valueCallback(s[0]) : s[0];
        i = n.valueCallback ? n.valueCallback(i) : i;
        const l = t.slice(o.length);
        return {
            value: i,
            rest: l
        }
    }
}
const z4 = /^(\d+)(th|st|nd|rd)?/i
  , $4 = /\d+/i
  , B4 = {
    narrow: /^(b|a)/i,
    abbreviated: /^(b\.?\s?c\.?|b\.?\s?c\.?\s?e\.?|a\.?\s?d\.?|c\.?\s?e\.?)/i,
    wide: /^(before christ|before common era|anno domini|common era)/i
}
  , W4 = {
    any: [/^b/i, /^(a|c)/i]
}
  , H4 = {
    narrow: /^[1234]/i,
    abbreviated: /^q[1234]/i,
    wide: /^[1234](th|st|nd|rd)? quarter/i
}
  , V4 = {
    any: [/1/i, /2/i, /3/i, /4/i]
}
  , U4 = {
    narrow: /^[jfmasond]/i,
    abbreviated: /^(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)/i,
    wide: /^(january|february|march|april|may|june|july|august|september|october|november|december)/i
}
  , Y4 = {
    narrow: [/^j/i, /^f/i, /^m/i, /^a/i, /^m/i, /^j/i, /^j/i, /^a/i, /^s/i, /^o/i, /^n/i, /^d/i],
    any: [/^ja/i, /^f/i, /^mar/i, /^ap/i, /^may/i, /^jun/i, /^jul/i, /^au/i, /^s/i, /^o/i, /^n/i, /^d/i]
}
  , K4 = {
    narrow: /^[smtwf]/i,
    short: /^(su|mo|tu|we|th|fr|sa)/i,
    abbreviated: /^(sun|mon|tue|wed|thu|fri|sat)/i,
    wide: /^(sunday|monday|tuesday|wednesday|thursday|friday|saturday)/i
}
  , Q4 = {
    narrow: [/^s/i, /^m/i, /^t/i, /^w/i, /^t/i, /^f/i, /^s/i],
    any: [/^su/i, /^m/i, /^tu/i, /^w/i, /^th/i, /^f/i, /^sa/i]
}
  , G4 = {
    narrow: /^(a|p|mi|n|(in the|at) (morning|afternoon|evening|night))/i,
    any: /^([ap]\.?\s?m\.?|midnight|noon|(in the|at) (morning|afternoon|evening|night))/i
}
  , q4 = {
    any: {
        am: /^a/i,
        pm: /^p/i,
        midnight: /^mi/i,
        noon: /^no/i,
        morning: /morning/i,
        afternoon: /afternoon/i,
        evening: /evening/i,
        night: /night/i
    }
}
  , X4 = {
    ordinalNumber: F4({
        matchPattern: z4,
        parsePattern: $4,
        valueCallback: e => parseInt(e, 10)
    }),
    era: Os({
        matchPatterns: B4,
        defaultMatchWidth: "wide",
        parsePatterns: W4,
        defaultParseWidth: "any"
    }),
    quarter: Os({
        matchPatterns: H4,
        defaultMatchWidth: "wide",
        parsePatterns: V4,
        defaultParseWidth: "any",
        valueCallback: e => e + 1
    }),
    month: Os({
        matchPatterns: U4,
        defaultMatchWidth: "wide",
        parsePatterns: Y4,
        defaultParseWidth: "any"
    }),
    day: Os({
        matchPatterns: K4,
        defaultMatchWidth: "wide",
        parsePatterns: Q4,
        defaultParseWidth: "any"
    }),
    dayPeriod: Os({
        matchPatterns: G4,
        defaultMatchWidth: "any",
        parsePatterns: q4,
        defaultParseWidth: "any"
    })
}
  , nw = {
    code: "en-US",
    formatDistance: b4,
    formatLong: C4,
    formatRelative: E4,
    localize: A4,
    match: X4,
    options: {
        weekStartsOn: 0,
        firstWeekContainsDate: 1
    }
};
function J4(e) {
    const t = le(e);
    return hn(t, ew(t)) + 1
}
function rw(e) {
    const t = le(e)
      , n = +ro(t) - +h4(t);
    return Math.round(n / $f) + 1
}
function ow(e, t) {
    var d, f, g, h;
    const n = le(e)
      , r = n.getFullYear()
      , o = Aa()
      , s = (t == null ? void 0 : t.firstWeekContainsDate) ?? ((f = (d = t == null ? void 0 : t.locale) == null ? void 0 : d.options) == null ? void 0 : f.firstWeekContainsDate) ?? o.firstWeekContainsDate ?? ((h = (g = o.locale) == null ? void 0 : g.options) == null ? void 0 : h.firstWeekContainsDate) ?? 1
      , i = bt(e, 0);
    i.setFullYear(r + 1, 0, s),
    i.setHours(0, 0, 0, 0);
    const l = wn(i, t)
      , c = bt(e, 0);
    c.setFullYear(r, 0, s),
    c.setHours(0, 0, 0, 0);
    const u = wn(c, t);
    return n.getTime() >= l.getTime() ? r + 1 : n.getTime() >= u.getTime() ? r : r - 1
}
function Z4(e, t) {
    var l, c, u, d;
    const n = Aa()
      , r = (t == null ? void 0 : t.firstWeekContainsDate) ?? ((c = (l = t == null ? void 0 : t.locale) == null ? void 0 : l.options) == null ? void 0 : c.firstWeekContainsDate) ?? n.firstWeekContainsDate ?? ((d = (u = n.locale) == null ? void 0 : u.options) == null ? void 0 : d.firstWeekContainsDate) ?? 1
      , o = ow(e, t)
      , s = bt(e, 0);
    return s.setFullYear(o, 0, r),
    s.setHours(0, 0, 0, 0),
    wn(s, t)
}
function sw(e, t) {
    const n = le(e)
      , r = +wn(n, t) - +Z4(n, t);
    return Math.round(r / $f) + 1
}
function he(e, t) {
    const n = e < 0 ? "-" : ""
      , r = Math.abs(e).toString().padStart(t, "0");
    return n + r
}
const Kn = {
    y(e, t) {
        const n = e.getFullYear()
          , r = n > 0 ? n : 1 - n;
        return he(t === "yy" ? r % 100 : r, t.length)
    },
    M(e, t) {
        const n = e.getMonth();
        return t === "M" ? String(n + 1) : he(n + 1, 2)
    },
    d(e, t) {
        return he(e.getDate(), t.length)
    },
    a(e, t) {
        const n = e.getHours() / 12 >= 1 ? "pm" : "am";
        switch (t) {
        case "a":
        case "aa":
            return n.toUpperCase();
        case "aaa":
            return n;
        case "aaaaa":
            return n[0];
        case "aaaa":
        default:
            return n === "am" ? "a.m." : "p.m."
        }
    },
    h(e, t) {
        return he(e.getHours() % 12 || 12, t.length)
    },
    H(e, t) {
        return he(e.getHours(), t.length)
    },
    m(e, t) {
        return he(e.getMinutes(), t.length)
    },
    s(e, t) {
        return he(e.getSeconds(), t.length)
    },
    S(e, t) {
        const n = t.length
          , r = e.getMilliseconds()
          , o = Math.trunc(r * Math.pow(10, n - 3));
        return he(o, t.length)
    }
}
  , xo = {
    am: "am",
    pm: "pm",
    midnight: "midnight",
    noon: "noon",
    morning: "morning",
    afternoon: "afternoon",
    evening: "evening",
    night: "night"
}
  , up = {
    G: function(e, t, n) {
        const r = e.getFullYear() > 0 ? 1 : 0;
        switch (t) {
        case "G":
        case "GG":
        case "GGG":
            return n.era(r, {
                width: "abbreviated"
            });
        case "GGGGG":
            return n.era(r, {
                width: "narrow"
            });
        case "GGGG":
        default:
            return n.era(r, {
                width: "wide"
            })
        }
    },
    y: function(e, t, n) {
        if (t === "yo") {
            const r = e.getFullYear()
              , o = r > 0 ? r : 1 - r;
            return n.ordinalNumber(o, {
                unit: "year"
            })
        }
        return Kn.y(e, t)
    },
    Y: function(e, t, n, r) {
        const o = ow(e, r)
          , s = o > 0 ? o : 1 - o;
        if (t === "YY") {
            const i = s % 100;
            return he(i, 2)
        }
        return t === "Yo" ? n.ordinalNumber(s, {
            unit: "year"
        }) : he(s, t.length)
    },
    R: function(e, t) {
        const n = Z0(e);
        return he(n, t.length)
    },
    u: function(e, t) {
        const n = e.getFullYear();
        return he(n, t.length)
    },
    Q: function(e, t, n) {
        const r = Math.ceil((e.getMonth() + 1) / 3);
        switch (t) {
        case "Q":
            return String(r);
        case "QQ":
            return he(r, 2);
        case "Qo":
            return n.ordinalNumber(r, {
                unit: "quarter"
            });
        case "QQQ":
            return n.quarter(r, {
                width: "abbreviated",
                context: "formatting"
            });
        case "QQQQQ":
            return n.quarter(r, {
                width: "narrow",
                context: "formatting"
            });
        case "QQQQ":
        default:
            return n.quarter(r, {
                width: "wide",
                context: "formatting"
            })
        }
    },
    q: function(e, t, n) {
        const r = Math.ceil((e.getMonth() + 1) / 3);
        switch (t) {
        case "q":
            return String(r);
        case "qq":
            return he(r, 2);
        case "qo":
            return n.ordinalNumber(r, {
                unit: "quarter"
            });
        case "qqq":
            return n.quarter(r, {
                width: "abbreviated",
                context: "standalone"
            });
        case "qqqqq":
            return n.quarter(r, {
                width: "narrow",
                context: "standalone"
            });
        case "qqqq":
        default:
            return n.quarter(r, {
                width: "wide",
                context: "standalone"
            })
        }
    },
    M: function(e, t, n) {
        const r = e.getMonth();
        switch (t) {
        case "M":
        case "MM":
            return Kn.M(e, t);
        case "Mo":
            return n.ordinalNumber(r + 1, {
                unit: "month"
            });
        case "MMM":
            return n.month(r, {
                width: "abbreviated",
                context: "formatting"
            });
        case "MMMMM":
            return n.month(r, {
                width: "narrow",
                context: "formatting"
            });
        case "MMMM":
        default:
            return n.month(r, {
                width: "wide",
                context: "formatting"
            })
        }
    },
    L: function(e, t, n) {
        const r = e.getMonth();
        switch (t) {
        case "L":
            return String(r + 1);
        case "LL":
            return he(r + 1, 2);
        case "Lo":
            return n.ordinalNumber(r + 1, {
                unit: "month"
            });
        case "LLL":
            return n.month(r, {
                width: "abbreviated",
                context: "standalone"
            });
        case "LLLLL":
            return n.month(r, {
                width: "narrow",
                context: "standalone"
            });
        case "LLLL":
        default:
            return n.month(r, {
                width: "wide",
                context: "standalone"
            })
        }
    },
    w: function(e, t, n, r) {
        const o = sw(e, r);
        return t === "wo" ? n.ordinalNumber(o, {
            unit: "week"
        }) : he(o, t.length)
    },
    I: function(e, t, n) {
        const r = rw(e);
        return t === "Io" ? n.ordinalNumber(r, {
            unit: "week"
        }) : he(r, t.length)
    },
    d: function(e, t, n) {
        return t === "do" ? n.ordinalNumber(e.getDate(), {
            unit: "date"
        }) : Kn.d(e, t)
    },
    D: function(e, t, n) {
        const r = J4(e);
        return t === "Do" ? n.ordinalNumber(r, {
            unit: "dayOfYear"
        }) : he(r, t.length)
    },
    E: function(e, t, n) {
        const r = e.getDay();
        switch (t) {
        case "E":
        case "EE":
        case "EEE":
            return n.day(r, {
                width: "abbreviated",
                context: "formatting"
            });
        case "EEEEE":
            return n.day(r, {
                width: "narrow",
                context: "formatting"
            });
        case "EEEEEE":
            return n.day(r, {
                width: "short",
                context: "formatting"
            });
        case "EEEE":
        default:
            return n.day(r, {
                width: "wide",
                context: "formatting"
            })
        }
    },
    e: function(e, t, n, r) {
        const o = e.getDay()
          , s = (o - r.weekStartsOn + 8) % 7 || 7;
        switch (t) {
        case "e":
            return String(s);
        case "ee":
            return he(s, 2);
        case "eo":
            return n.ordinalNumber(s, {
                unit: "day"
            });
        case "eee":
            return n.day(o, {
                width: "abbreviated",
                context: "formatting"
            });
        case "eeeee":
            return n.day(o, {
                width: "narrow",
                context: "formatting"
            });
        case "eeeeee":
            return n.day(o, {
                width: "short",
                context: "formatting"
            });
        case "eeee":
        default:
            return n.day(o, {
                width: "wide",
                context: "formatting"
            })
        }
    },
    c: function(e, t, n, r) {
        const o = e.getDay()
          , s = (o - r.weekStartsOn + 8) % 7 || 7;
        switch (t) {
        case "c":
            return String(s);
        case "cc":
            return he(s, t.length);
        case "co":
            return n.ordinalNumber(s, {
                unit: "day"
            });
        case "ccc":
            return n.day(o, {
                width: "abbreviated",
                context: "standalone"
            });
        case "ccccc":
            return n.day(o, {
                width: "narrow",
                context: "standalone"
            });
        case "cccccc":
            return n.day(o, {
                width: "short",
                context: "standalone"
            });
        case "cccc":
        default:
            return n.day(o, {
                width: "wide",
                context: "standalone"
            })
        }
    },
    i: function(e, t, n) {
        const r = e.getDay()
          , o = r === 0 ? 7 : r;
        switch (t) {
        case "i":
            return String(o);
        case "ii":
            return he(o, t.length);
        case "io":
            return n.ordinalNumber(o, {
                unit: "day"
            });
        case "iii":
            return n.day(r, {
                width: "abbreviated",
                context: "formatting"
            });
        case "iiiii":
            return n.day(r, {
                width: "narrow",
                context: "formatting"
            });
        case "iiiiii":
            return n.day(r, {
                width: "short",
                context: "formatting"
            });
        case "iiii":
        default:
            return n.day(r, {
                width: "wide",
                context: "formatting"
            })
        }
    },
    a: function(e, t, n) {
        const o = e.getHours() / 12 >= 1 ? "pm" : "am";
        switch (t) {
        case "a":
        case "aa":
            return n.dayPeriod(o, {
                width: "abbreviated",
                context: "formatting"
            });
        case "aaa":
            return n.dayPeriod(o, {
                width: "abbreviated",
                context: "formatting"
            }).toLowerCase();
        case "aaaaa":
            return n.dayPeriod(o, {
                width: "narrow",
                context: "formatting"
            });
        case "aaaa":
        default:
            return n.dayPeriod(o, {
                width: "wide",
                context: "formatting"
            })
        }
    },
    b: function(e, t, n) {
        const r = e.getHours();
        let o;
        switch (r === 12 ? o = xo.noon : r === 0 ? o = xo.midnight : o = r / 12 >= 1 ? "pm" : "am",
        t) {
        case "b":
        case "bb":
            return n.dayPeriod(o, {
                width: "abbreviated",
                context: "formatting"
            });
        case "bbb":
            return n.dayPeriod(o, {
                width: "abbreviated",
                context: "formatting"
            }).toLowerCase();
        case "bbbbb":
            return n.dayPeriod(o, {
                width: "narrow",
                context: "formatting"
            });
        case "bbbb":
        default:
            return n.dayPeriod(o, {
                width: "wide",
                context: "formatting"
            })
        }
    },
    B: function(e, t, n) {
        const r = e.getHours();
        let o;
        switch (r >= 17 ? o = xo.evening : r >= 12 ? o = xo.afternoon : r >= 4 ? o = xo.morning : o = xo.night,
        t) {
        case "B":
        case "BB":
        case "BBB":
            return n.dayPeriod(o, {
                width: "abbreviated",
                context: "formatting"
            });
        case "BBBBB":
            return n.dayPeriod(o, {
                width: "narrow",
                context: "formatting"
            });
        case "BBBB":
        default:
            return n.dayPeriod(o, {
                width: "wide",
                context: "formatting"
            })
        }
    },
    h: function(e, t, n) {
        if (t === "ho") {
            let r = e.getHours() % 12;
            return r === 0 && (r = 12),
            n.ordinalNumber(r, {
                unit: "hour"
            })
        }
        return Kn.h(e, t)
    },
    H: function(e, t, n) {
        return t === "Ho" ? n.ordinalNumber(e.getHours(), {
            unit: "hour"
        }) : Kn.H(e, t)
    },
    K: function(e, t, n) {
        const r = e.getHours() % 12;
        return t === "Ko" ? n.ordinalNumber(r, {
            unit: "hour"
        }) : he(r, t.length)
    },
    k: function(e, t, n) {
        let r = e.getHours();
        return r === 0 && (r = 24),
        t === "ko" ? n.ordinalNumber(r, {
            unit: "hour"
        }) : he(r, t.length)
    },
    m: function(e, t, n) {
        return t === "mo" ? n.ordinalNumber(e.getMinutes(), {
            unit: "minute"
        }) : Kn.m(e, t)
    },
    s: function(e, t, n) {
        return t === "so" ? n.ordinalNumber(e.getSeconds(), {
            unit: "second"
        }) : Kn.s(e, t)
    },
    S: function(e, t) {
        return Kn.S(e, t)
    },
    X: function(e, t, n) {
        const r = e.getTimezoneOffset();
        if (r === 0)
            return "Z";
        switch (t) {
        case "X":
            return fp(r);
        case "XXXX":
        case "XX":
            return Ar(r);
        case "XXXXX":
        case "XXX":
        default:
            return Ar(r, ":")
        }
    },
    x: function(e, t, n) {
        const r = e.getTimezoneOffset();
        switch (t) {
        case "x":
            return fp(r);
        case "xxxx":
        case "xx":
            return Ar(r);
        case "xxxxx":
        case "xxx":
        default:
            return Ar(r, ":")
        }
    },
    O: function(e, t, n) {
        const r = e.getTimezoneOffset();
        switch (t) {
        case "O":
        case "OO":
        case "OOO":
            return "GMT" + dp(r, ":");
        case "OOOO":
        default:
            return "GMT" + Ar(r, ":")
        }
    },
    z: function(e, t, n) {
        const r = e.getTimezoneOffset();
        switch (t) {
        case "z":
        case "zz":
        case "zzz":
            return "GMT" + dp(r, ":");
        case "zzzz":
        default:
            return "GMT" + Ar(r, ":")
        }
    },
    t: function(e, t, n) {
        const r = Math.trunc(e.getTime() / 1e3);
        return he(r, t.length)
    },
    T: function(e, t, n) {
        const r = e.getTime();
        return he(r, t.length)
    }
};
function dp(e, t="") {
    const n = e > 0 ? "-" : "+"
      , r = Math.abs(e)
      , o = Math.trunc(r / 60)
      , s = r % 60;
    return s === 0 ? n + String(o) : n + String(o) + t + he(s, 2)
}
function fp(e, t) {
    return e % 60 === 0 ? (e > 0 ? "-" : "+") + he(Math.abs(e) / 60, 2) : Ar(e, t)
}
function Ar(e, t="") {
    const n = e > 0 ? "-" : "+"
      , r = Math.abs(e)
      , o = he(Math.trunc(r / 60), 2)
      , s = he(r % 60, 2);
    return n + o + t + s
}
const mp = (e, t) => {
    switch (e) {
    case "P":
        return t.date({
            width: "short"
        });
    case "PP":
        return t.date({
            width: "medium"
        });
    case "PPP":
        return t.date({
            width: "long"
        });
    case "PPPP":
    default:
        return t.date({
            width: "full"
        })
    }
}
  , aw = (e, t) => {
    switch (e) {
    case "p":
        return t.time({
            width: "short"
        });
    case "pp":
        return t.time({
            width: "medium"
        });
    case "ppp":
        return t.time({
            width: "long"
        });
    case "pppp":
    default:
        return t.time({
            width: "full"
        })
    }
}
  , eT = (e, t) => {
    const n = e.match(/(P+)(p+)?/) || []
      , r = n[1]
      , o = n[2];
    if (!o)
        return mp(e, t);
    let s;
    switch (r) {
    case "P":
        s = t.dateTime({
            width: "short"
        });
        break;
    case "PP":
        s = t.dateTime({
            width: "medium"
        });
        break;
    case "PPP":
        s = t.dateTime({
            width: "long"
        });
        break;
    case "PPPP":
    default:
        s = t.dateTime({
            width: "full"
        });
        break
    }
    return s.replace("{{date}}", mp(r, t)).replace("{{time}}", aw(o, t))
}
  , tT = {
    p: aw,
    P: eT
}
  , nT = /^D+$/
  , rT = /^Y+$/
  , oT = ["D", "DD", "YY", "YYYY"];
function sT(e) {
    return nT.test(e)
}
function aT(e) {
    return rT.test(e)
}
function iT(e, t, n) {
    const r = lT(e, t, n);
    if (console.warn(r),
    oT.includes(e))
        throw new RangeError(r)
}
function lT(e, t, n) {
    const r = e[0] === "Y" ? "years" : "days of the month";
    return `Use \`${e.toLowerCase()}\` instead of \`${e}\` (in \`${t}\`) for formatting ${r} to the input \`${n}\`; see: https://github.com/date-fns/date-fns/blob/master/docs/unicodeTokens.md`
}
const cT = /[yYQqMLwIdDecihHKkms]o|(\w)\1*|''|'(''|[^'])+('|$)|./g
  , uT = /P+p+|P+|p+|''|'(''|[^'])+('|$)|./g
  , dT = /^'([^]*?)'?$/
  , fT = /''/g
  , mT = /[a-zA-Z]/;
function co(e, t, n) {
    var d, f, g, h, b, v, w, y;
    const r = Aa()
      , o = (n == null ? void 0 : n.locale) ?? r.locale ?? nw
      , s = (n == null ? void 0 : n.firstWeekContainsDate) ?? ((f = (d = n == null ? void 0 : n.locale) == null ? void 0 : d.options) == null ? void 0 : f.firstWeekContainsDate) ?? r.firstWeekContainsDate ?? ((h = (g = r.locale) == null ? void 0 : g.options) == null ? void 0 : h.firstWeekContainsDate) ?? 1
      , i = (n == null ? void 0 : n.weekStartsOn) ?? ((v = (b = n == null ? void 0 : n.locale) == null ? void 0 : b.options) == null ? void 0 : v.weekStartsOn) ?? r.weekStartsOn ?? ((y = (w = r.locale) == null ? void 0 : w.options) == null ? void 0 : y.weekStartsOn) ?? 0
      , l = le(e);
    if (!y4(l))
        throw new RangeError("Invalid time value");
    let c = t.match(uT).map(p => {
        const x = p[0];
        if (x === "p" || x === "P") {
            const N = tT[x];
            return N(p, o.formatLong)
        }
        return p
    }
    ).join("").match(cT).map(p => {
        if (p === "''")
            return {
                isToken: !1,
                value: "'"
            };
        const x = p[0];
        if (x === "'")
            return {
                isToken: !1,
                value: hT(p)
            };
        if (up[x])
            return {
                isToken: !0,
                value: p
            };
        if (x.match(mT))
            throw new RangeError("Format string contains an unescaped latin alphabet character `" + x + "`");
        return {
            isToken: !1,
            value: p
        }
    }
    );
    o.localize.preprocessor && (c = o.localize.preprocessor(l, c));
    const u = {
        firstWeekContainsDate: s,
        weekStartsOn: i,
        locale: o
    };
    return c.map(p => {
        if (!p.isToken)
            return p.value;
        const x = p.value;
        (!(n != null && n.useAdditionalWeekYearTokens) && aT(x) || !(n != null && n.useAdditionalDayOfYearTokens) && sT(x)) && iT(x, t, String(e));
        const N = up[x[0]];
        return N(l, x, o.localize, u)
    }
    ).join("")
}
function hT(e) {
    const t = e.match(dT);
    return t ? t[1].replace(fT, "'") : e
}
function pT(e) {
    const t = le(e)
      , n = t.getFullYear()
      , r = t.getMonth()
      , o = bt(e, 0);
    return o.setFullYear(n, r + 1, 0),
    o.setHours(0, 0, 0, 0),
    o.getDate()
}
function vT(e) {
    return Math.trunc(+le(e) / 1e3)
}
function gT(e) {
    const t = le(e)
      , n = t.getMonth();
    return t.setFullYear(t.getFullYear(), n + 1, 0),
    t.setHours(0, 0, 0, 0),
    t
}
function yT(e, t) {
    return x4(gT(e), ht(e), t) + 1
}
function md(e, t) {
    const n = le(e)
      , r = le(t);
    return n.getTime() > r.getTime()
}
function iw(e, t) {
    const n = le(e)
      , r = le(t);
    return +n < +r
}
function Vf(e, t) {
    const n = le(e)
      , r = le(t);
    return n.getFullYear() === r.getFullYear() && n.getMonth() === r.getMonth()
}
function xT(e, t) {
    const n = le(e)
      , r = le(t);
    return n.getFullYear() === r.getFullYear()
}
function Wc(e, t) {
    return tt(e, -t)
}
function Hc(e, t) {
    const n = le(e)
      , r = n.getFullYear()
      , o = n.getDate()
      , s = bt(e, 0);
    s.setFullYear(r, t, 15),
    s.setHours(0, 0, 0, 0);
    const i = pT(s);
    return n.setMonth(t, Math.min(o, i)),
    n
}
function hp(e, t) {
    const n = le(e);
    return isNaN(+n) ? bt(e, NaN) : (n.setFullYear(t),
    n)
}
var K = function() {
    return K = Object.assign || function(t) {
        for (var n, r = 1, o = arguments.length; r < o; r++) {
            n = arguments[r];
            for (var s in n)
                Object.prototype.hasOwnProperty.call(n, s) && (t[s] = n[s])
        }
        return t
    }
    ,
    K.apply(this, arguments)
};
function wT(e, t) {
    var n = {};
    for (var r in e)
        Object.prototype.hasOwnProperty.call(e, r) && t.indexOf(r) < 0 && (n[r] = e[r]);
    if (e != null && typeof Object.getOwnPropertySymbols == "function")
        for (var o = 0, r = Object.getOwnPropertySymbols(e); o < r.length; o++)
            t.indexOf(r[o]) < 0 && Object.prototype.propertyIsEnumerable.call(e, r[o]) && (n[r[o]] = e[r[o]]);
    return n
}
function lw(e, t, n) {
    for (var r = 0, o = t.length, s; r < o; r++)
        (s || !(r in t)) && (s || (s = Array.prototype.slice.call(t, 0, r)),
        s[r] = t[r]);
    return e.concat(s || Array.prototype.slice.call(t))
}
function Ia(e) {
    return e.mode === "multiple"
}
function La(e) {
    return e.mode === "range"
}
function Gl(e) {
    return e.mode === "single"
}
var bT = {
    root: "rdp",
    multiple_months: "rdp-multiple_months",
    with_weeknumber: "rdp-with_weeknumber",
    vhidden: "rdp-vhidden",
    button_reset: "rdp-button_reset",
    button: "rdp-button",
    caption: "rdp-caption",
    caption_start: "rdp-caption_start",
    caption_end: "rdp-caption_end",
    caption_between: "rdp-caption_between",
    caption_label: "rdp-caption_label",
    caption_dropdowns: "rdp-caption_dropdowns",
    dropdown: "rdp-dropdown",
    dropdown_month: "rdp-dropdown_month",
    dropdown_year: "rdp-dropdown_year",
    dropdown_icon: "rdp-dropdown_icon",
    months: "rdp-months",
    month: "rdp-month",
    table: "rdp-table",
    tbody: "rdp-tbody",
    tfoot: "rdp-tfoot",
    head: "rdp-head",
    head_row: "rdp-head_row",
    head_cell: "rdp-head_cell",
    nav: "rdp-nav",
    nav_button: "rdp-nav_button",
    nav_button_previous: "rdp-nav_button_previous",
    nav_button_next: "rdp-nav_button_next",
    nav_icon: "rdp-nav_icon",
    row: "rdp-row",
    weeknumber: "rdp-weeknumber",
    cell: "rdp-cell",
    day: "rdp-day",
    day_today: "rdp-day_today",
    day_outside: "rdp-day_outside",
    day_selected: "rdp-day_selected",
    day_disabled: "rdp-day_disabled",
    day_hidden: "rdp-day_hidden",
    day_range_start: "rdp-day_range_start",
    day_range_end: "rdp-day_range_end",
    day_range_middle: "rdp-day_range_middle"
};
function NT(e, t) {
    return co(e, "LLLL y", t)
}
function ST(e, t) {
    return co(e, "d", t)
}
function jT(e, t) {
    return co(e, "LLLL", t)
}
function CT(e) {
    return "".concat(e)
}
function kT(e, t) {
    return co(e, "cccccc", t)
}
function ET(e, t) {
    return co(e, "yyyy", t)
}
var PT = Object.freeze({
    __proto__: null,
    formatCaption: NT,
    formatDay: ST,
    formatMonthCaption: jT,
    formatWeekNumber: CT,
    formatWeekdayName: kT,
    formatYearCaption: ET
})
  , TT = function(e, t, n) {
    return co(e, "do MMMM (EEEE)", n)
}
  , MT = function() {
    return "Month: "
}
  , RT = function() {
    return "Go to next month"
}
  , _T = function() {
    return "Go to previous month"
}
  , DT = function(e, t) {
    return co(e, "cccc", t)
}
  , OT = function(e) {
    return "Week n. ".concat(e)
}
  , AT = function() {
    return "Year: "
}
  , IT = Object.freeze({
    __proto__: null,
    labelDay: TT,
    labelMonthDropdown: MT,
    labelNext: RT,
    labelPrevious: _T,
    labelWeekNumber: OT,
    labelWeekday: DT,
    labelYearDropdown: AT
});
function LT() {
    var e = "buttons"
      , t = bT
      , n = nw
      , r = {}
      , o = {}
      , s = 1
      , i = {}
      , l = new Date;
    return {
        captionLayout: e,
        classNames: t,
        formatters: PT,
        labels: IT,
        locale: n,
        modifiersClassNames: r,
        modifiers: o,
        numberOfMonths: s,
        styles: i,
        today: l,
        mode: "default"
    }
}
function FT(e) {
    var t = e.fromYear
      , n = e.toYear
      , r = e.fromMonth
      , o = e.toMonth
      , s = e.fromDate
      , i = e.toDate;
    return r ? s = ht(r) : t && (s = new Date(t,0,1)),
    o ? i = Wf(o) : n && (i = new Date(n,11,31)),
    {
        fromDate: s ? cs(s) : void 0,
        toDate: i ? cs(i) : void 0
    }
}
var cw = m.createContext(void 0);
function zT(e) {
    var t, n = e.initialProps, r = LT(), o = FT(n), s = o.fromDate, i = o.toDate, l = (t = n.captionLayout) !== null && t !== void 0 ? t : r.captionLayout;
    l !== "buttons" && (!s || !i) && (l = "buttons");
    var c;
    (Gl(n) || Ia(n) || La(n)) && (c = n.onSelect);
    var u = K(K(K({}, r), n), {
        captionLayout: l,
        classNames: K(K({}, r.classNames), n.classNames),
        components: K({}, n.components),
        formatters: K(K({}, r.formatters), n.formatters),
        fromDate: s,
        labels: K(K({}, r.labels), n.labels),
        mode: n.mode || r.mode,
        modifiers: K(K({}, r.modifiers), n.modifiers),
        modifiersClassNames: K(K({}, r.modifiersClassNames), n.modifiersClassNames),
        onSelect: c,
        styles: K(K({}, r.styles), n.styles),
        toDate: i
    });
    return a.jsx(cw.Provider, {
        value: u,
        children: e.children
    })
}
function ye() {
    var e = m.useContext(cw);
    if (!e)
        throw new Error("useDayPicker must be used within a DayPickerProvider.");
    return e
}
function uw(e) {
    var t = ye()
      , n = t.locale
      , r = t.classNames
      , o = t.styles
      , s = t.formatters.formatCaption;
    return a.jsx("div", {
        className: r.caption_label,
        style: o.caption_label,
        "aria-live": "polite",
        role: "presentation",
        id: e.id,
        children: s(e.displayMonth, {
            locale: n
        })
    })
}
function $T(e) {
    return a.jsx("svg", K({
        width: "8px",
        height: "8px",
        viewBox: "0 0 120 120",
        "data-testid": "iconDropdown"
    }, e, {
        children: a.jsx("path", {
            d: "M4.22182541,48.2218254 C8.44222828,44.0014225 15.2388494,43.9273804 19.5496459,47.9996989 L19.7781746,48.2218254 L60,88.443 L100.221825,48.2218254 C104.442228,44.0014225 111.238849,43.9273804 115.549646,47.9996989 L115.778175,48.2218254 C119.998577,52.4422283 120.07262,59.2388494 116.000301,63.5496459 L115.778175,63.7781746 L67.7781746,111.778175 C63.5577717,115.998577 56.7611506,116.07262 52.4503541,112.000301 L52.2218254,111.778175 L4.22182541,63.7781746 C-0.0739418023,59.4824074 -0.0739418023,52.5175926 4.22182541,48.2218254 Z",
            fill: "currentColor",
            fillRule: "nonzero"
        })
    }))
}
function dw(e) {
    var t, n, r = e.onChange, o = e.value, s = e.children, i = e.caption, l = e.className, c = e.style, u = ye(), d = (n = (t = u.components) === null || t === void 0 ? void 0 : t.IconDropdown) !== null && n !== void 0 ? n : $T;
    return a.jsxs("div", {
        className: l,
        style: c,
        children: [a.jsx("span", {
            className: u.classNames.vhidden,
            children: e["aria-label"]
        }), a.jsx("select", {
            name: e.name,
            "aria-label": e["aria-label"],
            className: u.classNames.dropdown,
            style: u.styles.dropdown,
            value: o,
            onChange: r,
            children: s
        }), a.jsxs("div", {
            className: u.classNames.caption_label,
            style: u.styles.caption_label,
            "aria-hidden": "true",
            children: [i, a.jsx(d, {
                className: u.classNames.dropdown_icon,
                style: u.styles.dropdown_icon
            })]
        })]
    })
}
function BT(e) {
    var t, n = ye(), r = n.fromDate, o = n.toDate, s = n.styles, i = n.locale, l = n.formatters.formatMonthCaption, c = n.classNames, u = n.components, d = n.labels.labelMonthDropdown;
    if (!r)
        return a.jsx(a.Fragment, {});
    if (!o)
        return a.jsx(a.Fragment, {});
    var f = [];
    if (xT(r, o))
        for (var g = ht(r), h = r.getMonth(); h <= o.getMonth(); h++)
            f.push(Hc(g, h));
    else
        for (var g = ht(new Date), h = 0; h <= 11; h++)
            f.push(Hc(g, h));
    var b = function(w) {
        var y = Number(w.target.value)
          , p = Hc(ht(e.displayMonth), y);
        e.onChange(p)
    }
      , v = (t = u == null ? void 0 : u.Dropdown) !== null && t !== void 0 ? t : dw;
    return a.jsx(v, {
        name: "months",
        "aria-label": d(),
        className: c.dropdown_month,
        style: s.dropdown_month,
        onChange: b,
        value: e.displayMonth.getMonth(),
        caption: l(e.displayMonth, {
            locale: i
        }),
        children: f.map(function(w) {
            return a.jsx("option", {
                value: w.getMonth(),
                children: l(w, {
                    locale: i
                })
            }, w.getMonth())
        })
    })
}
function WT(e) {
    var t, n = e.displayMonth, r = ye(), o = r.fromDate, s = r.toDate, i = r.locale, l = r.styles, c = r.classNames, u = r.components, d = r.formatters.formatYearCaption, f = r.labels.labelYearDropdown, g = [];
    if (!o)
        return a.jsx(a.Fragment, {});
    if (!s)
        return a.jsx(a.Fragment, {});
    for (var h = o.getFullYear(), b = s.getFullYear(), v = h; v <= b; v++)
        g.push(hp(ew(new Date), v));
    var w = function(p) {
        var x = hp(ht(n), Number(p.target.value));
        e.onChange(x)
    }
      , y = (t = u == null ? void 0 : u.Dropdown) !== null && t !== void 0 ? t : dw;
    return a.jsx(y, {
        name: "years",
        "aria-label": f(),
        className: c.dropdown_year,
        style: l.dropdown_year,
        onChange: w,
        value: n.getFullYear(),
        caption: d(n, {
            locale: i
        }),
        children: g.map(function(p) {
            return a.jsx("option", {
                value: p.getFullYear(),
                children: d(p, {
                    locale: i
                })
            }, p.getFullYear())
        })
    })
}
function HT(e, t) {
    var n = m.useState(e)
      , r = n[0]
      , o = n[1]
      , s = t === void 0 ? r : t;
    return [s, o]
}
function VT(e) {
    var t = e.month
      , n = e.defaultMonth
      , r = e.today
      , o = t || n || r || new Date
      , s = e.toDate
      , i = e.fromDate
      , l = e.numberOfMonths
      , c = l === void 0 ? 1 : l;
    if (s && ba(s, o) < 0) {
        var u = -1 * (c - 1);
        o = nn(s, u)
    }
    return i && ba(o, i) < 0 && (o = i),
    ht(o)
}
function UT() {
    var e = ye()
      , t = VT(e)
      , n = HT(t, e.month)
      , r = n[0]
      , o = n[1]
      , s = function(i) {
        var l;
        if (!e.disableNavigation) {
            var c = ht(i);
            o(c),
            (l = e.onMonthChange) === null || l === void 0 || l.call(e, c)
        }
    };
    return [r, s]
}
function YT(e, t) {
    for (var n = t.reverseMonths, r = t.numberOfMonths, o = ht(e), s = ht(nn(o, r)), i = ba(s, o), l = [], c = 0; c < i; c++) {
        var u = nn(o, c);
        l.push(u)
    }
    return n && (l = l.reverse()),
    l
}
function KT(e, t) {
    if (!t.disableNavigation) {
        var n = t.toDate
          , r = t.pagedNavigation
          , o = t.numberOfMonths
          , s = o === void 0 ? 1 : o
          , i = r ? s : 1
          , l = ht(e);
        if (!n)
            return nn(l, i);
        var c = ba(n, e);
        if (!(c < s))
            return nn(l, i)
    }
}
function QT(e, t) {
    if (!t.disableNavigation) {
        var n = t.fromDate
          , r = t.pagedNavigation
          , o = t.numberOfMonths
          , s = o === void 0 ? 1 : o
          , i = r ? s : 1
          , l = ht(e);
        if (!n)
            return nn(l, -i);
        var c = ba(l, n);
        if (!(c <= 0))
            return nn(l, -i)
    }
}
var fw = m.createContext(void 0);
function GT(e) {
    var t = ye()
      , n = UT()
      , r = n[0]
      , o = n[1]
      , s = YT(r, t)
      , i = KT(r, t)
      , l = QT(r, t)
      , c = function(f) {
        return s.some(function(g) {
            return Vf(f, g)
        })
    }
      , u = function(f, g) {
        c(f) || (g && iw(f, g) ? o(nn(f, 1 + t.numberOfMonths * -1)) : o(f))
    }
      , d = {
        currentMonth: r,
        displayMonths: s,
        goToMonth: o,
        goToDate: u,
        previousMonth: l,
        nextMonth: i,
        isDateDisplayed: c
    };
    return a.jsx(fw.Provider, {
        value: d,
        children: e.children
    })
}
function Fa() {
    var e = m.useContext(fw);
    if (!e)
        throw new Error("useNavigation must be used within a NavigationProvider");
    return e
}
function pp(e) {
    var t, n = ye(), r = n.classNames, o = n.styles, s = n.components, i = Fa().goToMonth, l = function(d) {
        i(nn(d, e.displayIndex ? -e.displayIndex : 0))
    }, c = (t = s == null ? void 0 : s.CaptionLabel) !== null && t !== void 0 ? t : uw, u = a.jsx(c, {
        id: e.id,
        displayMonth: e.displayMonth
    });
    return a.jsxs("div", {
        className: r.caption_dropdowns,
        style: o.caption_dropdowns,
        children: [a.jsx("div", {
            className: r.vhidden,
            children: u
        }), a.jsx(BT, {
            onChange: l,
            displayMonth: e.displayMonth
        }), a.jsx(WT, {
            onChange: l,
            displayMonth: e.displayMonth
        })]
    })
}
function qT(e) {
    return a.jsx("svg", K({
        width: "16px",
        height: "16px",
        viewBox: "0 0 120 120"
    }, e, {
        children: a.jsx("path", {
            d: "M69.490332,3.34314575 C72.6145263,0.218951416 77.6798462,0.218951416 80.8040405,3.34314575 C83.8617626,6.40086786 83.9268205,11.3179931 80.9992143,14.4548388 L80.8040405,14.6568542 L35.461,60 L80.8040405,105.343146 C83.8617626,108.400868 83.9268205,113.317993 80.9992143,116.454839 L80.8040405,116.656854 C77.7463184,119.714576 72.8291931,119.779634 69.6923475,116.852028 L69.490332,116.656854 L18.490332,65.6568542 C15.4326099,62.5991321 15.367552,57.6820069 18.2951583,54.5451612 L18.490332,54.3431458 L69.490332,3.34314575 Z",
            fill: "currentColor",
            fillRule: "nonzero"
        })
    }))
}
function XT(e) {
    return a.jsx("svg", K({
        width: "16px",
        height: "16px",
        viewBox: "0 0 120 120"
    }, e, {
        children: a.jsx("path", {
            d: "M49.8040405,3.34314575 C46.6798462,0.218951416 41.6145263,0.218951416 38.490332,3.34314575 C35.4326099,6.40086786 35.367552,11.3179931 38.2951583,14.4548388 L38.490332,14.6568542 L83.8333725,60 L38.490332,105.343146 C35.4326099,108.400868 35.367552,113.317993 38.2951583,116.454839 L38.490332,116.656854 C41.5480541,119.714576 46.4651794,119.779634 49.602025,116.852028 L49.8040405,116.656854 L100.804041,65.6568542 C103.861763,62.5991321 103.926821,57.6820069 100.999214,54.5451612 L100.804041,54.3431458 L49.8040405,3.34314575 Z",
            fill: "currentColor"
        })
    }))
}
var hl = m.forwardRef(function(e, t) {
    var n = ye()
      , r = n.classNames
      , o = n.styles
      , s = [r.button_reset, r.button];
    e.className && s.push(e.className);
    var i = s.join(" ")
      , l = K(K({}, o.button_reset), o.button);
    return e.style && Object.assign(l, e.style),
    a.jsx("button", K({}, e, {
        ref: t,
        type: "button",
        className: i,
        style: l
    }))
});
function JT(e) {
    var t, n, r = ye(), o = r.dir, s = r.locale, i = r.classNames, l = r.styles, c = r.labels, u = c.labelPrevious, d = c.labelNext, f = r.components;
    if (!e.nextMonth && !e.previousMonth)
        return a.jsx(a.Fragment, {});
    var g = u(e.previousMonth, {
        locale: s
    })
      , h = [i.nav_button, i.nav_button_previous].join(" ")
      , b = d(e.nextMonth, {
        locale: s
    })
      , v = [i.nav_button, i.nav_button_next].join(" ")
      , w = (t = f == null ? void 0 : f.IconRight) !== null && t !== void 0 ? t : XT
      , y = (n = f == null ? void 0 : f.IconLeft) !== null && n !== void 0 ? n : qT;
    return a.jsxs("div", {
        className: i.nav,
        style: l.nav,
        children: [!e.hidePrevious && a.jsx(hl, {
            name: "previous-month",
            "aria-label": g,
            className: h,
            style: l.nav_button_previous,
            disabled: !e.previousMonth,
            onClick: e.onPreviousClick,
            children: o === "rtl" ? a.jsx(w, {
                className: i.nav_icon,
                style: l.nav_icon
            }) : a.jsx(y, {
                className: i.nav_icon,
                style: l.nav_icon
            })
        }), !e.hideNext && a.jsx(hl, {
            name: "next-month",
            "aria-label": b,
            className: v,
            style: l.nav_button_next,
            disabled: !e.nextMonth,
            onClick: e.onNextClick,
            children: o === "rtl" ? a.jsx(y, {
                className: i.nav_icon,
                style: l.nav_icon
            }) : a.jsx(w, {
                className: i.nav_icon,
                style: l.nav_icon
            })
        })]
    })
}
function vp(e) {
    var t = ye().numberOfMonths
      , n = Fa()
      , r = n.previousMonth
      , o = n.nextMonth
      , s = n.goToMonth
      , i = n.displayMonths
      , l = i.findIndex(function(b) {
        return Vf(e.displayMonth, b)
    })
      , c = l === 0
      , u = l === i.length - 1
      , d = t > 1 && (c || !u)
      , f = t > 1 && (u || !c)
      , g = function() {
        r && s(r)
    }
      , h = function() {
        o && s(o)
    };
    return a.jsx(JT, {
        displayMonth: e.displayMonth,
        hideNext: d,
        hidePrevious: f,
        nextMonth: o,
        previousMonth: r,
        onPreviousClick: g,
        onNextClick: h
    })
}
function ZT(e) {
    var t, n = ye(), r = n.classNames, o = n.disableNavigation, s = n.styles, i = n.captionLayout, l = n.components, c = (t = l == null ? void 0 : l.CaptionLabel) !== null && t !== void 0 ? t : uw, u;
    return o ? u = a.jsx(c, {
        id: e.id,
        displayMonth: e.displayMonth
    }) : i === "dropdown" ? u = a.jsx(pp, {
        displayMonth: e.displayMonth,
        id: e.id
    }) : i === "dropdown-buttons" ? u = a.jsxs(a.Fragment, {
        children: [a.jsx(pp, {
            displayMonth: e.displayMonth,
            displayIndex: e.displayIndex,
            id: e.id
        }), a.jsx(vp, {
            displayMonth: e.displayMonth,
            displayIndex: e.displayIndex,
            id: e.id
        })]
    }) : u = a.jsxs(a.Fragment, {
        children: [a.jsx(c, {
            id: e.id,
            displayMonth: e.displayMonth,
            displayIndex: e.displayIndex
        }), a.jsx(vp, {
            displayMonth: e.displayMonth,
            id: e.id
        })]
    }),
    a.jsx("div", {
        className: r.caption,
        style: s.caption,
        children: u
    })
}
function eM(e) {
    var t = ye()
      , n = t.footer
      , r = t.styles
      , o = t.classNames.tfoot;
    return n ? a.jsx("tfoot", {
        className: o,
        style: r.tfoot,
        children: a.jsx("tr", {
            children: a.jsx("td", {
                colSpan: 8,
                children: n
            })
        })
    }) : a.jsx(a.Fragment, {})
}
function tM(e, t, n) {
    for (var r = n ? ro(new Date) : wn(new Date, {
        locale: e,
        weekStartsOn: t
    }), o = [], s = 0; s < 7; s++) {
        var i = tt(r, s);
        o.push(i)
    }
    return o
}
function nM() {
    var e = ye()
      , t = e.classNames
      , n = e.styles
      , r = e.showWeekNumber
      , o = e.locale
      , s = e.weekStartsOn
      , i = e.ISOWeek
      , l = e.formatters.formatWeekdayName
      , c = e.labels.labelWeekday
      , u = tM(o, s, i);
    return a.jsxs("tr", {
        style: n.head_row,
        className: t.head_row,
        children: [r && a.jsx("td", {
            style: n.head_cell,
            className: t.head_cell
        }), u.map(function(d, f) {
            return a.jsx("th", {
                scope: "col",
                className: t.head_cell,
                style: n.head_cell,
                "aria-label": c(d, {
                    locale: o
                }),
                children: l(d, {
                    locale: o
                })
            }, f)
        })]
    })
}
function rM() {
    var e, t = ye(), n = t.classNames, r = t.styles, o = t.components, s = (e = o == null ? void 0 : o.HeadRow) !== null && e !== void 0 ? e : nM;
    return a.jsx("thead", {
        style: r.head,
        className: n.head,
        children: a.jsx(s, {})
    })
}
function oM(e) {
    var t = ye()
      , n = t.locale
      , r = t.formatters.formatDay;
    return a.jsx(a.Fragment, {
        children: r(e.date, {
            locale: n
        })
    })
}
var Uf = m.createContext(void 0);
function sM(e) {
    if (!Ia(e.initialProps)) {
        var t = {
            selected: void 0,
            modifiers: {
                disabled: []
            }
        };
        return a.jsx(Uf.Provider, {
            value: t,
            children: e.children
        })
    }
    return a.jsx(aM, {
        initialProps: e.initialProps,
        children: e.children
    })
}
function aM(e) {
    var t = e.initialProps
      , n = e.children
      , r = t.selected
      , o = t.min
      , s = t.max
      , i = function(u, d, f) {
        var g, h;
        (g = t.onDayClick) === null || g === void 0 || g.call(t, u, d, f);
        var b = !!(d.selected && o && (r == null ? void 0 : r.length) === o);
        if (!b) {
            var v = !!(!d.selected && s && (r == null ? void 0 : r.length) === s);
            if (!v) {
                var w = r ? lw([], r) : [];
                if (d.selected) {
                    var y = w.findIndex(function(p) {
                        return ut(u, p)
                    });
                    w.splice(y, 1)
                } else
                    w.push(u);
                (h = t.onSelect) === null || h === void 0 || h.call(t, w, u, d, f)
            }
        }
    }
      , l = {
        disabled: []
    };
    r && l.disabled.push(function(u) {
        var d = s && r.length > s - 1
          , f = r.some(function(g) {
            return ut(g, u)
        });
        return !!(d && !f)
    });
    var c = {
        selected: r,
        onDayClick: i,
        modifiers: l
    };
    return a.jsx(Uf.Provider, {
        value: c,
        children: n
    })
}
function Yf() {
    var e = m.useContext(Uf);
    if (!e)
        throw new Error("useSelectMultiple must be used within a SelectMultipleProvider");
    return e
}
function iM(e, t) {
    var n = t || {}
      , r = n.from
      , o = n.to;
    return r && o ? ut(o, e) && ut(r, e) ? void 0 : ut(o, e) ? {
        from: o,
        to: void 0
    } : ut(r, e) ? void 0 : md(r, e) ? {
        from: e,
        to: o
    } : {
        from: r,
        to: e
    } : o ? md(e, o) ? {
        from: o,
        to: e
    } : {
        from: e,
        to: o
    } : r ? iw(e, r) ? {
        from: e,
        to: r
    } : {
        from: r,
        to: e
    } : {
        from: e,
        to: void 0
    }
}
var Kf = m.createContext(void 0);
function lM(e) {
    if (!La(e.initialProps)) {
        var t = {
            selected: void 0,
            modifiers: {
                range_start: [],
                range_end: [],
                range_middle: [],
                disabled: []
            }
        };
        return a.jsx(Kf.Provider, {
            value: t,
            children: e.children
        })
    }
    return a.jsx(cM, {
        initialProps: e.initialProps,
        children: e.children
    })
}
function cM(e) {
    var t = e.initialProps
      , n = e.children
      , r = t.selected
      , o = r || {}
      , s = o.from
      , i = o.to
      , l = t.min
      , c = t.max
      , u = function(h, b, v) {
        var w, y;
        (w = t.onDayClick) === null || w === void 0 || w.call(t, h, b, v);
        var p = iM(h, r);
        (y = t.onSelect) === null || y === void 0 || y.call(t, p, h, b, v)
    }
      , d = {
        range_start: [],
        range_end: [],
        range_middle: [],
        disabled: []
    };
    if (s ? (d.range_start = [s],
    i ? (d.range_end = [i],
    ut(s, i) || (d.range_middle = [{
        after: s,
        before: i
    }])) : d.range_end = [s]) : i && (d.range_start = [i],
    d.range_end = [i]),
    l && (s && !i && d.disabled.push({
        after: Wc(s, l - 1),
        before: tt(s, l - 1)
    }),
    s && i && d.disabled.push({
        after: s,
        before: tt(s, l - 1)
    }),
    !s && i && d.disabled.push({
        after: Wc(i, l - 1),
        before: tt(i, l - 1)
    })),
    c) {
        if (s && !i && (d.disabled.push({
            before: tt(s, -c + 1)
        }),
        d.disabled.push({
            after: tt(s, c - 1)
        })),
        s && i) {
            var f = hn(i, s) + 1
              , g = c - f;
            d.disabled.push({
                before: Wc(s, g)
            }),
            d.disabled.push({
                after: tt(i, g)
            })
        }
        !s && i && (d.disabled.push({
            before: tt(i, -c + 1)
        }),
        d.disabled.push({
            after: tt(i, c - 1)
        }))
    }
    return a.jsx(Kf.Provider, {
        value: {
            selected: r,
            onDayClick: u,
            modifiers: d
        },
        children: n
    })
}
function Qf() {
    var e = m.useContext(Kf);
    if (!e)
        throw new Error("useSelectRange must be used within a SelectRangeProvider");
    return e
}
function Mi(e) {
    return Array.isArray(e) ? lw([], e) : e !== void 0 ? [e] : []
}
function uM(e) {
    var t = {};
    return Object.entries(e).forEach(function(n) {
        var r = n[0]
          , o = n[1];
        t[r] = Mi(o)
    }),
    t
}
var rn;
(function(e) {
    e.Outside = "outside",
    e.Disabled = "disabled",
    e.Selected = "selected",
    e.Hidden = "hidden",
    e.Today = "today",
    e.RangeStart = "range_start",
    e.RangeEnd = "range_end",
    e.RangeMiddle = "range_middle"
}
)(rn || (rn = {}));
var dM = rn.Selected
  , Sn = rn.Disabled
  , fM = rn.Hidden
  , mM = rn.Today
  , Vc = rn.RangeEnd
  , Uc = rn.RangeMiddle
  , Yc = rn.RangeStart
  , hM = rn.Outside;
function pM(e, t, n) {
    var r, o = (r = {},
    r[dM] = Mi(e.selected),
    r[Sn] = Mi(e.disabled),
    r[fM] = Mi(e.hidden),
    r[mM] = [e.today],
    r[Vc] = [],
    r[Uc] = [],
    r[Yc] = [],
    r[hM] = [],
    r);
    return e.fromDate && o[Sn].push({
        before: e.fromDate
    }),
    e.toDate && o[Sn].push({
        after: e.toDate
    }),
    Ia(e) ? o[Sn] = o[Sn].concat(t.modifiers[Sn]) : La(e) && (o[Sn] = o[Sn].concat(n.modifiers[Sn]),
    o[Yc] = n.modifiers[Yc],
    o[Uc] = n.modifiers[Uc],
    o[Vc] = n.modifiers[Vc]),
    o
}
var mw = m.createContext(void 0);
function vM(e) {
    var t = ye()
      , n = Yf()
      , r = Qf()
      , o = pM(t, n, r)
      , s = uM(t.modifiers)
      , i = K(K({}, o), s);
    return a.jsx(mw.Provider, {
        value: i,
        children: e.children
    })
}
function hw() {
    var e = m.useContext(mw);
    if (!e)
        throw new Error("useModifiers must be used within a ModifiersProvider");
    return e
}
function gM(e) {
    return !!(e && typeof e == "object" && "before"in e && "after"in e)
}
function yM(e) {
    return !!(e && typeof e == "object" && "from"in e)
}
function xM(e) {
    return !!(e && typeof e == "object" && "after"in e)
}
function wM(e) {
    return !!(e && typeof e == "object" && "before"in e)
}
function bM(e) {
    return !!(e && typeof e == "object" && "dayOfWeek"in e)
}
function NM(e, t) {
    var n, r = t.from, o = t.to;
    if (r && o) {
        var s = hn(o, r) < 0;
        s && (n = [o, r],
        r = n[0],
        o = n[1]);
        var i = hn(e, r) >= 0 && hn(o, e) >= 0;
        return i
    }
    return o ? ut(o, e) : r ? ut(r, e) : !1
}
function SM(e) {
    return Bf(e)
}
function jM(e) {
    return Array.isArray(e) && e.every(Bf)
}
function CM(e, t) {
    return t.some(function(n) {
        if (typeof n == "boolean")
            return n;
        if (SM(n))
            return ut(e, n);
        if (jM(n))
            return n.includes(e);
        if (yM(n))
            return NM(e, n);
        if (bM(n))
            return n.dayOfWeek.includes(e.getDay());
        if (gM(n)) {
            var r = hn(n.before, e)
              , o = hn(n.after, e)
              , s = r > 0
              , i = o < 0
              , l = md(n.before, n.after);
            return l ? i && s : s || i
        }
        return xM(n) ? hn(e, n.after) > 0 : wM(n) ? hn(n.before, e) > 0 : typeof n == "function" ? n(e) : !1
    })
}
function Gf(e, t, n) {
    var r = Object.keys(t).reduce(function(s, i) {
        var l = t[i];
        return CM(e, l) && s.push(i),
        s
    }, [])
      , o = {};
    return r.forEach(function(s) {
        return o[s] = !0
    }),
    n && !Vf(e, n) && (o.outside = !0),
    o
}
function kM(e, t) {
    for (var n = ht(e[0]), r = Wf(e[e.length - 1]), o, s, i = n; i <= r; ) {
        var l = Gf(i, t)
          , c = !l.disabled && !l.hidden;
        if (!c) {
            i = tt(i, 1);
            continue
        }
        if (l.selected)
            return i;
        l.today && !s && (s = i),
        o || (o = i),
        i = tt(i, 1)
    }
    return s || o
}
var EM = 365;
function pw(e, t) {
    var n = t.moveBy
      , r = t.direction
      , o = t.context
      , s = t.modifiers
      , i = t.retry
      , l = i === void 0 ? {
        count: 0,
        lastFocused: e
    } : i
      , c = o.weekStartsOn
      , u = o.fromDate
      , d = o.toDate
      , f = o.locale
      , g = {
        day: tt,
        week: fd,
        month: nn,
        year: p4,
        startOfWeek: function(w) {
            return o.ISOWeek ? ro(w) : wn(w, {
                locale: f,
                weekStartsOn: c
            })
        },
        endOfWeek: function(w) {
            return o.ISOWeek ? tw(w) : Hf(w, {
                locale: f,
                weekStartsOn: c
            })
        }
    }
      , h = g[n](e, r === "after" ? 1 : -1);
    r === "before" && u ? h = v4([u, h]) : r === "after" && d && (h = g4([d, h]));
    var b = !0;
    if (s) {
        var v = Gf(h, s);
        b = !v.disabled && !v.hidden
    }
    return b ? h : l.count > EM ? l.lastFocused : pw(h, {
        moveBy: n,
        direction: r,
        context: o,
        modifiers: s,
        retry: K(K({}, l), {
            count: l.count + 1
        })
    })
}
var vw = m.createContext(void 0);
function PM(e) {
    var t = Fa()
      , n = hw()
      , r = m.useState()
      , o = r[0]
      , s = r[1]
      , i = m.useState()
      , l = i[0]
      , c = i[1]
      , u = kM(t.displayMonths, n)
      , d = o ?? (l && t.isDateDisplayed(l)) ? l : u
      , f = function() {
        c(o),
        s(void 0)
    }
      , g = function(w) {
        s(w)
    }
      , h = ye()
      , b = function(w, y) {
        if (o) {
            var p = pw(o, {
                moveBy: w,
                direction: y,
                context: h,
                modifiers: n
            });
            ut(o, p) || (t.goToDate(p, o),
            g(p))
        }
    }
      , v = {
        focusedDay: o,
        focusTarget: d,
        blur: f,
        focus: g,
        focusDayAfter: function() {
            return b("day", "after")
        },
        focusDayBefore: function() {
            return b("day", "before")
        },
        focusWeekAfter: function() {
            return b("week", "after")
        },
        focusWeekBefore: function() {
            return b("week", "before")
        },
        focusMonthBefore: function() {
            return b("month", "before")
        },
        focusMonthAfter: function() {
            return b("month", "after")
        },
        focusYearBefore: function() {
            return b("year", "before")
        },
        focusYearAfter: function() {
            return b("year", "after")
        },
        focusStartOfWeek: function() {
            return b("startOfWeek", "before")
        },
        focusEndOfWeek: function() {
            return b("endOfWeek", "after")
        }
    };
    return a.jsx(vw.Provider, {
        value: v,
        children: e.children
    })
}
function qf() {
    var e = m.useContext(vw);
    if (!e)
        throw new Error("useFocusContext must be used within a FocusProvider");
    return e
}
function TM(e, t) {
    var n = hw()
      , r = Gf(e, n, t);
    return r
}
var Xf = m.createContext(void 0);
function MM(e) {
    if (!Gl(e.initialProps)) {
        var t = {
            selected: void 0
        };
        return a.jsx(Xf.Provider, {
            value: t,
            children: e.children
        })
    }
    return a.jsx(RM, {
        initialProps: e.initialProps,
        children: e.children
    })
}
function RM(e) {
    var t = e.initialProps
      , n = e.children
      , r = function(s, i, l) {
        var c, u, d;
        if ((c = t.onDayClick) === null || c === void 0 || c.call(t, s, i, l),
        i.selected && !t.required) {
            (u = t.onSelect) === null || u === void 0 || u.call(t, void 0, s, i, l);
            return
        }
        (d = t.onSelect) === null || d === void 0 || d.call(t, s, s, i, l)
    }
      , o = {
        selected: t.selected,
        onDayClick: r
    };
    return a.jsx(Xf.Provider, {
        value: o,
        children: n
    })
}
function gw() {
    var e = m.useContext(Xf);
    if (!e)
        throw new Error("useSelectSingle must be used within a SelectSingleProvider");
    return e
}
function _M(e, t) {
    var n = ye()
      , r = gw()
      , o = Yf()
      , s = Qf()
      , i = qf()
      , l = i.focusDayAfter
      , c = i.focusDayBefore
      , u = i.focusWeekAfter
      , d = i.focusWeekBefore
      , f = i.blur
      , g = i.focus
      , h = i.focusMonthBefore
      , b = i.focusMonthAfter
      , v = i.focusYearBefore
      , w = i.focusYearAfter
      , y = i.focusStartOfWeek
      , p = i.focusEndOfWeek
      , x = function(M) {
        var j, E, L, U;
        Gl(n) ? (j = r.onDayClick) === null || j === void 0 || j.call(r, e, t, M) : Ia(n) ? (E = o.onDayClick) === null || E === void 0 || E.call(o, e, t, M) : La(n) ? (L = s.onDayClick) === null || L === void 0 || L.call(s, e, t, M) : (U = n.onDayClick) === null || U === void 0 || U.call(n, e, t, M)
    }
      , N = function(M) {
        var j;
        g(e),
        (j = n.onDayFocus) === null || j === void 0 || j.call(n, e, t, M)
    }
      , S = function(M) {
        var j;
        f(),
        (j = n.onDayBlur) === null || j === void 0 || j.call(n, e, t, M)
    }
      , k = function(M) {
        var j;
        (j = n.onDayMouseEnter) === null || j === void 0 || j.call(n, e, t, M)
    }
      , C = function(M) {
        var j;
        (j = n.onDayMouseLeave) === null || j === void 0 || j.call(n, e, t, M)
    }
      , T = function(M) {
        var j;
        (j = n.onDayPointerEnter) === null || j === void 0 || j.call(n, e, t, M)
    }
      , D = function(M) {
        var j;
        (j = n.onDayPointerLeave) === null || j === void 0 || j.call(n, e, t, M)
    }
      , R = function(M) {
        var j;
        (j = n.onDayTouchCancel) === null || j === void 0 || j.call(n, e, t, M)
    }
      , F = function(M) {
        var j;
        (j = n.onDayTouchEnd) === null || j === void 0 || j.call(n, e, t, M)
    }
      , A = function(M) {
        var j;
        (j = n.onDayTouchMove) === null || j === void 0 || j.call(n, e, t, M)
    }
      , W = function(M) {
        var j;
        (j = n.onDayTouchStart) === null || j === void 0 || j.call(n, e, t, M)
    }
      , O = function(M) {
        var j;
        (j = n.onDayKeyUp) === null || j === void 0 || j.call(n, e, t, M)
    }
      , V = function(M) {
        var j;
        switch (M.key) {
        case "ArrowLeft":
            M.preventDefault(),
            M.stopPropagation(),
            n.dir === "rtl" ? l() : c();
            break;
        case "ArrowRight":
            M.preventDefault(),
            M.stopPropagation(),
            n.dir === "rtl" ? c() : l();
            break;
        case "ArrowDown":
            M.preventDefault(),
            M.stopPropagation(),
            u();
            break;
        case "ArrowUp":
            M.preventDefault(),
            M.stopPropagation(),
            d();
            break;
        case "PageUp":
            M.preventDefault(),
            M.stopPropagation(),
            M.shiftKey ? v() : h();
            break;
        case "PageDown":
            M.preventDefault(),
            M.stopPropagation(),
            M.shiftKey ? w() : b();
            break;
        case "Home":
            M.preventDefault(),
            M.stopPropagation(),
            y();
            break;
        case "End":
            M.preventDefault(),
            M.stopPropagation(),
            p();
            break
        }
        (j = n.onDayKeyDown) === null || j === void 0 || j.call(n, e, t, M)
    }
      , $ = {
        onClick: x,
        onFocus: N,
        onBlur: S,
        onKeyDown: V,
        onKeyUp: O,
        onMouseEnter: k,
        onMouseLeave: C,
        onPointerEnter: T,
        onPointerLeave: D,
        onTouchCancel: R,
        onTouchEnd: F,
        onTouchMove: A,
        onTouchStart: W
    };
    return $
}
function DM() {
    var e = ye()
      , t = gw()
      , n = Yf()
      , r = Qf()
      , o = Gl(e) ? t.selected : Ia(e) ? n.selected : La(e) ? r.selected : void 0;
    return o
}
function OM(e) {
    return Object.values(rn).includes(e)
}
function AM(e, t) {
    var n = [e.classNames.day];
    return Object.keys(t).forEach(function(r) {
        var o = e.modifiersClassNames[r];
        if (o)
            n.push(o);
        else if (OM(r)) {
            var s = e.classNames["day_".concat(r)];
            s && n.push(s)
        }
    }),
    n
}
function IM(e, t) {
    var n = K({}, e.styles.day);
    return Object.keys(t).forEach(function(r) {
        var o;
        n = K(K({}, n), (o = e.modifiersStyles) === null || o === void 0 ? void 0 : o[r])
    }),
    n
}
function LM(e, t, n) {
    var r, o, s, i = ye(), l = qf(), c = TM(e, t), u = _M(e, c), d = DM(), f = !!(i.onDayClick || i.mode !== "default");
    m.useEffect(function() {
        var k;
        c.outside || l.focusedDay && f && ut(l.focusedDay, e) && ((k = n.current) === null || k === void 0 || k.focus())
    }, [l.focusedDay, e, n, f, c.outside]);
    var g = AM(i, c).join(" ")
      , h = IM(i, c)
      , b = !!(c.outside && !i.showOutsideDays || c.hidden)
      , v = (s = (o = i.components) === null || o === void 0 ? void 0 : o.DayContent) !== null && s !== void 0 ? s : oM
      , w = a.jsx(v, {
        date: e,
        displayMonth: t,
        activeModifiers: c
    })
      , y = {
        style: h,
        className: g,
        children: w,
        role: "gridcell"
    }
      , p = l.focusTarget && ut(l.focusTarget, e) && !c.outside
      , x = l.focusedDay && ut(l.focusedDay, e)
      , N = K(K(K({}, y), (r = {
        disabled: c.disabled,
        role: "gridcell"
    },
    r["aria-selected"] = c.selected,
    r.tabIndex = x || p ? 0 : -1,
    r)), u)
      , S = {
        isButton: f,
        isHidden: b,
        activeModifiers: c,
        selectedDays: d,
        buttonProps: N,
        divProps: y
    };
    return S
}
function FM(e) {
    var t = m.useRef(null)
      , n = LM(e.date, e.displayMonth, t);
    return n.isHidden ? a.jsx("div", {
        role: "gridcell"
    }) : n.isButton ? a.jsx(hl, K({
        name: "day",
        ref: t
    }, n.buttonProps)) : a.jsx("div", K({}, n.divProps))
}
function zM(e) {
    var t = e.number
      , n = e.dates
      , r = ye()
      , o = r.onWeekNumberClick
      , s = r.styles
      , i = r.classNames
      , l = r.locale
      , c = r.labels.labelWeekNumber
      , u = r.formatters.formatWeekNumber
      , d = u(Number(t), {
        locale: l
    });
    if (!o)
        return a.jsx("span", {
            className: i.weeknumber,
            style: s.weeknumber,
            children: d
        });
    var f = c(Number(t), {
        locale: l
    })
      , g = function(h) {
        o(t, n, h)
    };
    return a.jsx(hl, {
        name: "week-number",
        "aria-label": f,
        className: i.weeknumber,
        style: s.weeknumber,
        onClick: g,
        children: d
    })
}
function $M(e) {
    var t, n, r = ye(), o = r.styles, s = r.classNames, i = r.showWeekNumber, l = r.components, c = (t = l == null ? void 0 : l.Day) !== null && t !== void 0 ? t : FM, u = (n = l == null ? void 0 : l.WeekNumber) !== null && n !== void 0 ? n : zM, d;
    return i && (d = a.jsx("td", {
        className: s.cell,
        style: o.cell,
        children: a.jsx(u, {
            number: e.weekNumber,
            dates: e.dates
        })
    })),
    a.jsxs("tr", {
        className: s.row,
        style: o.row,
        children: [d, e.dates.map(function(f) {
            return a.jsx("td", {
                className: s.cell,
                style: o.cell,
                role: "presentation",
                children: a.jsx(c, {
                    displayMonth: e.displayMonth,
                    date: f
                })
            }, vT(f))
        })]
    })
}
function gp(e, t, n) {
    for (var r = n != null && n.ISOWeek ? tw(t) : Hf(t, n), o = n != null && n.ISOWeek ? ro(e) : wn(e, n), s = hn(r, o), i = [], l = 0; l <= s; l++)
        i.push(tt(o, l));
    var c = i.reduce(function(u, d) {
        var f = n != null && n.ISOWeek ? rw(d) : sw(d, n)
          , g = u.find(function(h) {
            return h.weekNumber === f
        });
        return g ? (g.dates.push(d),
        u) : (u.push({
            weekNumber: f,
            dates: [d]
        }),
        u)
    }, []);
    return c
}
function BM(e, t) {
    var n = gp(ht(e), Wf(e), t);
    if (t != null && t.useFixedWeeks) {
        var r = yT(e, t);
        if (r < 6) {
            var o = n[n.length - 1]
              , s = o.dates[o.dates.length - 1]
              , i = fd(s, 6 - r)
              , l = gp(fd(s, 1), i, t);
            n.push.apply(n, l)
        }
    }
    return n
}
function WM(e) {
    var t, n, r, o = ye(), s = o.locale, i = o.classNames, l = o.styles, c = o.hideHead, u = o.fixedWeeks, d = o.components, f = o.weekStartsOn, g = o.firstWeekContainsDate, h = o.ISOWeek, b = BM(e.displayMonth, {
        useFixedWeeks: !!u,
        ISOWeek: h,
        locale: s,
        weekStartsOn: f,
        firstWeekContainsDate: g
    }), v = (t = d == null ? void 0 : d.Head) !== null && t !== void 0 ? t : rM, w = (n = d == null ? void 0 : d.Row) !== null && n !== void 0 ? n : $M, y = (r = d == null ? void 0 : d.Footer) !== null && r !== void 0 ? r : eM;
    return a.jsxs("table", {
        id: e.id,
        className: i.table,
        style: l.table,
        role: "grid",
        "aria-labelledby": e["aria-labelledby"],
        children: [!c && a.jsx(v, {}), a.jsx("tbody", {
            className: i.tbody,
            style: l.tbody,
            children: b.map(function(p) {
                return a.jsx(w, {
                    displayMonth: e.displayMonth,
                    dates: p.dates,
                    weekNumber: p.weekNumber
                }, p.weekNumber)
            })
        }), a.jsx(y, {
            displayMonth: e.displayMonth
        })]
    })
}
function HM() {
    return !!(typeof window < "u" && window.document && window.document.createElement)
}
var VM = HM() ? m.useLayoutEffect : m.useEffect
  , Kc = !1
  , UM = 0;
function yp() {
    return "react-day-picker-".concat(++UM)
}
function YM(e) {
    var t, n = e ?? (Kc ? yp() : null), r = m.useState(n), o = r[0], s = r[1];
    return VM(function() {
        o === null && s(yp())
    }, []),
    m.useEffect(function() {
        Kc === !1 && (Kc = !0)
    }, []),
    (t = e ?? o) !== null && t !== void 0 ? t : void 0
}
function KM(e) {
    var t, n, r = ye(), o = r.dir, s = r.classNames, i = r.styles, l = r.components, c = Fa().displayMonths, u = YM(r.id ? "".concat(r.id, "-").concat(e.displayIndex) : void 0), d = r.id ? "".concat(r.id, "-grid-").concat(e.displayIndex) : void 0, f = [s.month], g = i.month, h = e.displayIndex === 0, b = e.displayIndex === c.length - 1, v = !h && !b;
    o === "rtl" && (t = [h, b],
    b = t[0],
    h = t[1]),
    h && (f.push(s.caption_start),
    g = K(K({}, g), i.caption_start)),
    b && (f.push(s.caption_end),
    g = K(K({}, g), i.caption_end)),
    v && (f.push(s.caption_between),
    g = K(K({}, g), i.caption_between));
    var w = (n = l == null ? void 0 : l.Caption) !== null && n !== void 0 ? n : ZT;
    return a.jsxs("div", {
        className: f.join(" "),
        style: g,
        children: [a.jsx(w, {
            id: u,
            displayMonth: e.displayMonth,
            displayIndex: e.displayIndex
        }), a.jsx(WM, {
            id: d,
            "aria-labelledby": u,
            displayMonth: e.displayMonth
        })]
    }, e.displayIndex)
}
function QM(e) {
    var t = ye()
      , n = t.classNames
      , r = t.styles;
    return a.jsx("div", {
        className: n.months,
        style: r.months,
        children: e.children
    })
}
function GM(e) {
    var t, n, r = e.initialProps, o = ye(), s = qf(), i = Fa(), l = m.useState(!1), c = l[0], u = l[1];
    m.useEffect(function() {
        o.initialFocus && s.focusTarget && (c || (s.focus(s.focusTarget),
        u(!0)))
    }, [o.initialFocus, c, s.focus, s.focusTarget, s]);
    var d = [o.classNames.root, o.className];
    o.numberOfMonths > 1 && d.push(o.classNames.multiple_months),
    o.showWeekNumber && d.push(o.classNames.with_weeknumber);
    var f = K(K({}, o.styles.root), o.style)
      , g = Object.keys(r).filter(function(b) {
        return b.startsWith("data-")
    }).reduce(function(b, v) {
        var w;
        return K(K({}, b), (w = {},
        w[v] = r[v],
        w))
    }, {})
      , h = (n = (t = r.components) === null || t === void 0 ? void 0 : t.Months) !== null && n !== void 0 ? n : QM;
    return a.jsx("div", K({
        className: d.join(" "),
        style: f,
        dir: o.dir,
        id: o.id,
        nonce: r.nonce,
        title: r.title,
        lang: r.lang
    }, g, {
        children: a.jsx(h, {
            children: i.displayMonths.map(function(b, v) {
                return a.jsx(KM, {
                    displayIndex: v,
                    displayMonth: b
                }, v)
            })
        })
    }))
}
function qM(e) {
    var t = e.children
      , n = wT(e, ["children"]);
    return a.jsx(zT, {
        initialProps: n,
        children: a.jsx(GT, {
            children: a.jsx(MM, {
                initialProps: n,
                children: a.jsx(sM, {
                    initialProps: n,
                    children: a.jsx(lM, {
                        initialProps: n,
                        children: a.jsx(vM, {
                            children: a.jsx(PM, {
                                children: t
                            })
                        })
                    })
                })
            })
        })
    })
}
function XM(e) {
    return a.jsx(qM, K({}, e, {
        children: a.jsx(GM, {
            initialProps: e
        })
    }))
}
function yw({className: e, classNames: t, showOutsideDays: n=!0, ...r}) {
    return a.jsx(XM, {
        showOutsideDays: n,
        className: re("p-3", e),
        classNames: {
            months: "flex flex-col sm:flex-row space-y-4 sm:space-x-4 sm:space-y-0",
            month: "space-y-4",
            caption: "flex justify-center pt-1 relative items-center",
            caption_label: "text-sm font-medium",
            nav: "space-x-1 flex items-center",
            nav_button: re(sd({
                variant: "outline"
            }), "h-7 w-7 bg-transparent p-0 opacity-50 hover:opacity-100"),
            nav_button_previous: "absolute left-1",
            nav_button_next: "absolute right-1",
            table: "w-full border-collapse space-y-1",
            head_row: "flex",
            head_cell: "text-muted-foreground rounded-md w-9 font-normal text-[0.8rem]",
            row: "flex w-full mt-2",
            cell: "h-9 w-9 text-center text-sm p-0 relative [&:has([aria-selected].day-range-end)]:rounded-r-md [&:has([aria-selected].day-outside)]:bg-accent/50 [&:has([aria-selected])]:bg-accent first:[&:has([aria-selected])]:rounded-l-md last:[&:has([aria-selected])]:rounded-r-md focus-within:relative focus-within:z-20",
            day: re(sd({
                variant: "ghost"
            }), "h-9 w-9 p-0 font-normal aria-selected:opacity-100"),
            day_range_end: "day-range-end",
            day_selected: "bg-primary text-primary-foreground hover:bg-primary hover:text-primary-foreground focus:bg-primary focus:text-primary-foreground",
            day_today: "bg-accent text-accent-foreground",
            day_outside: "day-outside text-muted-foreground opacity-50 aria-selected:bg-accent/50 aria-selected:text-muted-foreground aria-selected:opacity-30",
            day_disabled: "text-muted-foreground opacity-50",
            day_range_middle: "aria-selected:bg-accent aria-selected:text-accent-foreground",
            day_hidden: "invisible",
            ...t
        },
        components: {
            IconLeft: ({...o}) => a.jsx(bS, {
                className: "h-4 w-4"
            }),
            IconRight: ({...o}) => a.jsx(NS, {
                className: "h-4 w-4"
            })
        },
        ...r
    })
}
yw.displayName = "Calendar";
const JM = () => {
    const [e,t] = m.useState(new Date)
      , [n,r] = m.useState("")
      , o = [{
        id: "1",
        title: "Modern Family Home",
        address: "123 Oak Street, Downtown District, NY",
        price: "$750,000",
        images: [Xt, yn, _n],
        date: "2024-01-20",
        time: "2:00 PM - 4:00 PM",
        beds: 4,
        baths: 3,
        sqft: 2400,
        features: ["Updated Kitchen", "Hardwood Floors", "Large Backyard", "Garage"],
        description: "Beautiful modern family home with spacious rooms and updated finishes throughout.",
        agent: "Sarah Johnson"
    }, {
        id: "2",
        title: "Luxury Contemporary Villa",
        address: "456 Hill Road, Hillside Heights, NY",
        price: "$1,200,000",
        images: [yn, Xt, _n],
        date: "2024-01-21",
        time: "1:00 PM - 3:00 PM",
        beds: 5,
        baths: 4,
        sqft: 3200,
        features: ["Pool", "Home Theater", "Wine Cellar", "Smart Home"],
        description: "Stunning contemporary villa with premium amenities and panoramic views.",
        agent: "Michael Chen"
    }, {
        id: "3",
        title: "Elegant Victorian Estate",
        address: "789 Garden Lane, Heritage Gardens, NY",
        price: "$950,000",
        images: [_n, yn, Xt],
        date: "2024-01-22",
        time: "11:00 AM - 1:00 PM",
        beds: 4,
        baths: 3,
        sqft: 2800,
        features: ["Historic Details", "Fireplace", "Bay Windows", "Mature Gardens"],
        description: "Charming Victorian estate with period features and modern conveniences.",
        agent: "Emily Davis"
    }]
      , s = [new Date("2024-01-20"), new Date("2024-01-21"), new Date("2024-01-22"), new Date("2024-01-27"), new Date("2024-01-28")]
      , i = l => s.some(c => l.toDateString() === c.toDateString());
    return a.jsx("div", {
        className: "min-h-screen bg-surface-gradient",
        children: a.jsxs("div", {
            className: "max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12",
            children: [a.jsxs("div", {
                className: "text-center mb-12",
                children: [a.jsx("h1", {
                    className: "text-4xl md:text-5xl font-bold text-foreground mb-4",
                    children: "Open House Schedule"
                }), a.jsx("p", {
                    className: "text-xl text-muted-foreground max-w-2xl mx-auto",
                    children: "Visit our beautiful properties at your convenience. Select a date from our calendar and book your preferred open house viewing."
                })]
            }), a.jsxs("div", {
                className: "grid lg:grid-cols-2 gap-12 mb-16",
                children: [a.jsxs(Ce, {
                    className: "p-6 shadow-soft",
                    children: [a.jsx("h2", {
                        className: "text-2xl font-bold text-foreground mb-6",
                        children: "Select Your Visit Date"
                    }), a.jsx(yw, {
                        mode: "single",
                        selected: e,
                        onSelect: t,
                        disabled: l => l < new Date || !i(l),
                        className: "rounded-md border"
                    }), a.jsxs("div", {
                        className: "mt-4 space-y-2",
                        children: [a.jsxs("div", {
                            className: "flex items-center space-x-2",
                            children: [a.jsx("div", {
                                className: "w-4 h-4 bg-accent rounded-full"
                            }), a.jsx("span", {
                                className: "text-sm text-muted-foreground",
                                children: "Available dates"
                            })]
                        }), a.jsxs("div", {
                            className: "flex items-center space-x-2",
                            children: [a.jsx("div", {
                                className: "w-4 h-4 bg-muted rounded-full"
                            }), a.jsx("span", {
                                className: "text-sm text-muted-foreground",
                                children: "Unavailable dates"
                            })]
                        })]
                    })]
                }), a.jsxs(Ce, {
                    className: "p-6 shadow-soft",
                    children: [a.jsx("h2", {
                        className: "text-2xl font-bold text-foreground mb-6",
                        children: "Book Your Visit"
                    }), a.jsxs("form", {
                        className: "space-y-4",
                        children: [a.jsxs("div", {
                            className: "space-y-2",
                            children: [a.jsx(se, {
                                htmlFor: "visitorName",
                                children: "Full Name"
                            }), a.jsxs("div", {
                                className: "relative",
                                children: [a.jsx(wr, {
                                    className: "absolute left-3 top-3 h-4 w-4 text-muted-foreground"
                                }), a.jsx(Ee, {
                                    id: "visitorName",
                                    placeholder: "Enter your full name",
                                    className: "pl-10"
                                })]
                            })]
                        }), a.jsxs("div", {
                            className: "space-y-2",
                            children: [a.jsx(se, {
                                htmlFor: "visitorEmail",
                                children: "Email Address"
                            }), a.jsxs("div", {
                                className: "relative",
                                children: [a.jsx(ss, {
                                    className: "absolute left-3 top-3 h-4 w-4 text-muted-foreground"
                                }), a.jsx(Ee, {
                                    id: "visitorEmail",
                                    type: "email",
                                    placeholder: "Enter your email",
                                    className: "pl-10"
                                })]
                            })]
                        }), a.jsxs("div", {
                            className: "space-y-2",
                            children: [a.jsx(se, {
                                htmlFor: "visitorPhone",
                                children: "Phone Number"
                            }), a.jsxs("div", {
                                className: "relative",
                                children: [a.jsx(as, {
                                    className: "absolute left-3 top-3 h-4 w-4 text-muted-foreground"
                                }), a.jsx(Ee, {
                                    id: "visitorPhone",
                                    placeholder: "Enter your phone number",
                                    className: "pl-10"
                                })]
                            })]
                        }), a.jsxs("div", {
                            className: "space-y-2",
                            children: [a.jsx(se, {
                                htmlFor: "selectedProperty",
                                children: "Choose Property"
                            }), a.jsxs(Kt, {
                                value: n,
                                onValueChange: r,
                                children: [a.jsx(Mt, {
                                    children: a.jsx(Qt, {
                                        placeholder: "Select a property to visit"
                                    })
                                }), a.jsx(Rt, {
                                    children: o.map(l => a.jsxs(Y, {
                                        value: l.id,
                                        children: [l.title, " - ", l.time]
                                    }, l.id))
                                })]
                            })]
                        }), a.jsxs("div", {
                            className: "space-y-2",
                            children: [a.jsx(se, {
                                htmlFor: "visitors",
                                children: "Number of Visitors"
                            }), a.jsxs(Kt, {
                                children: [a.jsx(Mt, {
                                    children: a.jsx(Qt, {
                                        placeholder: "How many people will attend?"
                                    })
                                }), a.jsxs(Rt, {
                                    children: [a.jsx(Y, {
                                        value: "1",
                                        children: "1 person"
                                    }), a.jsx(Y, {
                                        value: "2",
                                        children: "2 people"
                                    }), a.jsx(Y, {
                                        value: "3",
                                        children: "3 people"
                                    }), a.jsx(Y, {
                                        value: "4",
                                        children: "4 people"
                                    }), a.jsx(Y, {
                                        value: "5+",
                                        children: "5+ people"
                                    })]
                                })]
                            })]
                        }), a.jsxs("div", {
                            className: "space-y-2",
                            children: [a.jsx(se, {
                                htmlFor: "specialRequests",
                                children: "Special Requests"
                            }), a.jsx(Oa, {
                                id: "specialRequests",
                                placeholder: "Any special requirements or questions about the property...",
                                className: "min-h-[80px]"
                            })]
                        }), a.jsxs(ae, {
                            className: "w-full bg-accent-gradient hover:shadow-accent text-primary font-semibold",
                            children: [a.jsx(Jr, {
                                className: "w-4 h-4 mr-2"
                            }), "Book Open House Visit"]
                        })]
                    })]
                })]
            }), a.jsxs("div", {
                children: [a.jsx("h2", {
                    className: "text-3xl font-bold text-foreground mb-8 text-center",
                    children: "Upcoming Open Houses"
                }), a.jsx("div", {
                    className: "grid gap-8",
                    children: o.map(l => a.jsx(Ce, {
                        className: "overflow-hidden shadow-medium hover:shadow-strong transition-all duration-300",
                        children: a.jsxs("div", {
                            className: "grid lg:grid-cols-2 gap-6",
                            children: [a.jsxs("div", {
                                className: "relative",
                                children: [a.jsxs("div", {
                                    className: "grid grid-cols-3 gap-2 h-64 lg:h-full",
                                    children: [a.jsx("img", {
                                        src: l.images[0],
                                        alt: l.title,
                                        className: "col-span-2 w-full h-full object-cover rounded-l-lg"
                                    }), a.jsxs("div", {
                                        className: "space-y-2",
                                        children: [a.jsx("img", {
                                            src: l.images[1],
                                            alt: l.title,
                                            className: "w-full h-1/2 object-cover rounded-tr-lg"
                                        }), a.jsx("img", {
                                            src: l.images[2],
                                            alt: l.title,
                                            className: "w-full h-1/2 object-cover"
                                        })]
                                    })]
                                }), a.jsx(rt, {
                                    className: "absolute top-4 left-4 bg-accent text-accent-foreground",
                                    children: "Open House"
                                })]
                            }), a.jsxs("div", {
                                className: "p-6 lg:p-8",
                                children: [a.jsxs("div", {
                                    className: "flex items-center justify-between mb-4",
                                    children: [a.jsx("h3", {
                                        className: "text-2xl font-bold text-foreground",
                                        children: l.title
                                    }), a.jsx("div", {
                                        className: "text-2xl font-bold text-primary",
                                        children: l.price
                                    })]
                                }), a.jsxs("div", {
                                    className: "flex items-center text-muted-foreground mb-4",
                                    children: [a.jsx(Ra, {
                                        className: "w-4 h-4 mr-2"
                                    }), a.jsx("span", {
                                        className: "text-sm",
                                        children: l.address
                                    })]
                                }), a.jsxs("div", {
                                    className: "flex items-center space-x-6 text-sm text-muted-foreground mb-4",
                                    children: [a.jsxs("div", {
                                        className: "flex items-center",
                                        children: [a.jsx(gf, {
                                            className: "w-4 h-4 mr-1"
                                        }), a.jsxs("span", {
                                            children: [l.beds, " beds"]
                                        })]
                                    }), a.jsx("div", {
                                        className: "flex items-center",
                                        children: a.jsxs("span", {
                                            children: [l.baths, " baths"]
                                        })
                                    }), a.jsx("div", {
                                        className: "flex items-center",
                                        children: a.jsxs("span", {
                                            children: [l.sqft.toLocaleString(), " sqft"]
                                        })
                                    })]
                                }), a.jsxs("div", {
                                    className: "flex items-center space-x-4 mb-4",
                                    children: [a.jsxs("div", {
                                        className: "flex items-center text-accent",
                                        children: [a.jsx(Jr, {
                                            className: "w-4 h-4 mr-2"
                                        }), a.jsx("span", {
                                            className: "font-medium",
                                            children: new Date(l.date).toLocaleDateString()
                                        })]
                                    }), a.jsxs("div", {
                                        className: "flex items-center text-accent",
                                        children: [a.jsx(os, {
                                            className: "w-4 h-4 mr-2"
                                        }), a.jsx("span", {
                                            className: "font-medium",
                                            children: l.time
                                        })]
                                    })]
                                }), a.jsx("p", {
                                    className: "text-muted-foreground mb-4 leading-relaxed",
                                    children: l.description
                                }), a.jsx("div", {
                                    className: "flex flex-wrap gap-2 mb-6",
                                    children: l.features.map( (c, u) => a.jsxs(rt, {
                                        variant: "outline",
                                        className: "border-primary/20 text-primary",
                                        children: [a.jsx(ir, {
                                            className: "w-3 h-3 mr-1"
                                        }), c]
                                    }, u))
                                }), a.jsxs("div", {
                                    className: "flex items-center justify-between",
                                    children: [a.jsxs("div", {
                                        className: "text-sm text-muted-foreground",
                                        children: [a.jsx("span", {
                                            children: "Hosted by: "
                                        }), a.jsx("span", {
                                            className: "font-medium text-foreground",
                                            children: l.agent
                                        })]
                                    }), a.jsx(ae, {
                                        className: "bg-primary hover:bg-primary-dark text-primary-foreground",
                                        onClick: () => r(l.id),
                                        children: "Book This Viewing"
                                    })]
                                })]
                            })]
                        })
                    }, l.id))
                })]
            }), a.jsxs(Ce, {
                className: "mt-16 p-8 text-center shadow-medium",
                children: [a.jsx("h3", {
                    className: "text-2xl font-bold text-foreground mb-4",
                    children: "Need Help with Your Visit?"
                }), a.jsx("p", {
                    className: "text-muted-foreground mb-6 max-w-2xl mx-auto",
                    children: "Our team is here to assist you with any questions about our open houses or to schedule a private viewing at a time that works better for you."
                }), a.jsxs("div", {
                    className: "flex flex-col sm:flex-row gap-4 justify-center",
                    children: [a.jsxs(ae, {
                        variant: "outline",
                        className: "border-primary text-primary hover:bg-primary hover:text-primary-foreground",
                        children: [a.jsx(as, {
                            className: "w-4 h-4 mr-2"
                        }), "Call Us: (555) 123-4567"]
                    }), a.jsxs(ae, {
                        variant: "outline",
                        className: "border-primary text-primary hover:bg-primary hover:text-primary-foreground",
                        children: [a.jsx(ss, {
                            className: "w-4 h-4 mr-2"
                        }), "Email: openhouse@realtypro.com"]
                    })]
                })]
            })]
        })
    })
}
;
var xw = ["PageUp", "PageDown"]
  , ww = ["ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight"]
  , bw = {
    "from-left": ["Home", "PageDown", "ArrowDown", "ArrowLeft"],
    "from-right": ["Home", "PageDown", "ArrowDown", "ArrowRight"],
    "from-bottom": ["Home", "PageDown", "ArrowDown", "ArrowLeft"],
    "from-top": ["Home", "PageDown", "ArrowUp", "ArrowLeft"]
}
  , ws = "Slider"
  , [hd,ZM,eR] = mf(ws)
  , [Nw,TR] = io(ws, [eR])
  , [tR,ql] = Nw(ws)
  , Sw = m.forwardRef( (e, t) => {
    const {name: n, min: r=0, max: o=100, step: s=1, orientation: i="horizontal", disabled: l=!1, minStepsBetweenThumbs: c=0, defaultValue: u=[r], value: d, onValueChange: f= () => {}
    , onValueCommit: g= () => {}
    , inverted: h=!1, form: b, ...v} = e
      , w = m.useRef(new Set)
      , y = m.useRef(0)
      , x = i === "horizontal" ? nR : rR
      , [N=[],S] = ma({
        prop: d,
        defaultProp: u,
        onChange: F => {
            var W;
            (W = [...w.current][y.current]) == null || W.focus(),
            f(F)
        }
    })
      , k = m.useRef(N);
    function C(F) {
        const A = lR(N, F);
        R(F, A)
    }
    function T(F) {
        R(F, y.current)
    }
    function D() {
        const F = k.current[y.current];
        N[y.current] !== F && g(N)
    }
    function R(F, A, {commit: W}={
        commit: !1
    }) {
        const O = fR(s)
          , V = mR(Math.round((F - r) / s) * s + r, O)
          , $ = ul(V, [r, o]);
        S( (M=[]) => {
            const j = aR(M, $, A);
            if (dR(j, c * s)) {
                y.current = j.indexOf($);
                const E = String(j) !== String(M);
                return E && W && g(j),
                E ? j : M
            } else
                return M
        }
        )
    }
    return a.jsx(tR, {
        scope: e.__scopeSlider,
        name: n,
        disabled: l,
        min: r,
        max: o,
        valueIndexToChangeRef: y,
        thumbs: w.current,
        values: N,
        orientation: i,
        form: b,
        children: a.jsx(hd.Provider, {
            scope: e.__scopeSlider,
            children: a.jsx(hd.Slot, {
                scope: e.__scopeSlider,
                children: a.jsx(x, {
                    "aria-disabled": l,
                    "data-disabled": l ? "" : void 0,
                    ...v,
                    ref: t,
                    onPointerDown: Q(v.onPointerDown, () => {
                        l || (k.current = N)
                    }
                    ),
                    min: r,
                    max: o,
                    inverted: h,
                    onSlideStart: l ? void 0 : C,
                    onSlideMove: l ? void 0 : T,
                    onSlideEnd: l ? void 0 : D,
                    onHomeKeyDown: () => !l && R(r, 0, {
                        commit: !0
                    }),
                    onEndKeyDown: () => !l && R(o, N.length - 1, {
                        commit: !0
                    }),
                    onStepKeyDown: ({event: F, direction: A}) => {
                        if (!l) {
                            const V = xw.includes(F.key) || F.shiftKey && ww.includes(F.key) ? 10 : 1
                              , $ = y.current
                              , M = N[$]
                              , j = s * V * A;
                            R(M + j, $, {
                                commit: !0
                            })
                        }
                    }
                })
            })
        })
    })
}
);
Sw.displayName = ws;
var [jw,Cw] = Nw(ws, {
    startEdge: "left",
    endEdge: "right",
    size: "width",
    direction: 1
})
  , nR = m.forwardRef( (e, t) => {
    const {min: n, max: r, dir: o, inverted: s, onSlideStart: i, onSlideMove: l, onSlideEnd: c, onStepKeyDown: u, ...d} = e
      , [f,g] = m.useState(null)
      , h = fe(t, x => g(x))
      , b = m.useRef(void 0)
      , v = Rx(o)
      , w = v === "ltr"
      , y = w && !s || !w && s;
    function p(x) {
        const N = b.current || f.getBoundingClientRect()
          , S = [0, N.width]
          , C = Jf(S, y ? [n, r] : [r, n]);
        return b.current = N,
        C(x - N.left)
    }
    return a.jsx(jw, {
        scope: e.__scopeSlider,
        startEdge: y ? "left" : "right",
        endEdge: y ? "right" : "left",
        direction: y ? 1 : -1,
        size: "width",
        children: a.jsx(kw, {
            dir: v,
            "data-orientation": "horizontal",
            ...d,
            ref: h,
            style: {
                ...d.style,
                "--radix-slider-thumb-transform": "translateX(-50%)"
            },
            onSlideStart: x => {
                const N = p(x.clientX);
                i == null || i(N)
            }
            ,
            onSlideMove: x => {
                const N = p(x.clientX);
                l == null || l(N)
            }
            ,
            onSlideEnd: () => {
                b.current = void 0,
                c == null || c()
            }
            ,
            onStepKeyDown: x => {
                const S = bw[y ? "from-left" : "from-right"].includes(x.key);
                u == null || u({
                    event: x,
                    direction: S ? -1 : 1
                })
            }
        })
    })
}
)
  , rR = m.forwardRef( (e, t) => {
    const {min: n, max: r, inverted: o, onSlideStart: s, onSlideMove: i, onSlideEnd: l, onStepKeyDown: c, ...u} = e
      , d = m.useRef(null)
      , f = fe(t, d)
      , g = m.useRef(void 0)
      , h = !o;
    function b(v) {
        const w = g.current || d.current.getBoundingClientRect()
          , y = [0, w.height]
          , x = Jf(y, h ? [r, n] : [n, r]);
        return g.current = w,
        x(v - w.top)
    }
    return a.jsx(jw, {
        scope: e.__scopeSlider,
        startEdge: h ? "bottom" : "top",
        endEdge: h ? "top" : "bottom",
        size: "height",
        direction: h ? 1 : -1,
        children: a.jsx(kw, {
            "data-orientation": "vertical",
            ...u,
            ref: f,
            style: {
                ...u.style,
                "--radix-slider-thumb-transform": "translateY(50%)"
            },
            onSlideStart: v => {
                const w = b(v.clientY);
                s == null || s(w)
            }
            ,
            onSlideMove: v => {
                const w = b(v.clientY);
                i == null || i(w)
            }
            ,
            onSlideEnd: () => {
                g.current = void 0,
                l == null || l()
            }
            ,
            onStepKeyDown: v => {
                const y = bw[h ? "from-bottom" : "from-top"].includes(v.key);
                c == null || c({
                    event: v,
                    direction: y ? -1 : 1
                })
            }
        })
    })
}
)
  , kw = m.forwardRef( (e, t) => {
    const {__scopeSlider: n, onSlideStart: r, onSlideMove: o, onSlideEnd: s, onHomeKeyDown: i, onEndKeyDown: l, onStepKeyDown: c, ...u} = e
      , d = ql(ws, n);
    return a.jsx(te.span, {
        ...u,
        ref: t,
        onKeyDown: Q(e.onKeyDown, f => {
            f.key === "Home" ? (i(f),
            f.preventDefault()) : f.key === "End" ? (l(f),
            f.preventDefault()) : xw.concat(ww).includes(f.key) && (c(f),
            f.preventDefault())
        }
        ),
        onPointerDown: Q(e.onPointerDown, f => {
            const g = f.target;
            g.setPointerCapture(f.pointerId),
            f.preventDefault(),
            d.thumbs.has(g) ? g.focus() : r(f)
        }
        ),
        onPointerMove: Q(e.onPointerMove, f => {
            f.target.hasPointerCapture(f.pointerId) && o(f)
        }
        ),
        onPointerUp: Q(e.onPointerUp, f => {
            const g = f.target;
            g.hasPointerCapture(f.pointerId) && (g.releasePointerCapture(f.pointerId),
            s(f))
        }
        )
    })
}
)
  , Ew = "SliderTrack"
  , Pw = m.forwardRef( (e, t) => {
    const {__scopeSlider: n, ...r} = e
      , o = ql(Ew, n);
    return a.jsx(te.span, {
        "data-disabled": o.disabled ? "" : void 0,
        "data-orientation": o.orientation,
        ...r,
        ref: t
    })
}
);
Pw.displayName = Ew;
var pd = "SliderRange"
  , Tw = m.forwardRef( (e, t) => {
    const {__scopeSlider: n, ...r} = e
      , o = ql(pd, n)
      , s = Cw(pd, n)
      , i = m.useRef(null)
      , l = fe(t, i)
      , c = o.values.length
      , u = o.values.map(g => _w(g, o.min, o.max))
      , d = c > 1 ? Math.min(...u) : 0
      , f = 100 - Math.max(...u);
    return a.jsx(te.span, {
        "data-orientation": o.orientation,
        "data-disabled": o.disabled ? "" : void 0,
        ...r,
        ref: l,
        style: {
            ...e.style,
            [s.startEdge]: d + "%",
            [s.endEdge]: f + "%"
        }
    })
}
);
Tw.displayName = pd;
var vd = "SliderThumb"
  , Mw = m.forwardRef( (e, t) => {
    const n = ZM(e.__scopeSlider)
      , [r,o] = m.useState(null)
      , s = fe(t, l => o(l))
      , i = m.useMemo( () => r ? n().findIndex(l => l.ref.current === r) : -1, [n, r]);
    return a.jsx(oR, {
        ...e,
        ref: s,
        index: i
    })
}
)
  , oR = m.forwardRef( (e, t) => {
    const {__scopeSlider: n, index: r, name: o, ...s} = e
      , i = ql(vd, n)
      , l = Cw(vd, n)
      , [c,u] = m.useState(null)
      , d = fe(t, p => u(p))
      , f = c ? i.form || !!c.closest("form") : !0
      , g = Hy(c)
      , h = i.values[r]
      , b = h === void 0 ? 0 : _w(h, i.min, i.max)
      , v = iR(r, i.values.length)
      , w = g == null ? void 0 : g[l.size]
      , y = w ? cR(w, b, l.direction) : 0;
    return m.useEffect( () => {
        if (c)
            return i.thumbs.add(c),
            () => {
                i.thumbs.delete(c)
            }
    }
    , [c, i.thumbs]),
    a.jsxs("span", {
        style: {
            transform: "var(--radix-slider-thumb-transform)",
            position: "absolute",
            [l.startEdge]: `calc(${b}% + ${y}px)`
        },
        children: [a.jsx(hd.ItemSlot, {
            scope: e.__scopeSlider,
            children: a.jsx(te.span, {
                role: "slider",
                "aria-label": e["aria-label"] || v,
                "aria-valuemin": i.min,
                "aria-valuenow": h,
                "aria-valuemax": i.max,
                "aria-orientation": i.orientation,
                "data-orientation": i.orientation,
                "data-disabled": i.disabled ? "" : void 0,
                tabIndex: i.disabled ? void 0 : 0,
                ...s,
                ref: d,
                style: h === void 0 ? {
                    display: "none"
                } : e.style,
                onFocus: Q(e.onFocus, () => {
                    i.valueIndexToChangeRef.current = r
                }
                )
            })
        }), f && a.jsx(Rw, {
            name: o ?? (i.name ? i.name + (i.values.length > 1 ? "[]" : "") : void 0),
            form: i.form,
            value: h
        }, r)]
    })
}
);
Mw.displayName = vd;
var sR = "RadioBubbleInput"
  , Rw = m.forwardRef( ({__scopeSlider: e, value: t, ...n}, r) => {
    const o = m.useRef(null)
      , s = fe(o, r)
      , i = Ox(t);
    return m.useEffect( () => {
        const l = o.current;
        if (!l)
            return;
        const c = window.HTMLInputElement.prototype
          , d = Object.getOwnPropertyDescriptor(c, "value").set;
        if (i !== t && d) {
            const f = new Event("input",{
                bubbles: !0
            });
            d.call(l, t),
            l.dispatchEvent(f)
        }
    }
    , [i, t]),
    a.jsx(te.input, {
        style: {
            display: "none"
        },
        ...n,
        ref: s,
        defaultValue: t
    })
}
);
Rw.displayName = sR;
function aR(e=[], t, n) {
    const r = [...e];
    return r[n] = t,
    r.sort( (o, s) => o - s)
}
function _w(e, t, n) {
    const s = 100 / (n - t) * (e - t);
    return ul(s, [0, 100])
}
function iR(e, t) {
    return t > 2 ? `Value ${e + 1} of ${t}` : t === 2 ? ["Minimum", "Maximum"][e] : void 0
}
function lR(e, t) {
    if (e.length === 1)
        return 0;
    const n = e.map(o => Math.abs(o - t))
      , r = Math.min(...n);
    return n.indexOf(r)
}
function cR(e, t, n) {
    const r = e / 2
      , s = Jf([0, 50], [0, r]);
    return (r - s(t) * n) * n
}
function uR(e) {
    return e.slice(0, -1).map( (t, n) => e[n + 1] - t)
}
function dR(e, t) {
    if (t > 0) {
        const n = uR(e);
        return Math.min(...n) >= t
    }
    return !0
}
function Jf(e, t) {
    return n => {
        if (e[0] === e[1] || t[0] === t[1])
            return t[0];
        const r = (t[1] - t[0]) / (e[1] - e[0]);
        return t[0] + r * (n - e[0])
    }
}
function fR(e) {
    return (String(e).split(".")[1] || "").length
}
function mR(e, t) {
    const n = Math.pow(10, t);
    return Math.round(e * n) / n
}
var Dw = Sw
  , hR = Pw
  , pR = Tw
  , vR = Mw;
const Ri = m.forwardRef( ({className: e, ...t}, n) => a.jsxs(Dw, {
    ref: n,
    className: re("relative flex w-full touch-none select-none items-center", e),
    ...t,
    children: [a.jsx(hR, {
        className: "relative h-2 w-full grow overflow-hidden rounded-full bg-secondary",
        children: a.jsx(pR, {
            className: "absolute h-full bg-primary"
        })
    }), a.jsx(vR, {
        className: "block h-5 w-5 rounded-full border-2 border-primary bg-background ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50"
    })]
}));
Ri.displayName = Dw.displayName;
const gR = () => {
    const [e,t] = m.useState([5e5])
      , [n,r] = m.useState([1e5])
      , [o,s] = m.useState([30])
      , [i,l] = m.useState([6.5])
      , c = e[0] - n[0]
      , u = i[0] / 100 / 12
      , d = o[0] * 12
      , f = c * (u * Math.pow(1 + u, d)) / (Math.pow(1 + u, d) - 1)
      , h = f * d - c
      , b = e[0] * .0125 / 12
      , v = e[0] * .005 / 12
      , w = c > e[0] * .8 ? c * .005 / 12 : 0
      , y = f + b + v + w;
    return a.jsx("div", {
        className: "min-h-screen bg-surface-gradient",
        children: a.jsxs("div", {
            className: "max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12",
            children: [a.jsxs("div", {
                className: "text-center mb-12",
                children: [a.jsx("h1", {
                    className: "text-4xl md:text-5xl font-bold text-foreground mb-4",
                    children: "Mortgage Calculator"
                }), a.jsx("p", {
                    className: "text-xl text-muted-foreground max-w-2xl mx-auto",
                    children: "Calculate your monthly mortgage payments and get personalized financing options from our expert team."
                })]
            }), a.jsxs("div", {
                className: "grid xl:grid-cols-3 gap-8",
                children: [a.jsxs("div", {
                    className: "xl:col-span-2 space-y-6",
                    children: [a.jsxs(Ce, {
                        className: "p-6 shadow-soft",
                        children: [a.jsxs("h2", {
                            className: "text-2xl font-bold text-foreground mb-6 flex items-center",
                            children: [a.jsx(Uu, {
                                className: "w-6 h-6 mr-2 text-accent"
                            }), "Loan Details"]
                        }), a.jsxs("div", {
                            className: "grid md:grid-cols-2 gap-6",
                            children: [a.jsxs("div", {
                                className: "space-y-4",
                                children: [a.jsxs("div", {
                                    children: [a.jsx(se, {
                                        className: "text-base font-medium",
                                        children: "Home Price"
                                    }), a.jsxs("div", {
                                        className: "mt-2",
                                        children: [a.jsx(Ee, {
                                            type: "number",
                                            value: e[0],
                                            onChange: p => t([parseInt(p.target.value) || 0]),
                                            className: "text-lg"
                                        }), a.jsx(Ri, {
                                            value: e,
                                            onValueChange: t,
                                            max: 2e6,
                                            min: 1e5,
                                            step: 1e4,
                                            className: "mt-3"
                                        }), a.jsxs("div", {
                                            className: "flex justify-between text-sm text-muted-foreground mt-1",
                                            children: [a.jsx("span", {
                                                children: "$100K"
                                            }), a.jsx("span", {
                                                children: "$2M"
                                            })]
                                        })]
                                    })]
                                }), a.jsxs("div", {
                                    children: [a.jsx(se, {
                                        className: "text-base font-medium",
                                        children: "Down Payment"
                                    }), a.jsxs("div", {
                                        className: "mt-2",
                                        children: [a.jsx(Ee, {
                                            type: "number",
                                            value: n[0],
                                            onChange: p => r([parseInt(p.target.value) || 0]),
                                            className: "text-lg"
                                        }), a.jsx(Ri, {
                                            value: n,
                                            onValueChange: r,
                                            max: e[0] * .5,
                                            min: e[0] * .05,
                                            step: 5e3,
                                            className: "mt-3"
                                        }), a.jsxs("div", {
                                            className: "flex justify-between text-sm text-muted-foreground mt-1",
                                            children: [a.jsxs("span", {
                                                children: [Math.round(n[0] / e[0] * 100), "% of home price"]
                                            }), a.jsxs("span", {
                                                children: ["$", n[0].toLocaleString()]
                                            })]
                                        })]
                                    })]
                                })]
                            }), a.jsxs("div", {
                                className: "space-y-4",
                                children: [a.jsxs("div", {
                                    children: [a.jsx(se, {
                                        className: "text-base font-medium",
                                        children: "Loan Term (Years)"
                                    }), a.jsx("div", {
                                        className: "mt-2",
                                        children: a.jsxs(Kt, {
                                            value: o[0].toString(),
                                            onValueChange: p => s([parseInt(p)]),
                                            children: [a.jsx(Mt, {
                                                className: "text-lg",
                                                children: a.jsx(Qt, {})
                                            }), a.jsxs(Rt, {
                                                children: [a.jsx(Y, {
                                                    value: "15",
                                                    children: "15 years"
                                                }), a.jsx(Y, {
                                                    value: "20",
                                                    children: "20 years"
                                                }), a.jsx(Y, {
                                                    value: "25",
                                                    children: "25 years"
                                                }), a.jsx(Y, {
                                                    value: "30",
                                                    children: "30 years"
                                                })]
                                            })]
                                        })
                                    })]
                                }), a.jsxs("div", {
                                    children: [a.jsx(se, {
                                        className: "text-base font-medium",
                                        children: "Interest Rate (%)"
                                    }), a.jsxs("div", {
                                        className: "mt-2",
                                        children: [a.jsx(Ee, {
                                            type: "number",
                                            step: "0.1",
                                            value: i[0],
                                            onChange: p => l([parseFloat(p.target.value) || 0]),
                                            className: "text-lg"
                                        }), a.jsx(Ri, {
                                            value: i,
                                            onValueChange: l,
                                            max: 12,
                                            min: 3,
                                            step: .1,
                                            className: "mt-3"
                                        }), a.jsxs("div", {
                                            className: "flex justify-between text-sm text-muted-foreground mt-1",
                                            children: [a.jsx("span", {
                                                children: "3%"
                                            }), a.jsx("span", {
                                                children: "12%"
                                            })]
                                        })]
                                    })]
                                })]
                            })]
                        })]
                    }), a.jsxs(Ce, {
                        className: "p-6 shadow-medium",
                        children: [a.jsx("h3", {
                            className: "text-2xl font-bold text-foreground mb-6",
                            children: "Your Monthly Payment Breakdown"
                        }), a.jsxs("div", {
                            className: "grid md:grid-cols-2 gap-6",
                            children: [a.jsxs("div", {
                                className: "space-y-4",
                                children: [a.jsxs("div", {
                                    className: "flex justify-between items-center p-4 bg-accent/5 rounded-lg",
                                    children: [a.jsx("span", {
                                        className: "text-muted-foreground",
                                        children: "Principal & Interest"
                                    }), a.jsxs("span", {
                                        className: "text-lg font-semibold text-foreground",
                                        children: ["$", isNaN(f) ? "0" : Math.round(f).toLocaleString()]
                                    })]
                                }), a.jsxs("div", {
                                    className: "flex justify-between items-center p-4 bg-secondary/50 rounded-lg",
                                    children: [a.jsx("span", {
                                        className: "text-muted-foreground",
                                        children: "Property Tax (est.)"
                                    }), a.jsxs("span", {
                                        className: "text-lg font-semibold text-foreground",
                                        children: ["$", Math.round(b).toLocaleString()]
                                    })]
                                }), a.jsxs("div", {
                                    className: "flex justify-between items-center p-4 bg-secondary/50 rounded-lg",
                                    children: [a.jsx("span", {
                                        className: "text-muted-foreground",
                                        children: "Home Insurance (est.)"
                                    }), a.jsxs("span", {
                                        className: "text-lg font-semibold text-foreground",
                                        children: ["$", Math.round(v).toLocaleString()]
                                    })]
                                }), w > 0 && a.jsxs("div", {
                                    className: "flex justify-between items-center p-4 bg-secondary/50 rounded-lg",
                                    children: [a.jsx("span", {
                                        className: "text-muted-foreground",
                                        children: "PMI (est.)"
                                    }), a.jsxs("span", {
                                        className: "text-lg font-semibold text-foreground",
                                        children: ["$", Math.round(w).toLocaleString()]
                                    })]
                                })]
                            }), a.jsxs("div", {
                                className: "space-y-6",
                                children: [a.jsxs("div", {
                                    className: "text-center p-6 bg-primary text-primary-foreground rounded-xl",
                                    children: [a.jsx("div", {
                                        className: "text-sm opacity-80 mb-2",
                                        children: "Total Monthly Payment"
                                    }), a.jsxs("div", {
                                        className: "text-3xl font-bold",
                                        children: ["$", isNaN(y) ? "0" : Math.round(y).toLocaleString()]
                                    })]
                                }), a.jsxs("div", {
                                    className: "grid grid-cols-2 gap-4 text-center",
                                    children: [a.jsxs("div", {
                                        className: "p-4 bg-accent/10 rounded-lg",
                                        children: [a.jsx("div", {
                                            className: "text-sm text-muted-foreground mb-1",
                                            children: "Total Interest"
                                        }), a.jsxs("div", {
                                            className: "text-lg font-semibold text-foreground",
                                            children: ["$", isNaN(h) ? "0" : Math.round(h).toLocaleString()]
                                        })]
                                    }), a.jsxs("div", {
                                        className: "p-4 bg-accent/10 rounded-lg",
                                        children: [a.jsx("div", {
                                            className: "text-sm text-muted-foreground mb-1",
                                            children: "Loan Amount"
                                        }), a.jsxs("div", {
                                            className: "text-lg font-semibold text-foreground",
                                            children: ["$", c.toLocaleString()]
                                        })]
                                    })]
                                })]
                            })]
                        })]
                    })]
                }), a.jsxs("div", {
                    className: "space-y-6",
                    children: [a.jsxs(Ce, {
                        className: "p-6 shadow-soft",
                        children: [a.jsx("h3", {
                            className: "text-xl font-bold text-foreground mb-4",
                            children: "Get Personalized Rates"
                        }), a.jsx("p", {
                            className: "text-muted-foreground text-sm mb-6",
                            children: "Connect with our mortgage specialists to get personalized rate quotes and expert guidance."
                        }), a.jsxs("form", {
                            className: "space-y-4",
                            children: [a.jsxs("div", {
                                className: "space-y-2",
                                children: [a.jsx(se, {
                                    htmlFor: "calcName",
                                    children: "Full Name"
                                }), a.jsxs("div", {
                                    className: "relative",
                                    children: [a.jsx(wr, {
                                        className: "absolute left-3 top-3 h-4 w-4 text-muted-foreground"
                                    }), a.jsx(Ee, {
                                        id: "calcName",
                                        placeholder: "Enter your name",
                                        className: "pl-10"
                                    })]
                                })]
                            }), a.jsxs("div", {
                                className: "space-y-2",
                                children: [a.jsx(se, {
                                    htmlFor: "calcEmail",
                                    children: "Email"
                                }), a.jsxs("div", {
                                    className: "relative",
                                    children: [a.jsx(ss, {
                                        className: "absolute left-3 top-3 h-4 w-4 text-muted-foreground"
                                    }), a.jsx(Ee, {
                                        id: "calcEmail",
                                        type: "email",
                                        placeholder: "Enter your email",
                                        className: "pl-10"
                                    })]
                                })]
                            }), a.jsxs("div", {
                                className: "space-y-2",
                                children: [a.jsx(se, {
                                    htmlFor: "calcPhone",
                                    children: "Phone"
                                }), a.jsxs("div", {
                                    className: "relative",
                                    children: [a.jsx(as, {
                                        className: "absolute left-3 top-3 h-4 w-4 text-muted-foreground"
                                    }), a.jsx(Ee, {
                                        id: "calcPhone",
                                        placeholder: "Enter your phone",
                                        className: "pl-10"
                                    })]
                                })]
                            }), a.jsxs("div", {
                                className: "space-y-2",
                                children: [a.jsx(se, {
                                    htmlFor: "creditScore",
                                    children: "Credit Score Range"
                                }), a.jsxs(Kt, {
                                    children: [a.jsx(Mt, {
                                        children: a.jsx(Qt, {
                                            placeholder: "Select range"
                                        })
                                    }), a.jsxs(Rt, {
                                        children: [a.jsx(Y, {
                                            value: "excellent",
                                            children: "Excellent (750+)"
                                        }), a.jsx(Y, {
                                            value: "good",
                                            children: "Good (700-749)"
                                        }), a.jsx(Y, {
                                            value: "fair",
                                            children: "Fair (650-699)"
                                        }), a.jsx(Y, {
                                            value: "poor",
                                            children: "Poor (600-649)"
                                        }), a.jsx(Y, {
                                            value: "unknown",
                                            children: "Not sure"
                                        })]
                                    })]
                                })]
                            }), a.jsxs("div", {
                                className: "space-y-2",
                                children: [a.jsx(se, {
                                    htmlFor: "buyingTimeframe",
                                    children: "Buying Timeframe"
                                }), a.jsxs(Kt, {
                                    children: [a.jsx(Mt, {
                                        children: a.jsx(Qt, {
                                            placeholder: "When are you buying?"
                                        })
                                    }), a.jsxs(Rt, {
                                        children: [a.jsx(Y, {
                                            value: "immediate",
                                            children: "Immediately"
                                        }), a.jsx(Y, {
                                            value: "1-3months",
                                            children: "1-3 months"
                                        }), a.jsx(Y, {
                                            value: "3-6months",
                                            children: "3-6 months"
                                        }), a.jsx(Y, {
                                            value: "6-12months",
                                            children: "6-12 months"
                                        }), a.jsx(Y, {
                                            value: "exploring",
                                            children: "Just exploring"
                                        })]
                                    })]
                                })]
                            }), a.jsxs("div", {
                                className: "space-y-2",
                                children: [a.jsx(se, {
                                    htmlFor: "questions",
                                    children: "Questions or Comments"
                                }), a.jsx(Oa, {
                                    id: "questions",
                                    placeholder: "Any specific questions about mortgages or the buying process?",
                                    className: "min-h-[80px]"
                                })]
                            }), a.jsx(ae, {
                                className: "w-full bg-accent-gradient hover:shadow-accent text-primary font-semibold",
                                children: "Get Personalized Quotes"
                            })]
                        })]
                    }), a.jsxs(Ce, {
                        className: "p-6 shadow-soft",
                        children: [a.jsx("h3", {
                            className: "text-xl font-bold text-foreground mb-4",
                            children: "Mortgage Tips"
                        }), a.jsxs("div", {
                            className: "space-y-4",
                            children: [a.jsxs("div", {
                                className: "flex items-start space-x-3",
                                children: [a.jsx(nl, {
                                    className: "w-5 h-5 text-accent mt-1"
                                }), a.jsxs("div", {
                                    children: [a.jsx("h4", {
                                        className: "font-medium text-foreground mb-1",
                                        children: "Improve Your Credit Score"
                                    }), a.jsx("p", {
                                        className: "text-sm text-muted-foreground",
                                        children: "A higher credit score can save you thousands in interest"
                                    })]
                                })]
                            }), a.jsxs("div", {
                                className: "flex items-start space-x-3",
                                children: [a.jsx(xy, {
                                    className: "w-5 h-5 text-accent mt-1"
                                }), a.jsxs("div", {
                                    children: [a.jsx("h4", {
                                        className: "font-medium text-foreground mb-1",
                                        children: "Save for a Larger Down Payment"
                                    }), a.jsx("p", {
                                        className: "text-sm text-muted-foreground",
                                        children: "20% down payment helps avoid PMI costs"
                                    })]
                                })]
                            }), a.jsxs("div", {
                                className: "flex items-start space-x-3",
                                children: [a.jsx(Ku, {
                                    className: "w-5 h-5 text-accent mt-1"
                                }), a.jsxs("div", {
                                    children: [a.jsx("h4", {
                                        className: "font-medium text-foreground mb-1",
                                        children: "Get Pre-Approved"
                                    }), a.jsx("p", {
                                        className: "text-sm text-muted-foreground",
                                        children: "Shows sellers you're a serious buyer"
                                    })]
                                })]
                            }), a.jsxs("div", {
                                className: "flex items-start space-x-3",
                                children: [a.jsx(Yu, {
                                    className: "w-5 h-5 text-accent mt-1"
                                }), a.jsxs("div", {
                                    children: [a.jsx("h4", {
                                        className: "font-medium text-foreground mb-1",
                                        children: "Shop Around for Rates"
                                    }), a.jsx("p", {
                                        className: "text-sm text-muted-foreground",
                                        children: "Compare offers from multiple lenders"
                                    })]
                                })]
                            })]
                        })]
                    })]
                })]
            }), a.jsxs(Ce, {
                className: "mt-12 p-8 shadow-medium",
                children: [a.jsxs("div", {
                    className: "text-center mb-8",
                    children: [a.jsx("h3", {
                        className: "text-2xl font-bold text-foreground mb-4",
                        children: "Ready to Take the Next Step?"
                    }), a.jsx("p", {
                        className: "text-muted-foreground max-w-2xl mx-auto",
                        children: "Our mortgage specialists are here to help you navigate the financing process and find the best loan options for your situation."
                    })]
                }), a.jsxs("div", {
                    className: "grid md:grid-cols-3 gap-6",
                    children: [a.jsxs("div", {
                        className: "text-center",
                        children: [a.jsx("div", {
                            className: "bg-accent/10 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4",
                            children: a.jsx(Uu, {
                                className: "w-8 h-8 text-accent"
                            })
                        }), a.jsx("h4", {
                            className: "font-semibold text-foreground mb-2",
                            children: "Free Consultation"
                        }), a.jsx("p", {
                            className: "text-sm text-muted-foreground",
                            children: "Get expert advice tailored to your financial situation"
                        })]
                    }), a.jsxs("div", {
                        className: "text-center",
                        children: [a.jsx("div", {
                            className: "bg-accent/10 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4",
                            children: a.jsx(nl, {
                                className: "w-8 h-8 text-accent"
                            })
                        }), a.jsx("h4", {
                            className: "font-semibold text-foreground mb-2",
                            children: "Competitive Rates"
                        }), a.jsx("p", {
                            className: "text-sm text-muted-foreground",
                            children: "Access to rates from multiple top-rated lenders"
                        })]
                    }), a.jsxs("div", {
                        className: "text-center",
                        children: [a.jsx("div", {
                            className: "bg-accent/10 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4",
                            children: a.jsx(Ku, {
                                className: "w-8 h-8 text-accent"
                            })
                        }), a.jsx("h4", {
                            className: "font-semibold text-foreground mb-2",
                            children: "Secure Process"
                        }), a.jsx("p", {
                            className: "text-sm text-muted-foreground",
                            children: "Your information is protected with bank-level security"
                        })]
                    })]
                })]
            })]
        })
    })
}
  , yR = () => {
    const e = ys();
    return m.useEffect( () => {
        console.error("404 Error: User attempted to access non-existent route:", e.pathname)
    }
    , [e.pathname]),
    a.jsx("div", {
        className: "flex min-h-screen items-center justify-center bg-gray-100",
        children: a.jsxs("div", {
            className: "text-center",
            children: [a.jsx("h1", {
                className: "mb-4 text-4xl font-bold",
                children: "404"
            }), a.jsx("p", {
                className: "mb-4 text-xl text-gray-600",
                children: "Oops! Page not found"
            }), a.jsx("a", {
                href: "/",
                className: "text-blue-500 underline hover:text-blue-700",
                children: "Return to Home"
            })]
        })
    })
}
  , xR = new ok
  , wR = () => a.jsx(ak, {
    client: xR,
    children: a.jsxs(OC, {
        children: [a.jsx(gj, {}), a.jsx(Gj, {}), a.jsx(oE, {
            children: a.jsxs("div", {
                className: "flex flex-col min-h-screen",
                children: [a.jsx(lE, {}), a.jsx("main", {
                    className: "flex-1",
                    children: a.jsxs(Xk, {
                        children: [a.jsx(Cn, {
                            path: "/",
                            element: a.jsx(gE, {})
                        }), a.jsx(Cn, {
                            path: "/buy-lease",
                            element: a.jsx(s4, {})
                        }), a.jsx(Cn, {
                            path: "/sell-evaluate",
                            element: a.jsx(a4, {})
                        }), a.jsx(Cn, {
                            path: "/blog",
                            element: a.jsx(i4, {})
                        }), a.jsx(Cn, {
                            path: "/blog/:slug",
                            element: a.jsx(d4, {})
                        }), a.jsx(Cn, {
                            path: "/open-house",
                            element: a.jsx(JM, {})
                        }), a.jsx(Cn, {
                            path: "/mortgage-calculator",
                            element: a.jsx(gR, {})
                        }), a.jsx(Cn, {
                            path: "*",
                            element: a.jsx(yR, {})
                        })]
                    })
                }), a.jsx(cE, {})]
            })
        })]
    })
});
Bg(document.getElementById("root")).render(a.jsx(wR, {}));
