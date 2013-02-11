# flickr-favorite-attribution

Creates an image containing attributions for all of the favorites in a user's account


## Usage

Copy `config.sample.py` to `config.py` and make necessary modifications.

Run

```
python get_favorites.py
```

Compile `word_cloud` (make sure livraries from `requirements.txt` are installed):

```
cd word_cloud
make
```

Run

```
python plot_word_cloud.py
```

Upload the image with

```
python upload_image.py
```
