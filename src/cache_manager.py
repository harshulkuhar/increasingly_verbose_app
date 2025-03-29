from typing import Dict, Tuple, Union
import logging
from sentence_transformers import SentenceTransformer
import numpy as np
from dataclasses import dataclass
from datetime import datetime
import torch

torch.classes.__path__ = []

logger = logging.getLogger(__name__)

@dataclass
class CacheEntry:
    filtered_sentence: str
    verbose_response: str
    embedding: np.ndarray
    timestamp: datetime

class CacheManager:
    def __init__(self, similarity_threshold: float = 0.71):
        self._cache: Dict[str, CacheEntry] = {}
        self._model = SentenceTransformer('all-MiniLM-L6-v2')
        self._similarity_threshold = similarity_threshold
    
    def _get_embedding(self, text: str) -> np.ndarray:
        """Generate embedding for the input text"""
        return self._model.encode(text, convert_to_numpy=True)
    
    def _cosine_similarity(self, emb1: np.ndarray, emb2: np.ndarray) -> float:
        """Calculate cosine similarity between two embeddings"""
        return np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2))
    
    def get_cached_response(self, input_text: str) -> Union[Tuple[str, str], None]:
        """Returns (filtered_sentence, verbose_response) if a similar input is cached, None otherwise"""
        input_embedding = self._get_embedding(input_text)
        
        for cached_text, entry in self._cache.items():
            similarity = self._cosine_similarity(input_embedding, entry.embedding)
            if similarity >= self._similarity_threshold:
                logger.info(f"""
                    Found semantically similar cached response ::
                        Input :: {input_text[:50]}...
                        Cache :: {cached_text[:50]}...
                        Similarity :: {similarity:.2f}
                    """)
                return entry.filtered_sentence, entry.verbose_response
        
        return None
    
    def cache_response(self, input_text: str, filtered_sentence: str, verbose_response: str) -> None:
        """Store the response in cache with its embedding"""
        embedding = self._get_embedding(input_text)
        entry = CacheEntry(
            filtered_sentence=filtered_sentence,
            verbose_response=verbose_response,
            embedding=embedding,
            timestamp=datetime.now()
        )
        self._cache[input_text] = entry
        logger.info(f"Added to cache :: {input_text[:50]}...")
