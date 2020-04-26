dictLogConfig = {
        "version":1,
        "handlers":{
            "HandlerYoutube":{
                "class":"logging.FileHandler",
                "formatter":"FormatterYoutube",
                "filename":"logs\Youtube.log",
                "mode":"a+",
            }
        },
        "loggers":{
            "Youtube":{
                "handlers":["HandlerYoutube"],
                "level":"INFO",
            }
        },
        "formatters":{
            "FormatterYoutube":{
                "format":"%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            }
        }
    }