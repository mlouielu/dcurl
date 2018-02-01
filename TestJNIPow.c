#include <jni.h>
#include "TestJNIPow.h"

void dcurl_init(int max_cpu_thread, int max_gpu_thread);

void dcurl_entry(char *trytes, int mwm);

JNIEXPORT void JNICALL Java_TestJNIPow_init(JNIEnv *env, jobject obj, jint max_cpu_thread, jint max_gpu_thread)
{
    dcurl_init(max_cpu_thread, max_gpu_thread);
}

JNIEXPORT void JNICALL Java_TestJNIPow_entry(JNIEnv *env, jobject obj, jstring trytes, jint mwm)
{
    char *c_trytes = (*env)->GetStringUTFChars(env, trytes, NULL);
    printf("%s\n", c_trytes);

    dcurl_entry(c_trytes, mwm);
}
