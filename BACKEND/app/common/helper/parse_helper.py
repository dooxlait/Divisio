# BACKEND\app\common\helper\parse_helper.py


def parse_filter_params(args: dict) -> dict:
    parsed = {}
    for k, v in args.items():
        # Convertit les booléens
        if v.lower() == "true":
            parsed[k] = True
        elif v.lower() == "false":
            parsed[k] = False
        else:
            parsed[k] = v  # laisse tel quel pour int, str, etc.
    return parsed