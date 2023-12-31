import json

from rest_framework import serializers
from airss.models import RSSFeedSource, RssFeedAiContent, RssFeedAiSettings, FetchedNews


class RSSFeedSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RSSFeedSource
        fields = ('id', 'feed_source_name', 'feed_url')


class RssFeedAiContentSerializer(serializers.ModelSerializer):
    source = serializers.PrimaryKeyRelatedField(queryset=RSSFeedSource.objects.all(), many=False)

    class Meta:
        model = RssFeedAiContent
        fields = ["title", "preamble", "text", "article_url", "source", "image_url", "source_feed_id", "pub_date"]


class RssFeedAiSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RssFeedAiSettings
        fields = ['_id', 'keywords', 'negative_keywords']


class FetchedNewsSerializer(serializers.ModelSerializer):
    source = serializers.PrimaryKeyRelatedField(queryset=RSSFeedSource.objects.all(), many=False)

    class Meta:
        model = FetchedNews
        fields = ['source', 'feed_id']
