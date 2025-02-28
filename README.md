# Pet Store: Image Classifier
This is a pet store Image Classifier code that wraps the [Fabiuas/Animal-classifier](https://huggingface.co/Fabiuas/Animal-classifier) model.

## Quickstart: Smoketest
This project is intended to be served up within an AMIGOS DAG. Even so, it has an "example_driver" script in the repo for use for local "smoke tests" as well as an example of how to send the model images RESTfully.

## Quickstart: Model
This project uses a large Pytorch model to do inference. Rather than persist this file in Git, it's expedient to download this binary using the HuggingFace CLI per below.

```bash
$ pip install -U "huggingface_hub[cli]"
$ huggingface-cli download Fabiuas/Animal-classifier pytorch_model.bin --local-dir=./model
$ huggingface-cli download Fabiuas/Animal-classifier config.json --local-dir=./model
$ huggingface-cli download Fabiuas/Animal-classifier preprocessor_config.json --local-dir=./model
```

## Contributors
* __Jeremy Case__: jeremycase@odysseyconsult.com
