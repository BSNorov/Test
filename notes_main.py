import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QLabel, QPushButton, QTextEdit,
    QComboBox, QFrame, QGraphicsDropShadowEffect
)
from PyQt6.QtGui import QColor, QFont


STYLE = """
QMainWindow {
    background-color: #0B0D17;
}

QWidget {
    color: #F2F2FA;
    font-family: "Arial";
    font-size: 14px;
}

QFrame#sidebar {
    background: #111421;
    border-right: 1px solid #25283B;
}

QFrame#card {
    background: #171A2B;
    border: 1px solid #30334B;
    border-radius: 20px;
}

QFrame#topbar {
    background: transparent;
    border-bottom: 1px solid #25283B;
}

QLabel#logo {
    color: #B6A4FF;
    font-size: 25px;
    font-weight: bold;
}

QLabel#heading {
    font-size: 30px;
    font-weight: bold;
}

QLabel#subtitle {
    color: #9295AE;
    font-size: 13px;
}

QLabel#section {
    color: #B9BBD0;
    font-size: 12px;
    font-weight: bold;
}

QTextEdit {
    background: transparent;
    border: none;
    color: #F6F4FF;
    font-size: 20px;
    selection-background-color: #7559D9;
}

QComboBox {
    background: #24273B;
    color: white;
    border: 1px solid #383B55;
    border-radius: 10px;
    padding: 10px 14px;
    min-width: 135px;
}

QComboBox::drop-down {
    border: none;
    width: 24px;
}

QComboBox QAbstractItemView {
    background: #24273B;
    color: white;
    selection-background-color: #7455DB;
    padding: 6px;
}

QPushButton {
    border: none;
    border-radius: 11px;
    padding: 11px 16px;
    background: #25283C;
    color: #DCDDF0;
    font-weight: bold;
}

QPushButton:hover {
    background: #343850;
}

QPushButton#primary {
    background: #825CF4;
    color: white;
    font-size: 15px;
    padding: 15px 25px;
}

QPushButton#primary:hover {
    background: #9878FF;
}

QPushButton#nav {
    background: transparent;
    text-align: left;
    padding: 14px;
    color: #999DB8;
}

QPushButton#nav:hover {
    background: #24273C;
    color: white;
}

QPushButton#active {
    background: #30264F;
    color: #C4B0FF;
    text-align: left;
    padding: 14px;
}
"""


class TranslatorApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("LINGUA — Translation Studio")
        self.resize(1200, 760)
        self.setMinimumSize(850, 600)

        self.setStyleSheet(STYLE)

        self.languages = {
            "English": "en",
            "Русский": "ru",
            "中文": "zh-CN",
            "Español": "es",
            "Français": "fr",
            "Deutsch": "de",
            "日本語": "ja",
            "한국어": "ko",
            "Türkçe": "tr",
            "العربية": "ar"
        }

        self.setup_ui()

    def shadow(self, widget):
        effect = QGraphicsDropShadowEffect()
        effect.setBlurRadius(35)
        effect.setOffset(0, 10)
        effect.setColor(QColor(0, 0, 0, 65))
        widget.setGraphicsEffect(effect)

    def setup_ui(self):

        root = QWidget()
        self.setCentralWidget(root)

        main = QHBoxLayout(root)
        main.setContentsMargins(0, 0, 0, 0)
        main.setSpacing(0)

        # SIDEBAR
        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(215)

        side_layout = QVBoxLayout(sidebar)
        side_layout.setContentsMargins(18, 28, 18, 25)
        side_layout.setSpacing(12)

        logo = QLabel("✦  LINGUA")
        logo.setObjectName("logo")
        side_layout.addWidget(logo)

        tagline = QLabel("TRANSLATION STUDIO")
        tagline.setObjectName("subtitle")
        side_layout.addWidget(tagline)

        side_layout.addSpacing(45)

        nav1 = QPushButton("◈   Translator")
        nav1.setObjectName("active")

        nav2 = QPushButton("◷   History")
        nav2.setObjectName("nav")

        nav3 = QPushButton("☆   Favorites")
        nav3.setObjectName("nav")

        nav4 = QPushButton("⚙   Settings")
        nav4.setObjectName("nav")

        side_layout.addWidget(nav1)
        side_layout.addWidget(nav2)
        side_layout.addWidget(nav3)
        side_layout.addWidget(nav4)

        side_layout.addStretch()

        status = QLabel("●  Interface ready")
        status.setStyleSheet(
            "color: #64D7AC; font-size: 12px;"
        )

        side_layout.addWidget(status)

        version = QLabel("LINGUA  /  VERSION 1.0")
        version.setObjectName("subtitle")
        side_layout.addWidget(version)

        main.addWidget(sidebar)

        # MAIN CONTENT
        content = QWidget()
        content_layout = QVBoxLayout(content)

        content_layout.setContentsMargins(
            35, 25, 35, 30
        )
        content_layout.setSpacing(25)

        # TOP BAR
        topbar = QFrame()
        topbar.setObjectName("topbar")

        top_layout = QHBoxLayout(topbar)
        top_layout.setContentsMargins(0, 0, 0, 18)

        top_title = QLabel("Workspace")
        top_title.setStyleSheet(
            "font-size: 15px; font-weight: bold;"
        )

        top_layout.addWidget(top_title)
        top_layout.addStretch()

        badge = QLabel("✦  CREATIVE STUDIO")
        badge.setStyleSheet("""
            background: #28213F;
            color: #C6B2FF;
            padding: 9px 15px;
            border-radius: 12px;
            font-size: 11px;
            font-weight: bold;
        """)

        top_layout.addWidget(badge)
        content_layout.addWidget(topbar)

        # HEADER
        heading = QLabel("Translate anything.")
        heading.setObjectName("heading")

        subtitle = QLabel(
            "Your words, every language. "
            "A beautiful space for communication."
        )
        subtitle.setObjectName("subtitle")

        content_layout.addWidget(heading)
        content_layout.addWidget(subtitle)

        # LANGUAGE SELECTION
        language_row = QHBoxLayout()
        language_row.setSpacing(15)

        self.source_lang = QComboBox()
        self.target_lang = QComboBox()

        for language in self.languages:
            self.source_lang.addItem(language)
            self.target_lang.addItem(language)

        self.source_lang.setCurrentText("English")
        self.target_lang.setCurrentText("Русский")

        swap_btn = QPushButton("⇄")
        swap_btn.setFixedSize(48, 44)
        swap_btn.setToolTip("Swap languages")
        swap_btn.clicked.connect(self.swap_languages)

        language_row.addWidget(self.source_lang)
        language_row.addStretch()
        language_row.addWidget(swap_btn)
        language_row.addStretch()
        language_row.addWidget(self.target_lang)

        content_layout.addLayout(language_row)

        # TRANSLATION CARDS
        cards = QHBoxLayout()
        cards.setSpacing(18)

        # INPUT CARD
        input_card = QFrame()
        input_card.setObjectName("card")

        input_layout = QVBoxLayout(input_card)
        input_layout.setContentsMargins(22, 22, 22, 20)
        input_layout.setSpacing(15)

        input_title = QLabel("ORIGINAL TEXT")
        input_title.setObjectName("section")

        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText(
            "Type or paste your text here..."
        )

        self.counter = QLabel("0 characters")
        self.counter.setObjectName("subtitle")

        clear_btn = QPushButton("✕  Clear")
        clear_btn.clicked.connect(self.clear_text)

        input_bottom = QHBoxLayout()
        input_bottom.addWidget(self.counter)
        input_bottom.addStretch()
        input_bottom.addWidget(clear_btn)

        input_layout.addWidget(input_title)
        input_layout.addWidget(self.input_text)
        input_layout.addLayout(input_bottom)

        # OUTPUT CARD
        output_card = QFrame()
        output_card.setObjectName("card")

        output_layout = QVBoxLayout(output_card)
        output_layout.setContentsMargins(22, 22, 22, 20)
        output_layout.setSpacing(15)

        output_title = QLabel("TRANSLATION")
        output_title.setObjectName("section")

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setPlaceholderText(
            "Your translation will appear here..."
        )

        self.copy_btn = QPushButton("▢  Copy")
        self.copy_btn.clicked.connect(self.copy_translation)

        output_bottom = QHBoxLayout()
        output_bottom.addStretch()
        output_bottom.addWidget(self.copy_btn)

        output_layout.addWidget(output_title)
        output_layout.addWidget(self.output_text)
        output_layout.addLayout(output_bottom)

        cards.addWidget(input_card, 1)
        cards.addWidget(output_card, 1)

        self.shadow(input_card)
        self.shadow(output_card)

        content_layout.addLayout(cards, 1)

        # BOTTOM CONTROLS
        bottom = QHBoxLayout()

        self.message = QLabel("Ready to translate")
        self.message.setObjectName("subtitle")

        self.translate_btn = QPushButton(
            "✦   Translate now   →"
        )
        self.translate_btn.setObjectName("primary")
        self.translate_btn.setMinimumWidth(210)
        self.translate_btn.clicked.connect(
            self.translate_placeholder
        )

        bottom.addWidget(self.message)
        bottom.addStretch()
        bottom.addWidget(self.translate_btn)

        content_layout.addLayout(bottom)

        # FOOTER
        footer = QLabel(
            "LINGUA STUDIO   •   Designed for language lovers"
        )
        footer.setObjectName("subtitle")
        footer.setAlignment(Qt.AlignmentFlag.AlignCenter)

        content_layout.addWidget(footer)

        main.addWidget(content, 1)

        # SIGNALS
        self.input_text.textChanged.connect(
            self.update_counter
        )

    def update_counter(self):
        text = self.input_text.toPlainText()
        self.counter.setText(
            f"{len(text)} characters"
        )

    def clear_text(self):
        self.input_text.clear()
        self.output_text.clear()
        self.message.setText("Ready to translate")

    def swap_languages(self):
        source = self.source_lang.currentIndex()
        target = self.target_lang.currentIndex()

        self.source_lang.setCurrentIndex(target)
        self.target_lang.setCurrentIndex(source)

        # Swap existing texts too
        original = self.input_text.toPlainText()
        translated = self.output_text.toPlainText()

        if translated:
            self.input_text.setPlainText(translated)
            self.output_text.setPlainText(original)

    def copy_translation(self):
        text = self.output_text.toPlainText()

        if text:
            QApplication.clipboard().setText(text)
            self.message.setText("✓ Copied to clipboard")
        else:
            self.message.setText("Nothing to copy yet")

    def translate_placeholder(self):
        text = self.input_text.toPlainText().strip()

        if not text:
            self.message.setText(
                "Please enter some text first"
            )
            return

        # Future translation API goes here.
        # Example:
        #
        # result = translator.translate(text)
        # self.output_text.setPlainText(result)

        self.message.setText(
            "Translation engine not connected yet"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setFont(QFont("Arial", 12))

    window = TranslatorApp()
    window.show()

    sys.exit(app.exec())
