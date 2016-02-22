import pycountry
import phonenumbers

from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer

from .models import (Providers, ServiceArea)


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Providers

    def validate_currency(self, currency):
        try:
            pycountry.currencies.get(letter=currency)
            return currency
        except:
            raise serializers.ValidationError("Invalid currency")

    def validate_language(self, language):
        try:
            pycountry.languages.get(iso639_1_code=language)
            return language
        except:
            raise serializers.ValidationError("Invalid language")

    def validate_phone_no(self, phone_no):
        try:
            phonenumbers.parse(phone_no, None)
            return phone_no
        except:
            raise serializers.ValidationError("Invalid phone_no")


class ServiceAreaSerializer(DocumentSerializer):

    class Meta:
        model = ServiceArea

    def validate_provider_id(self, provider_id):
        try:
            Providers.objects.get(id=provider_id)
            return provider_id
        except Providers.DoesNotExist:
            raise serializers.ValidationError("Invalid provider_id")


class QueryParamSerializer(DocumentSerializer):

    class Meta:
        model = ServiceArea
        fields = ('polygon',)
