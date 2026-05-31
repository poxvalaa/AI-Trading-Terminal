import sys

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView
)

from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QColor, QFont

from predictor import get_all_predictions

from datetime import datetime


class TradingWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("AI Forex Terminal")

        self.resize(1100, 650)

        self.setStyleSheet("""
            QMainWindow{
                background:#0f172a;
            }

            QWidget{
                background:#0f172a;
                color:white;
            }

            QLabel{
                color:white;
            }

            QTableWidget{
                background:#111827;
                color:white;
                border:none;
                gridline-color:#1f2937;
                font-size:14px;
            }

            QHeaderView::section{
                background:#1e293b;
                color:white;
                padding:10px;
                border:none;
                font-weight:bold;
            }

            QTableWidget::item{
                padding:8px;
            }
        """)

        layout = QVBoxLayout()

        title = QLabel("AI FOREX TERMINAL")

        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title.setFont(
            QFont(
                "Arial",
                18,
                QFont.Weight.Bold
            )
        )

        layout.addWidget(title)

        self.table = QTableWidget()

        self.table.setColumnCount(5)

        self.table.setHorizontalHeaderLabels([
            "PAIR",
            "FORECAST",
            "CONFIDENCE",
            "SIGNAL",
            "HORIZON"
        ])

        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.table.verticalHeader().setVisible(False)

        layout.addWidget(self.table)

        self.status = QLabel()

        self.status.setAlignment(
            Qt.AlignmentFlag.AlignRight
        )

        layout.addWidget(self.status)

        container = QWidget()

        container.setLayout(layout)

        self.setCentralWidget(container)

        self.update_table()

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.update_table
        )

        self.timer.start(3000)

    def update_table(self):

        predictions = get_all_predictions()

        self.table.setRowCount(
            len(predictions)
        )

        for row, item in enumerate(predictions):

            self.table.setItem(
                row,
                0,
                QTableWidgetItem(
                    item["pair"]
                )
            )

            forecast_item = QTableWidgetItem(
                f'{item["forecast"]}%'
            )

            if item["forecast"] > 0:
                forecast_item.setForeground(
                    QColor("#22c55e")
                )
            else:
                forecast_item.setForeground(
                    QColor("#ef4444")
                )

            self.table.setItem(
                row,
                1,
                forecast_item
            )

            conf_item = QTableWidgetItem(
                f'{item["confidence"]}%'
            )

            self.table.setItem(
                row,
                2,
                conf_item
            )

            signal_item = QTableWidgetItem(
                item["signal"]
            )

            if "LONG" in item["signal"]:
                signal_item.setForeground(
                    QColor("#22c55e")
                )

            if "SHORT" in item["signal"]:
                signal_item.setForeground(
                    QColor("#ef4444")
                )

            self.table.setItem(
                row,
                3,
                signal_item
            )

            self.table.setItem(
                row,
                4,
                QTableWidgetItem(
                    item["horizon"]
                )
            )

        self.status.setText(
            "Last Update: "
            + datetime.now().strftime("%H:%M:%S")
        )


app = QApplication(sys.argv)

window = TradingWindow()

window.show()

sys.exit(app.exec())