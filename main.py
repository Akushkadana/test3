import flet as ft


def get_result(score, attendance):
    if score < 0 or score > 100:
        return "Некорректный балл"

    if attendance < 0 or attendance > 100:
        return "Некорректная посещаемость"

    if score >= 90 and attendance >= 80:
        return "Отлично"

    if score >= 70 and attendance >= 70:
        return "Хорошо"

    if score >= 50 and attendance >= 60:
        return "Зачёт"

    return "Незачёт"


def main(page: ft.Page):
    page.title = "Результат студента"
    page.window_width = 500
    page.window_height = 600
    page.padding = 30

    title = ft.Text(
        "Определение результата студента",
        size=24,
        weight=ft.FontWeight.BOLD
    )

    score_input = ft.TextField(
        label="Баллы (0-100)",
        width=300
    )

    attendance_input = ft.TextField(
        label="Посещаемость (0-100)",
        width=300
    )

    result_text = ft.Text(
        "",
        size=22,
        weight=ft.FontWeight.BOLD
    )

    def calculate(e):
        try:
            score = float(score_input.value)
            attendance = float(attendance_input.value)

            result = get_result(score, attendance)

            result_text.value = result

            if result == "Отлично":
                result_text.color = "green"
            elif result == "Хорошо":
                result_text.color = "blue"
            elif result == "Зачёт":
                result_text.color = "orange"
            else:
                result_text.color = "red"

        except ValueError:
            result_text.value = "Введите числа!"
            result_text.color = "red"

        page.update()

    calculate_button = ft.Button(
        content="Определить результат",
        on_click=calculate
    )

    page.add(
        title,
        ft.Divider(),
        score_input,
        attendance_input,
        calculate_button,
        result_text
    )


ft.run(main)
