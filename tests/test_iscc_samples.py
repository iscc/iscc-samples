from pathlib import Path
import iscc_samples as samples


def test_samples_all():
    files = samples.all()
    assert isinstance(files, list)
    assert isinstance(files[0], Path)
    assert len(files) == 55
    assert files[0].name == "demo.doc"


def test_samples_texts():
    texts = samples.texts()
    assert isinstance(texts, list)
    assert isinstance(texts[0], Path)
    assert len(texts) == 18
    assert texts[0].name == "demo.doc"


def test_samples_text_ext():
    texts = samples.texts(".md")
    assert texts[0].name == "demo.md"


def test_samples_images():
    images = samples.images()
    assert isinstance(images, list)
    assert isinstance(images[0], Path)
    assert len(images) == 6
    assert images[0].name == "demo.bmp"


def test_samples_audios():
    audios = samples.audios()
    assert isinstance(audios[0], Path)
    assert len(audios) == 10
    assert audios[0].name == "demo.aac"


def test_samples_videos():
    videos = samples.videos()
    assert isinstance(videos, list)
    assert isinstance(videos[0], Path)
    assert len(videos) == 21
    assert videos[0].name == "demo.3g2"


def test_audio_cover():
    assert samples.audios('mp3')[1].name == "withcover.mp3"
