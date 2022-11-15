import flet as ft

navigation_rail = ft.NavigationRail(
    selected_index=0,

    min_width=100,

    destinations=[
        ft.NavigationRailDestination(
            icon=ft.icons.FAVORITE_BORDER,
            selected_icon=ft.icons.FAVORITE,
            label="First"
        ),
        ft.NavigationRailDestination(
            icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
            selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
            label="Second",
        ),
    ]
)
