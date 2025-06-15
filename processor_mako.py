from typing import Any, List
import dotenv
from ismcore.utils.general_utils import build_template_text_v2, parse_response
from ismcore.model.processor_state import StateConfigCode
from ismcore.processor.base_processor import BaseProcessor
from ismcore.processor.monitored_processor_state import MonitoredUsage

from logger import log

dotenv.load_dotenv()
logging = log.getLogger(__name__)


class MakoProcessor(BaseProcessor, MonitoredUsage):

    @property
    def template(self):
        if self.config.template_id:
            template = self.storage.fetch_template(self.config.template_id)
            return template

        return None

    # TODO remove once core is reinstalled
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_template = self.template.template_content if self.template else None
        
        if not self.user_template:
            raise ValueError(f'unable execute blank template for state route id: {self.output_processor_state.id}')

    @property
    def config(self) -> StateConfigCode:
        return self.output_state.config

    # async def process_input_data(self, input_query_state: dict | List[dict], force: bool = False):
    async def process_input_data(self, input_data: dict | List[dict], force: bool = False):
        result = build_template_text_v2(self.template, input_data)
        result, result_type, raw = parse_response(result)

        await self.finalize_result(
            result=result,
            input_data=input_data,
            additional_query_state=None
        )


    async def _stream(self, input_data: Any, template: str):
        # For Mako templates, we'll process the entire template at once
        # and yield the result as a single chunk
        # result = build_template_text_v2(template or self.template, input_data)
        yield template
        # pass

    #
    # async def apply_states(self, query_states: [dict]):
    #     route_message = {
    #         "route_id": self.output_processor_state.id,
    #         "type": "query_state_list",
    #         "query_state_list": query_states
    #     }
    #
    #     await self.sync_store_route.(json.dumps(route_message))
