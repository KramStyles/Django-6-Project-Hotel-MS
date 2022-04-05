from pyexpat import model
import uuid
from django.db import models
from django.db.models.deletion import CASCADE
# Create your models here.

class User (models.Model):

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length = 254, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    password = models.CharField(max_length=50), 
    otp_code = models.CharField(max_length=6, unique=True, null=True)
    email_verification = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return "User: " + self.username
    
class Receptionist(models.Model):
    
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField( max_length=20)
    last_name = models.CharField( max_length=20)
    gender = models.CharField( max_length=6)
    avatar_url = models.CharField(max_length=260, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return f"Receptionest:{self.first_name} {self.last_name}"

class  Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room_type_id = models.ForeignKey('Room_type', on_delete=models.CASCADE)
    room_status_id = models.ForeignKey('Room_status', on_delete=models.CASCADE)
    room_no = models.CharField(max_length=6, unique=True)
    price = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return f"Room :{self.room_no} price:{self.price} is currently {self.room_status_id}"

class Room_status(models.Model):
   
    status = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self):
        return f"Room_status: {self.status}"

class Room_type(models.Model):
    
    type = models.CharField(max_length=20, unique=True)
    price = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return f"Room_type : {self.type} price: {self.price}"

class Booking(models.Model): 
    
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(User, on_delete=CASCADE)
    staff_id = models.ForeignKey(Receptionist, on_delete=CASCADE)
    payment_id = models.ForeignKey('Payment' , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return f"Booking by customer :{self.customer_id} paid {self.payment_id} for room {self.room_id}"

class  Payment(models.Model):
    
    payment_type_id = models.ForeignKey('Payment_type', on_delete=models.CASCADE)
    customer_id = models.ForeignKey(User, on_delete=CASCADE)
    staff_id = models.ForeignKey(Receptionist, on_delete=CASCADE)
    amount = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return f"Customer {self.customer_id} amount:{self.amount} processed by staff {self.staff_id}"


class Payment_type(models.Model):
    
    name = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return  f"Payment option: {self.name}"
class Reservation (models.Model):
    
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    payment_type_id = models.ForeignKey(Payment_type, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(User, on_delete=CASCADE)
    staff_id = models.ForeignKey(Receptionist, on_delete=CASCADE)
    start_time =models.TimeField( auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return f"Reservation:{self.name} booked {self.rook_id}"
