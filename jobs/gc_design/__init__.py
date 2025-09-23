"""Initial data required for core sites."""

from nautobot.apps.jobs import register_jobs, IntegerVar

from nautobot_design_builder.design_job import DesignJob

from .context import GoldenConfigDesignContext


class GoldenConfigDesign(DesignJob):
    """Initialize the database with default values needed by the core site designs."""
    has_sensitive_variables = False

    has_sensitive_variables = False
    routers_per_site = IntegerVar(min_value=1, max_value=6, default=2)

    class Meta:
        """Metadata needed to implement the backbone site design."""

        name = "Golden Config Creation"
        commit_default = False
        design_file = "designs/0001.yaml.j2"
        context_class = GoldenConfigDesignContext
        version = "1.0.0"

    def post_implementation(self, context, environment):
        debug_tag = '[DT]'
        self.logger.info(f'{debug_tag} POST IMPLEMENTATION')
        self.logger.info(f'{debug_tag} JOURNAL: {environment.journal.__dict__}')
        self.logger.info(f'{debug_tag} CONTEXT: {context.__dict__}')

name = "Golden Config Designs"
register_jobs(GoldenConfigDesign)
