
import threading

print('thread %s is running...' % threading.current_thread().name);
# => thread MainThread is running... 可以看出默认主线程 名叫 MainThread ?