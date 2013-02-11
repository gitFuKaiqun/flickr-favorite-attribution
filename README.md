# flickr-favorite-attribution

Creates an image containing attributions for all of the favorites in a user's account


## Usage

1. Copy `config.sample.py` to `config.py` and make necessary modifications.

2. Run

```
python get_favorites.py
```

3. Compile `word_cloud` (make sure livraries from `requirements.txt` are installed):

```
cd word_cloud
make
```

4. Run

```
python plot_word_cloud.py
```

5. Upload the image with

```
python upload_image.py
```
