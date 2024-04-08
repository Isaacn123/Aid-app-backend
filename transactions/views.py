
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, parser_classes

from .models import Transactions
from .serializer import TransactionSerializer
from transactions import serializer

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_transactions(request):
    if request.method == "GET":
        all_transactions = Transactions.objects.all()
        if not all_transactions:
            return Response({"error":"Transactions don't exist"}, status = status.HTTP_404_NOT_FOUND)
        serializer_data = TransactionSerializer(all_transactions, many=True)
        return Response(serializer_data.data, status = status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_transactions_event(request, event_uid):
    if request.method == "GET":
        all_transactions = Transactions.objects.filter(event_uid=event_uid)
        if not all_transactions:
            return Response({"error":"Transactions don't exist"}, status = status.HTTP_404_NOT_FOUND)
        serializer_data = TransactionSerializer(all_transactions, many=True)
        return Response(serializer_data, status = status.HTTP_200_OK)



@api_view(['POST'])
@permission_classes([AllowAny])
def create_transaction(request):
    if request.method == "POST":
        serializer_data = TransactionSerializer(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data, status = status.HTTP_201_CREATED)
        else:
            return Response({"error":"Oops, we couldn't create transaction"}, status = status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([AllowAny])
def update_transaction(request, uid):
    if request.method == "PUT":
        get_transaction = Transactions.objects.filter(transaction_uid = uid).first()
        if not get_transaction:
            return Response({"error":"Transaction doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TransactionSerializer(get_transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"error":"fields are not valid"}, status=status.HTTP_400_BAD_REQUEST)


        


@api_view(['GET'])
@permission_classes([AllowAny])
def get_transaction(request, uid):
    if request.method == "GET":
        get_transaction = Transactions.objects.filter(transaction_uid = uid).first()
        serializer = TransactionSerializer(get_transaction)
        return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_transaction(request, uid):
    if request.method == "DELETE":
        get_transaction = Transactions.objects.filter(transaction_uid = uid).first()
        if not get_transaction:
            return Response({"error":"Transaction doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
        else:
            get_transaction.delete()
            return Response({"message":"deleted"}, status=status.HTTP_200_OK)


