
from unicodedata import category
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, Response, JsonResponse
from .models import Profile,Category,Cart,Order,Product

# @api_view(['POST'])
# def admin_registser(request):
#     User.objects.create_user(email=request.data["email"],password=request.data["pwd"],username=request.data["usr"],
#     is_staff=1,is_superuser=1)
#     return HttpResponse('Register')

# @api_view(['POST'])
# def user_registser(request):
#     User.objects.create_user(email=request.data["email"],password=request.data["pwd"],username=request.data["usr"])
#     return HttpResponse('Register')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['first_name'] = user.first_name
        token['email'] = user.email
        # send params into the token
        # should export it in the Loginslicer
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def register(request):
    isStaff = request.data["staff"]
    user = User.objects.create_user(
        email=request.data["email"], password=request.data["password"],
        is_staff=isStaff, first_name=request.data['first_name'],
        last_name=request.data['last_name'])
    Profile.objects.create(user=user, phone=request.data['phone'],
                           address=request.data['address'], gender=request.data['gender'])
    return Response("routes")



@api_view(['POST'])
@permission_classes([IsAuthenticated])
# only for admin
def add_category(request):
#    name= models.CharField(max_length=50, null=True, blank=True)
    Category.objects.create(name=request.data['name'])
    return Response('added')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
# only for admin
def get_category(request):
    categoryLst=[]
    for cat in Category.objects.all():
        categoryLst.append({'name':cat.name})
    return JsonResponse(categoryLst)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
# only for admin
def add_product(request):
    Product.objects.create(description=request.data['description'],
    photo=request.data['photo'],
    price=request.data['price'],
    category=request.data['category'],
    )
    #  description = models.CharField(max_length=50,null=True,blank=True)
    # photo=models.ImageField(null=True,blank=True)
    # category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    # price = models.DecimalField(max_digits=100,decimal_places=2)
    return Response('added')





def test(request):
    return HttpResponse('hello world')
