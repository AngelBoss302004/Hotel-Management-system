from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Room

# Create your views here.


class hotel(APIView):

    def post(self, request):
        try:
            room_number = request.data.get('room_number')
            room_type = request.data.get('room_type')
            customer_name = request.data.get('customer_name')
            price = request.data.get('price')
            status = request.data.get('status')

            Room.objects.create(
                room_number=room_number,
                room_type=room_type,
                customer_name=customer_name,
                price=price,
                status=status
            )

            return Response("Room added successfully!")

        except Exception as e:
            return Response(str(e), status=400)

    def get(self, request, id=None):
        try:
            if id is not None:
                room = Room.objects.get(id=id)

                data = {
                    'id': room.id,
                    'room_number': room.room_number,
                    'room_type': room.room_type,
                    'customer_name': room.customer_name,
                    'price': room.price,
                    'status': room.status
                }

                return Response(data)

            rooms = Room.objects.all()

            data = []

            for room in rooms:
                data.append({
                    'id': room.id,
                    'room_number': room.room_number,
                    'room_type': room.room_type,
                    'customer_name': room.customer_name,
                    'price': room.price,
                    'status': room.status
                })

            return Response(data)

        except Room.DoesNotExist:
            return Response("Room not found!", status=404)

        except Exception as e:
            return Response(str(e), status=400)

    def put(self, request, id):
        try:
            room = Room.objects.get(id=id)

            room.room_number = request.data.get(
                'room_number', room.room_number)

            room.room_type = request.data.get(
                'room_type', room.room_type)

            room.customer_name = request.data.get(
                'customer_name', room.customer_name)

            room.price = request.data.get(
                'price', room.price)

            room.status = request.data.get(
                'status', room.status)

            room.save()

            return Response("Room updated successfully!")

        except Room.DoesNotExist:
            return Response("Room not found!", status=404)

        except Exception as e:
            return Response(str(e), status=400)

    def delete(self, request, id):
        try:
            room = Room.objects.get(id=id)

            room.delete()

            return Response("Room deleted successfully!")

        except Room.DoesNotExist:
            return Response("Room not found!", status=404)

        except Exception as e:
            return Response(str(e), status=400)