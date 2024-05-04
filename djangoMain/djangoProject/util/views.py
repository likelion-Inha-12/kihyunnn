from django.shortcuts import render

from django.http import HttpResponse


def health(request):
    return HttpResponse("seminar server ok!")

def api_response(data, message, status): # 공통 응답 형식 함수
    response = {
        "message":message,
        "data":data
    }
    return Response(response, status=status)

    