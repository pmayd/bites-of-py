from decorators import make_html
import pytest

def test_make_html():
    @make_html('p')
    @make_html('strong')
    def get_text(text='I code with PyBites'):
        return text

    assert get_text() == '<p><strong>I code with PyBites</strong></p>'


if __name__ == "__main__":
    pytest.main()