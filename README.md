# Django-rest-framework-implementation

1) issue in return through Response
i.e. error in "return Response(serializer.data)" line
but works correctly with "return JsonResponse(serializer.data, safe=False)"

2) Not able to get the APIView form which REST_FRAMEWORK provide.
