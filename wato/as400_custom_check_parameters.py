register_check_parameters(
    _("Operating System Resources"),
    "as400",
    _("AS/400 CPU Usage and Jobs Levels"),
    Dictionary(
        elements = [
            ("cpu_levels",
                Dictionary(
                    elements= [
                        (
                            "levels",
                            Tuple(
                                title = _("Levels for cpu usage (%)"),
                                label = _("Levels for cpu usage (%)"),
                                elements = [
                                    Percentage(title = _("Warning at:" ), maxvalue = 1500.0),
                                    Percentage(title = _("Critical at:"), maxvalue = 1500.0),
                                ]
                            )
                        ),
                        (
                            "average",
                            Integer(title = _("Averaging on:"))
                        )
                    ]
                )
            ),
            ("jobs_levels",
                Tuple(
                    title = _("Levels for Jobs"),
                    label = _("Levels for Jobs"),
                    elements = [
                        Integer(title = _("Warning at:" ), maxvalue = 1000000),
                        Integer(title = _("Critical at:"), maxvalue = 1000000),
                    ]
                ),
            ),
        ],
    ),
    '',
    "dict"
)

