from main import celery_app

# the celery task can be called in similar way with parameters passed after the fucntion name
email_task = celery_app.send_task(
    'tasks.test_task',
        args=[10]
)


#**to schedule a celery task to be executed after some time
#celery_task = function_name.apply_async(
#             args=[
#                 str(tenant_db.schema_name),
#                 tenant_db.org_id,
#             ],
#             countdown=policy_deletion_time,#countdown time to be deleted
#         )

#**to revoke a celery task
#celery_app.control.revoke(celery_task_id, terminate=True)