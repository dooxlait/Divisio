# BACKEND\app\common\helper\parse_helper.py


from datetime import datetime

def parse_filter_params(args: dict) -> dict:
    parsed = {}
    date_formats = ["%Y-%m-%d", "%d/%m/%Y", "%Y-%m-%dT%H:%M:%S"]  # formats possibles

    for k, v in args.items():
        # Convertit les booléens
        if v.lower() == "true":
            parsed[k] = True
        elif v.lower() == "false":
            parsed[k] = False
        else:
            # Tente de convertir en date
            parsed_value = v
            for fmt in date_formats:
                try:
                    parsed_value = datetime.strptime(v, fmt)
                    break  # si la conversion réussit, on sort de la boucle
                except ValueError:
                    continue
            parsed[k] = parsed_value

    return parsed
