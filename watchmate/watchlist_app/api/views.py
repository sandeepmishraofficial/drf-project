from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer



class MovieListAV(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

class MovieDetailAV(APIView):
    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'message':'Movie not found!'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    
    def put(self, request, pk):
       movie = Movie.objects.get(pk=pk)
       serializer = MovieSerializer(movie, data=request.data)
       if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
       else:
              return Response(serializer)
    def delete(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response({'message':'Movie Deleted!'}, status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies , many = True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# @api_view(['GET','PUT','DELETE'])
# def movie_detail(request, pk):
#     if request.method == 'GET':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         try: 
#            movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'message':'Movie not found!'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response({'message':'Movie Deleted!'}, status=status.HTTP_204_NO_CONTENT)
