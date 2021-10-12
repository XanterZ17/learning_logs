"""Defines URL patterns fo learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Path that shows all topics.
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Adding.
    # Toppic.
    path('new_topic/', views.new_topic, name='new_topic'),
    # Entry.
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),

    # Editing.
    # Entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),


    # Deleting.
    # Topic.
    path('topics/delete_topic/<int:topic_id>', views.delete_topic, name='delete_topic'),
    # Tntry.
    path('topics/<int:topic_id>/delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry')
]