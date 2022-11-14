from rest_framework import serializers
from base.models import RencanaDiet, MakananDiet, Olahraga, Minum
from .BahanMakananSerializer import MakananDetailSerializer

class MinumSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Minum
        fields = ['id', 'jumlah_minum', 'banyak_minum', 'progress', 'rencana_diet_id']

class OlahragaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Olahraga
        fields = ['id', 'nama', 'status']

class MakananDietSerializer(serializers.ModelSerializer):
    makanan = MakananDetailSerializer(many=False, read_only=True)
    
    class Meta:
        model = MakananDiet
        fields = ['id', 'waktu_makan', 'waktu_makan', 'status', 'makanan']

class RencanaDietSerializer(serializers.ModelSerializer):
    # rencana_diet_makanan = MakananDietSerializer(many=True, read_only=True)
    # olahraga = OlahragaSerializer(many=False, read_only=True)
    # minum = MinumSerializer(many=False, read_only=True)
    
    class Meta:
        model = RencanaDiet
        fields = ['id', 'tanggal', 'user_id']
        