

import logging
import threading
import time
import random

logger = logging.getLogger(__name__)



class QueueStatsProcessor(threading.Thread):
  def __init__(
        self,
        stop_event,
        queues=[],
  ):
    threading.Thread.__init__(self)
    self.name = "queue_stats_processor"
    
    self.queues = queues
    self.stop_event = stop_event
  

  def run(self):
    logger.info("starting queue stats processor...")
    while not self.stop_event.is_set():
      for q in self.queues:
        logger.debug(f"queue stats: {q['name']}: {q['queue'].qsize() if q['queue'] is not None else 'None'}")
      time.sleep(random.uniform(4.5,5.5))

    logger.info("Exiting queue stats processor...")