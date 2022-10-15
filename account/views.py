from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.models import Expense, ExpenseType, Income, IncomeType
from account.serializers import (
    ExpenseTypeSerializaer,
    IncomeTypeSerializaer,
    SendPasswordResetEmailSerializer, 
    UserChangePasswordSerializer, 
    UserLoginSerializer, 
    UserPasswordResetSerializer, 
    UserProfileSerializer, 
    UserRegistrationSerializer, 
    GetIncomeSerializaer,
    GetExchangeSerializaer,
)
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt

# Generate Token Manually


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response({'token': token, 'msg': 'Registration Successful'}, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response({'token': token, 'msg': 'Login Success'}, status=status.HTTP_200_OK)
        else:
            return Response({'errors': {'non_field_errors': ['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)


class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(
            data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Password Changed Successfully'}, status=status.HTTP_200_OK)


class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Password Reset link send. Please check your Email'}, status=status.HTTP_200_OK)


class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, uid, token, format=None):
        serializer = UserPasswordResetSerializer(
            data=request.data, context={'uid': uid, 'token': token})
        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Password Reset Successfully'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'income_list': '/income/list',
        'income_details': '/income/details/:id/'
    }
    return JsonResponse(api_urls)

@api_view(['GET'])
def IncomeList(request):
    if(request.user.is_authenticated):
        incomes = Income.objects.all()
        serializer = GetIncomeSerializaer(incomes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response('User is not authenticated', status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def IncomeDetail(request, pk):
    if(request.user.is_authenticated):
        income = Income.objects.get(id=pk)
        serializer = GetIncomeSerializaer(income, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response("User is not authenticated", status=status.HTTP_401_UNAUTHORIZED)

class AddIncome(APIView):
    def post(self, request):
        if(request.user.is_authenticated):
            serializer = GetIncomeSerializaer(data=request.data)
            if(serializer.is_valid()):
                serializer.save()
            return Response("Income saved successfully", status=status.HTTP_200_OK) 
        return Response("User is not authorized to create a new income", status=status.HTTP_401_UNAUTHORIZED) 

class UpdateIncome(APIView):
    def post(self, request, pk):
        income = Income.objects.get(id=pk)
        serializer = GetIncomeSerializaer(instance=income,data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response("Income Updated successfully", status=status.HTTP_200_OK) 

@api_view(['DELETE'])
def DeleteIncome(request, pk):
    income = Income.objects.get(id=pk)
    income.delete()
    return Response("Income Deleted successfully", status=status.HTTP_200_OK)

@api_view(['GET'])
def ExpenseList(requet):
    if(requet.user.is_authenticated):
        expenses = Expense.objects.all()
        serializer = GetExchangeSerializaer(expenses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response('User is Not Authenticated', status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def ExpenseDetail(request, pk):
    if(request.user.is_authenticated):
        expense = Expense.objects.get(id=pk)
        serializer = GetExchangeSerializaer(expense, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response("User is not authenticated", status=status.HTTP_401_UNAUTHORIZED)

class AddExpense(APIView):
    def post(self, request):
        if(request.user.is_authenticated):
            serializer = GetExchangeSerializaer(data=request.data)
            if(serializer.is_valid()):
                serializer.save()
            return Response("Expense saved successfully", status=status.HTTP_200_OK) 
        return Response("User is not authorized to create a new expense", status=status.HTTP_401_UNAUTHORIZED) 

class UpdateExpense(APIView):
    def post(self, request, pk):
        expense = Expense.objects.get(id=pk)
        serializer = GetExchangeSerializaer(instance=expense,data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response("Expense Updated successfully", status=status.HTTP_200_OK) 

@api_view(['DELETE'])
def DeleteExpense(request, pk):
    expense = Expense.objects.get(id=pk)
    expense.delete()
    return Response("Expense Deleted successfully", status=status.HTTP_200_OK)

@api_view(['GET'])
def ExpenseTypeList(requet):
    if(requet.user.is_authenticated):
        expenses = ExpenseType.objects.all()
        serializer = ExpenseTypeSerializaer(expenses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response('User is Not Authenticated', status=status.HTTP_401_UNAUTHORIZED)

class AddExpenseType(APIView):
    def post(self, request):
        if(request.user.is_authenticated):
            serializer = ExpenseTypeSerializaer(data=request.data)
            if(serializer.is_valid()):
                serializer.save()
            return Response("Expense Type saved successfully", status=status.HTTP_200_OK) 
        return Response("User is not authorized to create a new expense type", status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def IncomeTypeList(requet):
    if(requet.user.is_authenticated):
        income = IncomeType.objects.all()
        serializer = IncomeTypeSerializaer(income, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response('User is Not Authenticated', status=status.HTTP_401_UNAUTHORIZED)

class AddIncomeType(APIView):
    def post(self, request):
        if(request.user.is_authenticated):
            serializer = IncomeTypeSerializaer(data=request.data)
            if(serializer.is_valid()):
                serializer.save()
            return Response("Income Type saved successfully", status=status.HTTP_200_OK) 
        return Response("User is not authorized to create a new income type", status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def ReportGeneration(request):
    incomes = Income.objects.all()
    expenses = Expense.objects.all()

    incomeTotal = 0
    for income in incomes:
        incomeTotal += income.amount

    expenseTotal = 0
    for expense in expenses:
        expenseTotal += expense.amount

    incomeNameTotalAmount = Income.objects.values('income_name').annotate(total_amt = Sum('amount'))
    expenseNameTotalAmount = Expense.objects.values('expense_name').annotate(total_amt = Sum('amount'))

    print(incomeNameTotalAmount,"Income Name Total amount")
    print(expenseNameTotalAmount,"Exense Name Total amount")

    return Response("Report Generated saved successfully", status=status.HTTP_200_OK)