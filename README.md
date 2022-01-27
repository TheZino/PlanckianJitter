# Planckian Jitter data augmentation

![](./img.png)

Official implementation of the code from "Planckian jitter: enhancing the color quality of self-supervised visual
representations".

Code written in Pytorch v1.8.1.

Dependecies
- Pillow==7.2.0
- numpy==1.19.5
- torch==1.8.1

Example usage with other torchvision trasforms:

```
import torchvision.transforms as tranforms

from planckianTransforms import PlanckianJitter

data_transforms = [
            transforms.RandomResizedCrop(size=self.input_height),
            transforms.RandomHorizontalFlip(p=0.5),
            transforms.RandomVerticalFlip(p=0.5),
            transforms.RandomApply([PlanckianJitter(mode="blackbody")], p=0.8),
        ]
    
img_out = data_transforms(img)
```

If you are going to use this code please cite us:
```
t.b.d.
```

## License

MIT


