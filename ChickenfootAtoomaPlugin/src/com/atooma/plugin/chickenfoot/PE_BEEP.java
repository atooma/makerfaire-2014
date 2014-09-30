package com.atooma.plugin.chickenfoot;

import org.json.JSONException;
import org.json.JSONObject;

import android.content.Context;
import android.os.RemoteException;

import com.atooma.plugin.ParameterBundle;
import com.atooma.plugin.Performer;
import com.loopj.android.http.AsyncHttpClient;
import com.loopj.android.http.RequestParams;

public class PE_BEEP extends Performer {

	public PE_BEEP(Context context, String id, int version) {
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

		String url = baseUrl + "/beep";

		try {
			JSONObject json = new JSONObject("{\"duration\" : " + duration + "}");
			AsyncHttpClient client = new AsyncHttpClient();
			RequestParams params = new RequestParams();
			params.put("json", json.toString());
			client.post(url, params, null);
		} catch (JSONException e) {
			e.printStackTrace();
		}

		return new ParameterBundle();
	}

	@Override
	public void defineUI() {
		setTitle(R.string.pe_beep);
		setIcon(R.drawable.plugin_icon_el_normal);
	}

}
