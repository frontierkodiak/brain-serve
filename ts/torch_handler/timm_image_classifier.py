"""
Module for image classification default handler
"""
import torch
import torch.nn.functional as F
from torchvision import transforms

from ts.torch_handler.vision_handler import VisionHandler
from ts.utils.util  import map_class_to_label

from timm.models import create_model

class TimmImageClassifier(VisionHandler):
    """
    ImageClassifier handler class. This handler takes an image
    and returns the name of object in that image.
    """

    topk = 5
    # These are the standard Imagenet dimensions
    # and statistics
    image_processing = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])

    def initialize(self, context):
        self.manifest = context.manifest

        model_dir = properties.get("model_dir")
        self.model_pt_path = None
        if "serializedFile" in self.manifest["model"]:
            serialized_file = self.manifest["model"]["serializedFile"]
            self.model_pt_path = os.path.join(model_dir, serialized_file)

        model_json_path = os.path.join(model_dir, "model.json")
        with open(model_json_path,'r') as rf: 
            model_dict = json.load(rf)
        self.model = create_model(
            checkpoint_path=self.model_pt_path, **model_dict)  # from timm.models import create_model
        self.model.to(self.device)
        self.model.eval()

        logger.debug("Model loaded successfully")

        # # Preprocessing transforms
        # data_json_path = os.path.join(model_dir, "data.json")
        # with open(data_json_path,'r') as rf: 
        #     data_dict = json.load(rf)
        # self.image_processing = transforms_imagenet_eval(**data_dict)  # from timm.data.transforms_factory import transforms_imagenet_eval

    

    def set_max_result_classes(self, topk):
        self.topk = topk

    def get_max_result_classes(self):
        return self.topk

    def postprocess(self, data):
        ps = F.softmax(data, dim=1)
        probs, classes = torch.topk(ps, self.topk, dim=1)
        probs = probs.tolist()
        classes = classes.tolist()
        return map_class_to_label(probs, self.mapping, classes)
