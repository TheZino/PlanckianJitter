import torchvision.transforms as transforms
from PIL import Image
from planckianTransforms import PlanckianJitter

if __name__ == "__main__":

    img = Image.open('./demo_img/flw.jpg')

    data_transforms = transforms.Compose([
        transforms.RandomResizedCrop(size=img.size[0]),
        transforms.RandomHorizontalFlip(p=0.5),
        transforms.RandomVerticalFlip(p=0.5),
        transforms.RandomApply([PlanckianJitter(mode="blackbody")], p=0.8)])

    img_out = data_transforms(img)

    img_out.show()
