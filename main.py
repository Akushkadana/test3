import flet as ft


def main(page: ft.Page):
    page.title = "Мой список задач"
    page.window_width = 500
    page.window_height = 600
    page.padding = 30

    title = ft.Text(
        "Мой список задач",
        size=28,
        weight=ft.FontWeight.BOLD
    )

    task_input = ft.TextField(
        label="Введите задачу",
        hint_text="Например: Сделать домашнее задание",
        expand=True
    )

    tasks = ft.Column()

    def add_task(e):
        if task_input.value.strip():
            checkbox = ft.Checkbox(
                label=task_input.value,
            )

            tasks.controls.append(checkbox)

            task_input.value = ""
            page.update()

    def clear_tasks(e):
        tasks.controls.clear()
        page.update()

    add_button = ft.Button(
        content="Добавить",
        on_click=add_task
    )

    clear_button = ft.Button(
        content="Очистить",
        on_click=clear_tasks
    )

    page.add(
        title,
        ft.Divider(),
        ft.Row(
            controls=[
                task_input,
                add_button
            ]
        ),
        ft.Divider(),
        tasks,
        clear_button
    )


ft.run(main)