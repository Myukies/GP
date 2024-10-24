using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraShakeEffect : MonoBehaviour
{
    public Transform cameraTransform = default;
    private Vector3 _orignalPosOfCam = default; 
    public float shakeFrequency = default;


    // Start is called before the first frame update
    void Start()
    {
        _orignalPosOfCam = cameraTransform.position;
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKey(KeyCode.S))
        {
            CameraShake();
        }
        else if (Input.GetKeyUp(KeyCode.S))

        {
            StopShake();
        }

    }
    private void CameraShake()
    {
        cameraTransform.position = _orignalPosOfCam + UnityEngine.Random.insideUnitSphere * shakeFrequency;
    }

    private void StopShake()
    {
        cameraTransform.position = _orignalPosOfCam;
    }

}
