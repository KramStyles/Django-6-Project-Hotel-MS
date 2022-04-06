from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=240, unique=True)
    email = models.EmailField(max_length=240, unique=True)
    phone_number = models.CharField(max_length=240, default=None, null=True)
    password = models.CharField(max_length=240)
    otp_code = models.CharField(max_length=240, default=None, null=True)
    email_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField('Is Admin', default=False)
    is_superadmin = models.BooleanField('Is Super Admin', default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'User: {self.username.title()}'


class Receptionist(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=240, unique=True)
    last_name = models.CharField(max_length=240, unique=True)
    gender = models.CharField(max_length=240)
    avatar_url = models.CharField(max_length=240, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"Receptionist: {self.first_name} {self.last_name}"


class Room(models.Model):
    room_type_id = models.ForeignKey('RoomType', on_delete=models.CASCADE)
    room_status_id = models.ForeignKey('RoomStatus', on_delete=models.CASCADE)
    room_no = models.CharField(max_length=240, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'''Room :{self.room_no} price: #{self.room_type_id.price}
    is currently {self.room_status_id.status.upper()}.'''


class RoomStatus(models.Model):
    status = models.CharField(max_length=240, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"Room_status: {self.status}"


class RoomType(models.Model):
    room_type = models.CharField(max_length=240, unique=True)
    price = models.CharField(max_length=240)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"Room_type : {self.room_type}, price: {self.price}"


class Booking(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Receptionist, on_delete=models.CASCADE)
    payment_id = models.ForeignKey('Payment', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"Booking by {self.customer_id.username.title()} paid for Room {self.room_id.room_no}."


class Payment(models.Model):
    payment_type_id = models.ForeignKey('PaymentType', on_delete=models.CASCADE)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Receptionist, on_delete=models.CASCADE)
    amount = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.customer_id} paid #{self.amount} processed by {self.staff_id}."


class PaymentType(models.Model):
    name = models.CharField(max_length=240, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"Payment option: {self.name}"


class Reservation(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    payment_type_id = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Receptionist, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"Reservation: {self.customer_id.username.title()} booked Room: {self.room_id.room_no}."
