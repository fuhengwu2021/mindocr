# Use MindOCR for Curved Text

## Clone MindOCR

`git clone https://github.com/mindspore-lab/mindocr.git`

## Environmental Variable Setup

`export GLOG_v=4`

## Run MindOCR

Command:

```
python ../tools/infer/text/predict_system.py --image_dir customer_issue_curved_text.png --det_algorithm DB_MV3 --rec_algorithm CRNN
```

Result:

```
[2023-10-03 22:24:44] mindocr.models.backbones.mindcv_models.utils INFO - Finish loading model checkpoint from: /home/wukong/.mindspore/models/dbnet_mobilenetv3-62c44539.ckpt
[2023-10-03 22:24:44] mindocr INFO - Init detection model: DB_MV3 --> dbnet_mobilenetv3. Model weights loaded from pretrained url
[2023-10-03 22:24:44] mindocr INFO - Pick optimal preprocess hyper-params for det algo DB_MV3:
 {'DetResize': {'target_size': None, 'keep_ratio': True, 'limit_side_len': 960, 'limit_type': 'max', 'padding': False, 'force_divisable': True}}
[2023-10-03 22:24:44] mindocr.data.transforms.det_transforms INFO - `limit_type` is max. Image will be resized by limiting the max side length to 960.
[2023-10-03 22:24:44] mindocr INFO - recognize in batch mode batch_size: 8
[2023-10-03 22:24:44] mindocr.models.backbones.mindcv_models.utils INFO - Finish loading model checkpoint from: /home/wukong/.mindspore/models/crnn_resnet34-83f37f07.ckpt
[2023-10-03 22:24:44] mindocr INFO - Init recognition model: CRNN --> crnn_resnet34. Model weights loaded from pretrained url
[2023-10-03 22:24:44] mindocr WARNING - `rec_image_shape` [' 32', ' 320'] dose not meet the network input requirement or is not optimal, which should be [32, 100] under batch mode = True
[2023-10-03 22:24:44] mindocr INFO - Pick optimal preprocess hyper-params for rec algo CRNN:
target_height:	32
target_width:	100
padding:	False
keep_ratio:	False
norm_before_pad:	False
[2023-10-03 22:24:44] mindocr.postprocess.rec_postprocess INFO - `character_dict_path` for RecCTCLabelDecode is not given. Default dict "0123456789abcdefghijklmnopqrstuvwxyz" is applied. Only number and English letters (regardless of lower/upper case) will be recognized and evaluated.
[2023-10-03 22:24:44] mindocr INFO - 
INFO: Infering [1/1]: customer_issue_curved_text.png
[2023-10-03 22:24:44] mindocr INFO - Original image shape: (37, 207, 3)
[2023-10-03 22:24:44] mindocr INFO - After det preprocess: (3, 64, 224)
[2023-10-03 22:24:46] mindocr INFO - Num detected text boxes: 4
Det time: 1.4675424098968506
[2023-10-03 22:24:46] mindocr INFO - num images for rec: 4
[2023-10-03 22:24:46] mindocr INFO - Rec img idx range: [0, 4)
[2023-10-03 22:24:47] mindocr INFO - Recognized texts: 
company	1.0
inc	0.9999683499336243
delivery	0.9999999403953552
a	0.47223836183547974
Rec time: 0.7644393444061279
[2023-10-03 22:24:47] mindocr INFO - Total time:2.2583811283111572
[2023-10-03 22:24:47] mindocr INFO - Average FPS: 0.4427950568059392
[2023-10-03 22:24:47] mindocr INFO - Averge time cost: {'det': 1.4675424098968506, 'rec': 0.7644393444061279, 'all': 2.2583811283111572}
[2023-10-03 22:24:47] mindocr INFO - Done! Results saved in ./inference_results/system_results.txt
```

This run will generate an annotation file which can be consumed by our OCR.

## Visualization

Command:

```
python vis.py
```
