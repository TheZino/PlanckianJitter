# Planckian Jitter data augmentation

![](./img.png)

Official implementation of the code from ["Planckian jitter: enhancing the color quality of self-supervised visual
representations"](https://arxiv.org/abs/2202.07993).

Code written in Pytorch v1.8.1.

Dependencies
- Pillow==7.2.0
- numpy==1.19.5
- torch==1.8.1

Example usage with other torchvision transforms:

```python
import torchvision.transforms as transforms
from PIL import Image

from planckianTransforms import PlanckianJitter

img = Image.open('./examples/flower.jpeg')

data_transforms = transforms.Compose([
    	transforms.RandomResizedCrop(size=img.size[0]),
    	transforms.RandomHorizontalFlip(p=0.5),
    	transforms.RandomVerticalFlip(p=0.5),
    	transforms.RandomApply([PlanckianJitter(mode="blackbody")], p=0.8)])

img_out = data_transforms(img)
img_out.save('./examples/out.png')
```

Two parameters can be passed to the transform:
- mode: choose between `BlackBody` points sampling or `CIED`. \[Default is `BlackBody`\]
- idx: if idx is provided a specific illuminant is used instead of a random one from the sampled list.

```python
# randomly selects an illuminant from the BlackBody list.
PlanckianJitter(mode="blackbody")

# randomly selects an illuminant from the CIED list.
PlanckianJitter(mode="CIED")

# selects the illuminant at index 5 of the BlackBody list.
PlanckianJitter(mode="blackbody", idx=5)
```

## Reference
If you are going to use this code please cite us:
```
@article{zini2022planckian,
  title={Planckian jitter: enhancing the color quality of self-supervised visual representations},
  author={Zini, Simone and Buzzelli, Marco and Twardowski, Bart{\l}omiej and van de Weijer, Joost},
  journal={arXiv preprint arXiv:2202.07993},
  year={2022}
}
```

## License

MIT
