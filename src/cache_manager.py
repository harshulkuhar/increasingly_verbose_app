from typing import Dict, Tuple, Union
import logging

logger = logging.getLogger(__name__)

class CacheManager:
    def __init__(self):
        self._cache: Dict[str, Tuple[str, str]] = {}
    
    def get_cached_response(self, input_text: str) -> Union[Tuple[str, str], None]:
        """Returns (filtered_sentence, verbose_response) if cached, None otherwise"""
        return self._cache.get(input_text)
    
    def cache_response(self, input_text: str, filtered_sentence: str, verbose_response: str) -> None:
        """Store the response in cache"""
        self._cache[input_text] = (filtered_sentence, verbose_response)
        logger.info(f"Cached response for input: {input_text[:50]}...")
