"""Initial data required for core sites."""

from nautobot.apps.jobs import register_jobs, IntegerVar

from nautobot_design_builder.design_job import DesignJob

from .context import InitialDesignContext


class InitialDesign(DesignJob):
    """Initialize the database with default values needed by the core site designs."""
    has_sensitive_variables = False

    has_sensitive_variables = False
    routers_per_site = IntegerVar(min_value=1, max_value=6, default=2)

    class Meta:
        """Metadata needed to implement the backbone site design."""

        name = "Initial Data"
        commit_default = False
        design_file = "designs/0001_design.yaml.j2"
        context_class = InitialDesignContext
        version = "1.0.0"
        description = "Establish the devices and site information for four sites: IAD5, LGA1, LAX11, SEA11."
        docs = """This design creates the following objects in the source of truth to establish the initia network environment in  four sites: IAD5, LGA1, LAX11, SEA11.

These sites belong to the America region (and different subregions), and use Juniper PTX10016 devices.

The user input data is:
    - Number of routers per site (integer)
    - The description for us-west-1 region (string)
"""

    def post_implementation(self, context, environment):
        debug_tag = '[DT]'
        self.logger.info(f'{debug_tag} POST IMPLEMENTATION')
        self.logger.info(f'{debug_tag} JOURNAL: {environment.journal.__dict__}')
        self.logger.info(f'{debug_tag} CONTEXT: {context.__dict__}')
        '''
        self.logger.info(f'{debug_tag} DESIGN KEYS: {self.designs.keys()}')
        self.logger.info(
            f"{debug_tag} DESIGN: {self.designs['designs/0001_design.yaml.j2']}"
        )
        if hasattr(self, 'rendered_design') and geattr(self, 'rendered_design'):
            self.logger.info(f'{debug_tag} RENDERED DESIGN: {self.rendered_design.__dict__}')
        if hasattr(self, 'rendered') and getattr(self, 'rendered'):
            self.logger.info(f'{debug_tag} RENDERED: {self.rendered.__dict__}')
        self.logger.info(f'{debug_tag} ENVIRONMENT: {environment.__dict__}')
        '''

name = "Demo Designs"
register_jobs(InitialDesign)
