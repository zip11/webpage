    declare function GM_log(message: string, level?: GM_Types.LoggerLevel): any;

    declare namespace GM_Types {
    type LoggerLevel = "debug" | "info" | "warn" | "error";
    }


    GM_log("log message", "info", { component: "example" });