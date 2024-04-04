import os
from pathlib import Path
import text_renderer
from text_renderer.effect import *
from text_renderer.corpus import *
from text_renderer.config import (
    RenderCfg,
    NormPerspectiveTransformCfg,
    GeneratorCfg,
    SimpleTextColorCfg,
    UniformPerspectiveTransformCfg,
)
from text_renderer.effect.curve import Curve
CURRENT_DIR = Path('/Users/apple/text_renderer/text_renderer')
import imgaug.augmenters as iaa

text_effect_cfg = Effects([
    text_renderer.effect.DropoutRand(p=0.1), #Drop pixel
    Curve(p=0.5, period=180, amplitude=(1,8)), # Curve
    Line(0.2, thickness=(2, 5),line_pos_p=(0, 1, 0, 0, 0, 0, 0, 0, 0, 0)),  #Underline
    ImgAugEffect(p=0,aug=iaa.GaussianBlur(sigma=(0.5, 1.35))),   #Gaussian Blur
    Padding(p=1, w_ratio=[0.015, 0.021], h_ratio=[0.3, 0.35], center=True), #Add padding
])

extra_text_effect_cfg = Effects([
    Padding(p=1, w_ratio=[0.015, 0.021], h_ratio=[0.7, 0.75], center=True), #Add padding
])

# bg_effect_cfg = #

my_corpus = CharCorpus(
    CharCorpusCfg(
        text_paths=[CURRENT_DIR/"corpus/c4_ja_0.txt"] ,
        length=(3,39),
        font_size=(35, 68),

        font_dir=CURRENT_DIR / "font",
        char_spacing = (-0.1, 0.3),

        # horizontal= False  # horizontal
    ),
)

def story_data():
    return GeneratorCfg(
        num_image=100,
        save_dir=CURRENT_DIR / "output",
        render_cfg=RenderCfg(
              corpus= [my_corpus, my_corpus],
              corpus_effects=[text_effect_cfg, extra_text_effect_cfg],
              bg_dir=CURRENT_DIR / "bg",
              layout=text_renderer.layout.ExtraTextLineLayout(bottom_prob=0.05),
              perspective_transform=UniformPerspectiveTransformCfg(12, 12, 1.2), # rotate
              # render_effects=bg_effect_cfg
              text_color_cfg=SimpleTextColorCfg(),
              height=70,
              gray=False,
              return_bg_and_mask=False
          ),
    )

configs = [story_data()]
