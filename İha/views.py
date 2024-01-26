from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import İHA
from .serializers import İHASerializer
from rest_framework import generics

# class IHAViewSet(viewsets.ModelViewSet):
#     queryset = İHA.objects.all()
#     serializer_class = İHASerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.delete()
#         return Response({'detail': 'İHA başariyla silindi'}, status=status.HTTP_204_NO_CONTENT)
    
#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
    
class IhaAddView(generics.CreateAPIView):
    queryset = İHA.objects.all()
    serializer_class = İHASerializer
    def create(self, request, *args, **kwargs):
        super().create(request,*args,**kwargs)
        return Response({'message': 'Iha created succesfully'})
    
class IhaListView(generics.ListAPIView):
    queryset = İHA.objects.all()
    serializer_class = İHASerializer

    def get_queryset(self):
        model = self.request.query_params.get('model', None)
        brand = self.request.query_params.get('brand', None)

        queryset = super().get_queryset()

        if model:
            queryset = queryset.filter(model__icontains=model)

        if brand:
            queryset = queryset.filter(brand__icontains=brand)

        return queryset
    

class IhaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = İHA.objects.all()
    serializer_class = İHASerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)

        iha_id = request.query_params.get('pk')
        image_id = request.query_params.get('imageId')
        
        if iha_id is None:
            return Response({"error": "iha id must be provided"}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            iha = İHA.objects.get(id=iha_id)
        except İHA.DoesNotExist:
            return Response({"error":"Invalid iha id" }, status=status.HTTP_404_NOT_FOUND)
        
        cleaned_data = {key: value for key, value in request.data.items() if value is not None}
        serializer = self.get_serializer(instance=iha, data=cleaned_data, partial=partial)

        if serializer.is_valid():
            if not image_id:
                serializer.validated_data["image"] = []
            serializer.save()
            return Response({"message": "İHA updated successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

