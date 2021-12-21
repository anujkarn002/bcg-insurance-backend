from rest_framework.generics import ListAPIView, GenericAPIView, UpdateAPIView
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from rest_framework.response import Response
from .serializers import PolicySerializer, StatSerializer
from .models import Policy

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class PolicyStatView(ListAPIView):
    serializer_class = StatSerializer
    queryset = Policy.objects.get_monthly_data()

    def get_queryset(self):
        region = self.request.query_params.get('region', None)
        if region:
            return Policy.objects.get_monthly_data(region=region)
        return Policy.objects.get_monthly_data()

    def get_serializer_context(self):
        return {'request': self.request}

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class PolicyListView(ListAPIView):
    serializer_class = PolicySerializer
    queryset = Policy.objects.all()
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Policy.objects.all()
        try:
            q = int(self.request.query_params.get('q'))
        except (ValueError, TypeError):
            q = None
        if q is not None:
            # search through id or customer id
            queryset = queryset.filter(Q(id__icontains=q) | Q(customer__id__icontains=q))
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



class PolicyUpdateView(UpdateAPIView):
    serializer_class = PolicySerializer
    queryset = Policy.objects.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

