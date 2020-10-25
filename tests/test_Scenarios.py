from gitstats import RelativeEffortNormalizer, Templater
import pytest
from .scenarios import scenarios
import os


class TestScenarios:

    @pytest.mark.parametrize(
        "normalizer,normalizer_name,scenarios",
        [(RelativeEffortNormalizer(), "Relative Effort", scenarios)])
    def test(self, normalizer, normalizer_name, scenarios):

        template = Templater(template_name="scenario.j2",
                             searchpath=os.path.dirname(
                                 os.path.abspath(__file__))).get_template()

        outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              "scenarios/")
        os.makedirs(outdir, exist_ok=True)
        outfile = os.path.join(outdir, "{}.log".format(normalizer_name))
        with open(outfile, "w") as outfile:
            for scenario in scenarios:
                outfile.write(
                    template.render(
                        scenario=scenario,
                        scenario_result=normalizer.normalize(scenario)))
                outfile.write("\n")