```bash
2023-06-27T02:46:54,947 [INFO ] W-9000-eva02_large_patch14_clip_336.merged2b_ft_inat21_1.0-stdout MODEL_LOG -   File "/home/venv/lib/python3.9/site-packages/ts/model_service_worker.py", line 131, in load_model
2023-06-27T02:46:54,947 [INFO ] W-9000-eva02_large_patch14_clip_336.merged2b_ft_inat21_1.0-stdout MODEL_LOG -     service = model_loader.load(
2023-06-27T02:46:54,947 [INFO ] epollEventLoopGroup-5-1 org.pytorch.serve.wlm.WorkerThread - 9000 Worker disconnected. WORKER_STARTED
2023-06-27T02:46:54,947 [INFO ] W-9000-eva02_large_patch14_clip_336.merged2b_ft_inat21_1.0-stdout MODEL_LOG -   File "/home/model-server/tmp/models/a0566cf149e24c5eae00ce4170b9770d/ts/model_loader.py", line 135, in load
2023-06-27T02:46:54,947 [INFO ] epollEventLoopGroup-5-1 org.pytorch.serve.wlm.WorkerThread - 9000 Worker disconnected. WORKER_STARTED
2023-06-27T02:46:54,947 [INFO ] W-9000-eva02_large_patch14_clip_336.merged2b_ft_inat21_1.0-stdout MODEL_LOG -     initialize_fn(service.context)
2023-06-27T02:46:54,948 [INFO ] W-9000-eva02_large_patch14_clip_336.merged2b_ft_inat21_1.0-stdout MODEL_LOG -   File "/home/model-server/tmp/models/a0566cf149e24c5eae00ce4170b9770d/timm_image_classifier.py", line 33, in initialize
2023-06-27T02:46:54,948 [DEBUG] W-9000-eva02_large_patch14_clip_336.merged2b_ft_inat21_1.0 org.pytorch.serve.wlm.WorkerThread - System state is : WORKER_STARTED
2023-06-27T02:46:54,948 [INFO ] W-9000-eva02_large_patch14_clip_336.merged2b_ft_inat21_1.0-stdout MODEL_LOG -     model_dir = properties.get("model_dir")
2023-06-27T02:46:54,948 [DEBUG] W-9000-eva02_large_patch14_clip_336.merged2b_ft_inat21_1.0 org.pytorch.serve.wlm.WorkerThread - System state is : WORKER_STARTED
2023-06-27T02:46:54,948 [INFO ] W-9000-eva02_large_patch14_clip_336.merged2b_ft_inat21_1.0-stdout MODEL_LOG - NameError: name 'properties' is not defined


2023-06-27T03:23:57,853 [INFO ] W-9000-eva02_large_patch14_clip_336.merged2b_ft_inat21_1.0-stdout MODEL_LOG -     self.model = create_model(
2023-06-27T03:23:57,853 [INFO ] W-9000-eva02_large_patch14_clip_336.merged2b_ft_inat21_1.0-stdout MODEL_LOG - TypeError: create_model() missing 1 required positional argument: 'model_name'




2023-06-27T03:32:26,630 [INFO ] W-9000-eva02_large_patch14_clip_336.merged2b_ft_inat21_1.0-stdout MODEL_LOG -     self.model = create_model(
2023-06-27T03:32:26,630 [INFO ] W-9000-eva02_large_patch14_clip_336.merged2b_ft_inat21_1.0-stdout MODEL_LOG -   File "/home/model-server/tmp/models/fbce45821f9c4199b7e106665a1792cd/timm/models/_factory.py", line 114, in create_model
2023-06-27T03:32:26,630 [INFO ] W-9000-eva02_large_patch14_clip_336.merged2b_ft_inat21_1.0-stdout MODEL_LOG -     model = create_fn(
2023-06-27T03:32:26,630 [INFO ] epollEventLoopGroup-5-1 org.pytorch.serve.wlm.WorkerThread - 9000 Worker disconnected. WORKER_STARTED
2023-06-27T03:32:26,630 [INFO ] epollEventLoopGroup-5-1 org.pytorch.serve.wlm.WorkerThread - 9000 Worker disconnected. WORKER_STARTED
2023-06-27T03:32:26,630 [INFO ] W-9000-eva02_large_patch14_clip_336.merged2b_ft_inat21_1.0-stdout MODEL_LOG -   File "/home/model-server/tmp/models/fbce45821f9c4199b7e106665a1792cd/timm/models/eva.py", line 1067, in eva02_large_patch14_clip_336
2023-06-27T03:32:26,631 [INFO ] W-9000-eva02_large_patch14_clip_336.merged2b_ft_inat21_1.0-stdout MODEL_LOG -     model = _create_eva('eva02_large_patch14_clip_336', pretrained=pretrained, **dict(model_args, **kwargs))
2023-06-27T03:32:26,631 [DEBUG] W-9000-eva02_large_patch14_clip_336.merged2b_ft_inat21_1.0 org.pytorch.serve.wlm.WorkerThread - System state is : WORKER_STARTED
2023-06-27T03:32:26,631 [INFO ] W-9000-eva02_large_patch14_clip_336.merged2b_ft_inat21_1.0-stdout MODEL_LOG -   File "/home/model-server/tmp/models/fbce45821f9c4199b7e106665a1792cd/timm/models/eva.py", line 645, in _create_eva
2023-06-27T03:32:26,631 [INFO ] W-9000-eva02_large_patch14_clip_336.merged2b_ft_inat21_1.0-stdout MODEL_LOG -     model = build_model_with_cfg(
2023-06-27T03:32:26,631 [INFO ] W-9000-eva02_large_patch14_clip_336.merged2b_ft_inat21_1.0-stdout MODEL_LOG -   File "/home/model-server/tmp/models/fbce45821f9c4199b7e106665a1792cd/timm/models/_builder.py", line 381, in build_model_with_cfg
2023-06-27T03:32:26,631 [INFO ] W-9000-eva02_large_patch14_clip_336.merged2b_ft_inat21_1.0-stdout MODEL_LOG -     model = model_cls(**kwargs)
2023-06-27T03:32:26,631 [INFO ] W-9000-eva02_large_patch14_clip_336.merged2b_ft_inat21_1.0-stdout MODEL_LOG - TypeError: __init__() got an unexpected keyword argument 'hf_hub_id'
```