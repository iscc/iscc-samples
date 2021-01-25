from pathlib import Path
import iscc_samples as samples


def test_samples_texts():
    texts = samples.texts()
    assert isinstance(texts, list)
    assert isinstance(texts[0], Path)
    assert len(texts) == 16


def test_samples_images():
    images = samples.images()
    assert isinstance(images, list)
    assert isinstance(images[0], Path)
    assert len(images) == 6


def test_samples_audios():
    audios = samples.audios()
    assert isinstance(audios[0], Path)
    assert len(audios) == 5


def test_samples_videos():
    videos = samples.videos()
    assert isinstance(videos, list)
    assert isinstance(videos[0], Path)
    assert len(videos) == 21
