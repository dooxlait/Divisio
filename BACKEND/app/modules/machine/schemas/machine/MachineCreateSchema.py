# BACKEND\app\modules\machine\schemas\machine\MachineCreateSchema.py

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import pre_load
from app.core.extensions import db
from app.modules.machine.models.machine import Machine


class MachineCreateSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Machine
        load_instance = True
        include_fk = True
        sqla_session = db.session

    @pre_load
    def clean_strings(self, data, **kwargs):
        """
        Nettoyage et normalisation des champs string :
        - strip() sur toutes les valeurs string
        - name : Title Case
        - type : UPPERCASE
        - manufacturer, model, serial_number : UPPERCASE
        """
        cleaned_data = dict(data)  # éviter la mutation directe

        for key, value in cleaned_data.items():
            if isinstance(value, str):
                cleaned_data[key] = value.strip()

        # Normalisations spécifiques
        if "name" in cleaned_data and isinstance(cleaned_data["name"], str):
            cleaned_data["name"] = cleaned_data["name"].title()

        if "type" in cleaned_data and isinstance(cleaned_data["type"], str):
            cleaned_data["type"] = cleaned_data["type"].upper()

        if "manufacturer" in cleaned_data and isinstance(cleaned_data["manufacturer"], str):
            cleaned_data["manufacturer"] = cleaned_data["manufacturer"].upper()

        if "model" in cleaned_data and isinstance(cleaned_data["model"], str):
            cleaned_data["model"] = cleaned_data["model"].upper()

        if "serial_number" in cleaned_data and isinstance(cleaned_data["serial_number"], str):
            cleaned_data["serial_number"] = cleaned_data["serial_number"].upper()

        return cleaned_data
