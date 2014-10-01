package com.atooma.plugin.chickenfoot;

import java.io.UnsupportedEncodingException;

import org.apache.http.entity.StringEntity;
import org.json.JSONException;
import org.json.JSONObject;

import android.content.Context;
import android.os.RemoteException;

import com.atooma.plugin.ParameterBundle;
import com.atooma.plugin.Performer;
import com.loopj.android.http.AsyncHttpClient;
import com.loopj.android.http.JsonHttpResponseHandler;

public class PE_LEFT extends Performer {

	public PE_LEFT(Context context, String id, int version) {
		super(context, id, version);
	}

	@Override
	public void declareParameters() {
		addParameter(R.string.address, R.string.address, "ADDRESS", "STRING", true);
		addParameter(R.string.duration, R.string.duration, "DURATION", "NUMBER", true);
	}

	@Override
	public ParameterBundle onInvoke(String ruleId, ParameterBundle parameters) throws RemoteException {
		String baseUrl = (String) parameters.get("ADDRESS");
		Double duration = (Double) parameters.get("DURATION");

		String url = baseUrl + "/move";

		try {
			JSONObject json = new JSONObject("{\"type\": \"left\", \"duration\" : " + duration + "}");
			AsyncHttpClient client = new AsyncHttpClient();
			StringEntity entity;
			try {
				entity = new StringEntity(json.toString());
				client.post(this.getContext(), url, null, entity, "application/json", new JsonHttpResponseHandler() {
					public void onSuccess(final JSONObject json) {

					}

					public void onFailure(final Throwable e, final JSONObject response) {
					}

				});
			} catch (UnsupportedEncodingException e1) {
			}
		} catch (JSONException e) {
			e.printStackTrace();
		}

		return new ParameterBundle();
	}

	@Override
	public void defineUI() {
		setTitle(R.string.pe_left);
		setIcon(R.drawable.icon_left);
	}

}
